import argparse
import os
import re
import tomllib
import fnmatch
import jinja2

import markdown
from tqdm import tqdm

TITLE = """\
  ____  _        _   _         ____  _ _           ____            
 / ___|| |_ __ _| |_(_) ___   / ___|(_) |_ ___    / ___| ___ _ __  
 \___ \| __/ _` | __| |/ __|  \___ \| | __/ _ \  | |  _ / _ \ '_ \ 
  ___) | || (_| | |_| | (__    ___) | | ||  __/  | |_| |  __/ | | |
 |____/ \__\__,_|\__|_|\___|  |____/|_|\__\___|   \____|\___|_| |_|
                                                                 
"""  # nopep8

global DEFAULT_HTML_TEMPLATE, DEFAULT_CONFIG, DEFAULT_IGNORE

DEFAULT_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
    </head>
    <body>
        {{ body }}
    </body>
</html>
"""  # nopep8

DEFAULT_CONFIG = {"title": "My Blog", "template": None}


def match_folder_path(folder_path, folder_list):
    for pattern in folder_list:
        if fnmatch.fnmatch(os.path.normpath(folder_path), os.path.normpath(pattern)):
            return True
    return False


def is_valid_folder_path(arg):
    if arg and not os.path.isdir(arg):
        raise argparse.ArgumentTypeError(f"'{arg}' is not a valid folder path.")
    return arg


def is_valid_file_path(arg):
    if arg and not os.path.isfile(arg):
        raise argparse.ArgumentTypeError(f"'{arg}' is not a valid file path.")
    return arg


def find_md_files(root_directory: str, ignore: list):
    md_files = []

    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            path = os.path.join(foldername, filename)
            if (
                filename.endswith(".md")
                and path not in ignore
                and not match_folder_path(foldername, ignore)
            ):
                md_files.append(path)

    return md_files


def parse_metadata_and_content(text):
    # Define a regular expression pattern to match the metadata table
    pattern = r"---\n(.*?)\n---"

    # Use re.DOTALL to match across newlines
    match = re.search(pattern, text, re.DOTALL)

    if match:
        # Extract the matched metadata table
        metadata_table = match.group(1)
        # Split the metadata into key-value pairs
        metadata_lines = metadata_table.split("\n")

        # Create a dictionary to store metadata
        metadata = {}
        for line in metadata_lines:
            if ":" in line:
                key, value = map(str.strip, line.split(":", 1))
                metadata[key] = value

        # Extract the remaining content after the metadata
        content_start = match.end()
        body = text[content_start:].strip()

        return metadata, body
    else:
        # If no metadata table is found, return an empty dictionary and the entire content

        return {}, text.strip()


def merge_dicts(default, target):
    for key in default:
        if key not in target:
            target[key] = default[key]
    return target


def replace_extension(filepath, new_extension="html"):
    # Split the file path into root and extension
    root, old_extension = os.path.splitext(filepath)

    # Create the new file path with the desired extension
    new_filepath = f"{root}.{new_extension}"

    return new_filepath


def core_dump(DEFAULT_CONFIG, ignore_list, md_files):
    print(f"DEFAULT CONFIG: {DEFAULT_CONFIG}")
    print(f"IGNORE LIST: {ignore_list}")
    print(f"MD FILES: {md_files}")


def main():
    global DEFAULT_HTML_TEMPLATE, DEFAULT_CONFIG, DEFAULT_IGNORE

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Static Site Generator")
    parser.add_argument(
        "--safe", action="store_true", help="Don't overwrite existing files (optional)."
    )
    parser.add_argument(
        "--run",
        type=is_valid_folder_path,
        help="Specify website root folder (required).",
    )
    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Default metadata configuration in YAML format (optional).",
    )
    parser.add_argument(
        "--ignore",
        type=str,
        default=None,
        help="List of newline separated file paths to skip (optional).",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging (optional).",
    )

    args = parser.parse_args()

    if args.config and is_valid_file_path(args.config):
        with open(args.config, "rb") as config_file:
            config_dict = tomllib.load(config_file)
            DEFAULT_CONFIG = merge_dicts(DEFAULT_CONFIG, config_dict["default"])

    ignore_list = []
    if args.ignore and is_valid_file_path(args.ignore):
        with open(args.ignore, "r") as ignore_file:
            ignore_list = ignore_file.read().splitlines()

        for path in ignore_list:
            if path[-1] == "*":
                ignore_list.append(path[:-1])

    print(TITLE)

    md_files = find_md_files(root_directory=args.run, ignore=ignore_list)

    if args.debug:
        print("DEBUG MODE")
        core_dump(DEFAULT_CONFIG, ignore_list, md_files)
    else:
        progress_bar = tqdm(
            total=len(md_files), desc="Generating static site files", unit="iteration"
        )

    # init Jinja2 enviroment for formatting templates
    environment = jinja2.Environment()

    for filepath in md_files:
        try:
            with open(filepath, "r") as file:
                metadata, body = parse_metadata_and_content(file.read())
                metadata = merge_dicts(DEFAULT_CONFIG, metadata)
                template = environment.from_string(DEFAULT_HTML_TEMPLATE)

                if "template" in metadata and is_valid_file_path(metadata["template"]):
                    with open(metadata["template"], "r") as template_file:
                        template = environment.from_string(template_file.read())

                output = template.render(
                    title=metadata["title"],
                    body=markdown.markdown(body, extensions=["codehilite"]),
                )

                html_filepath = replace_extension(filepath, new_extension="html")

                if args.debug:
                    print(f"FILE: {filepath}, \t Metadata: {filepath}")

                # if in safe mode, only run if output file doesn't exist
                # or run + overwrite if safe mode is not enabled
                if (not args.safe) or (
                    args.safe and not is_valid_file_path(html_filepath)
                ):
                    with open(html_filepath, "w") as html_file:
                        html_file.write(output)

                if not args.debug:
                    progress_bar.update(1)

        except Exception as error:
            core_dump(DEFAULT_CONFIG, ignore_list, md_files)
            raise error

    if not args.debug:
        progress_bar.close()


def cli():
    main()


if __name__ == "__main__":
    main()
