---
title: hi
template: ./static_site_gen/tests/templates/index.html
---

Hi, this is my blog.

Install `ssg` with dev dependencies to test:

```sh
poetry install --with dev
```

Build with:

```sh
poetry run ssg --run=./static_site_gen/tests --config=./static_site_gen/tests/config.toml
```

Run with a simple Flask server:

```sh
poetry run flask --app=./static_site_gen/tests/server.py run
```

Thanks for reading!
