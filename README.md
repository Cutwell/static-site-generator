<!-- Update this link with your own project logo -->
# <img src="logo.png" style="width:64px;padding-right:20px;margin-bottom:-8px;"> Static Site Generator
 A CLI tool for converting Markdown to HTML.

<!-- Find new badges at https://shields.io/badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://img.shields.io/pypi/v/static-site-gen)](https://pypi.org/project/static-site-gen/)

[![Demo of the Read Me template command line app. It shows the user running.](demo.gif)](https://raw.githubusercontent.com/Cutwell/static-site-generator/main/demo.gif)

## Install

```sh
pip install static-site-gen
```

## Usage

```sh
ssg [-h] [--help] [--safe] [--debug] [--run=<project_root>] [--config=<config.toml>] [--ignore=<.ssgignore>]
```

|Flag|Description|
|:---:|:---:|
|`-h`, `--help`|Show this help message and exit (optional).|
|`--safe`|Don't overwrite existing files (optional).|
|`--run=`|Specify website root folder (required).|
|`--config=`|Default metadata configuration in YAML format (optional).|
|`--ignore=`|Filepath to list of newline separated file paths to skip (optional).|
|`--debug`|Enable debug logging (optional)|

## Docs

For further customisation and run instructions, see [here](./docs/index.md).

## Contributing

For information on how to set up your dev environment and contribute, see [here](.github/CONTRIBUTING.md).

## License

MIT
