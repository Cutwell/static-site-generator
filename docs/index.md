---
title: Static Site Gen /docs
---

# Static Site Gen /docs

## Self-compile

Install `ssg` with dependencies to test:

```sh
poetry install --with dev
```

Build (from project root) with:

```sh
poetry run ssg --run=./docs --config=./docs/config.toml --ignore=./.ssgignore
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

## Customisation

### Global metadata settings

Example metadata (saved as `.toml` file and specified using `--config=` setting):

```toml
[default]
title="My Title"
template="/path/to/file.html"
rootdir="/absolute/path/to/rootdir"
```

### Individual metadata settings

Example metadata (at top of `.md` files):

```markdown
---
title: My Title
template: /path/to/file.html
---
```

### Jinja2 HTML Templating

* We use Jinja2 for formatting generated HTML (and other variables) into the HTML template:

```html
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
```

## Run locally

### Install dependencies

```sh
poetry install --without dev
```

### Usage

Run the program from the command line (from the project root) like this:

```sh
poetry run ssg run .
```

