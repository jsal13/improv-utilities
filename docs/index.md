# improvutilities

This page serves as the homepage for improvutilities.  The documentation follows the [diataxis](https://diataxis.fr/) style and is split up into four parts:

- [Tutorial](/tutorial)
- [How-to Guide](/how-to-guides)
- [Explanation](/explanation)
- [Reference Material](/reference)

## Quickstart

In general, if there is a question of how to do something (testing, etc.), defer to [this repository](https://github.com/fmind/mlops-python-package) which was the loose inspiration for this cookiecutter.  

Otherwise, to quickstart:

1. Go to the repo root.
2. Run `just env` to create the poetry env and go into the poetry shell.
3. Develop while in the poetry shell.

To generate docs, fill in anything you'd like in the **docs** section and run `just serve-docs`.

## Commands

Look at the `justfile` to see the various available commands.

## Project layout

```text
mkdocs.yml    # The configuration file.
docs/
├── explanation.md
├── how-to-guides.md
├── index.md
├── reference.md
└── tutorials.md
```

TODO: Add the other parts.
