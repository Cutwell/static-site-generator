# Contributing Guide

Thank you for investing your time in contributing to our project! :sparkles:.

## New contributor guide

To navigate our codebase with confidence, see the [README](README.md) :confetti_ball: file. Here are some resources to help you get started with open source contributions:

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)


## Getting started

We consider all sorts of contributions to our project, some of which don't even require writing a single line of code :sparkles:.

### Issues

#### Create a new issue

If you spot a problem, [search if an issue already exists](https://github.com/Cutwell/static-site-generator/issues). If a related issue doesn't exist, you can open a new issue using a relevant [issue form](https://github.com/Cutwell/static-site-generator/issues/new).

#### Solve an issue

Scan through our [existing issues](https://github.com/Cutwell/static-site-generator/issues) to find one that interests you. You can narrow down the search using `labels` as filters.

### Make Changes

1. Fork the repository.
- Using GitHub Desktop:
  - [Getting started with GitHub Desktop](https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/getting-started-with-github-desktop) will guide you through setting up Desktop.
  - Once Desktop is set up, you can use it to [fork the repo](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/cloning-and-forking-repositories-from-github-desktop)!

- Using the command line:
  - [Fork the repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#fork-an-example-repository) so that you can make your changes without affecting the original project until you're ready to merge them.

2. Install the app and dev dependencies:

If using `poetry`:

```sh
poetry install --with dev
```

3. Create a working branch and start with your changes!

### Commit your update

Commit the changes once you are happy with them. Don't forget to format your code according to the [ruff](https://github.com/astral-sh/ruff) style and check that all unit tests pass, in order to speed up the review process :zap:.

Run unit tests (from the project root) using:

```sh
poetry run pytest -s .
```

Auto-format your code to `ruff` standards (ran also from the project root) using:

```sh
poetry run ruff check .
poetry run ruff format .
```

### Update necessary docs

If you've made changes that affect the usage of the app, update the README with any new features or instructions.

If you've made changes that affect the visual output of the app, create a new demo GIF using [terminalizer](https://github.com/faressoft/terminalizer) and compress the output using [gifcompressor](https://gifcompressor.com). Use the `demo.yml` file to recreate the look and feel of the demo GIF.

### Pull Request

When you're finished with the changes, create a pull request, also known as a PR.
- Fill the "Ready for review" template so that we can review your PR. This template helps reviewers understand your changes as well as the purpose of your pull request.
- Don't forget to [link PR to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one.
- Enable the checkbox to [allow maintainer edits](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/allowing-changes-to-a-pull-request-branch-created-from-a-fork) so the branch can be updated for a merge.
Once you submit your PR, a maintainer will review your proposal. We may ask questions or request additional information.
- We may ask for changes to be made before a PR can be merged, either using [suggested changes](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/incorporating-feedback-in-your-pull-request) or pull request comments. You can apply suggested changes directly through the UI. You can make any other changes in your fork, then commit them to your branch.
- As you update your PR and apply changes, mark each conversation as [resolved](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/commenting-on-a-pull-request#resolving-conversations).
- If you run into any merge issues, checkout this [git tutorial](https://github.com/skills/resolve-merge-conflicts) to help you resolve merge conflicts and other issues.

### Your PR is merged!

Congratulations :tada::tada: :sparkles:.

Once your PR is merged, your contributions will be publicly visible on the repository.

Now that you are part of our community, check the [issues list](https://github.com/Cutwell/static-site-generator/issues) to see how else you can contribute.
