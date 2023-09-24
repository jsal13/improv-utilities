# Improv Utilities

This repository will store any ops code, helper code, or other items related to working with the _Improv Utilities_.

- [Improv Utilities](#improv-utilities)
  - [Introduction](#introduction)
  - [Contributing](#contributing)

## Introduction

This repository will store any ops code, helper code, or other items related to working tech with improv people.

More specific instructions will be found in relevant folders.

## Requirements

- [Docker](https://www.docker.com/)
- [Just](https://www.docker.com/) (Optional)

## Quickstart

Use `just` to see the possible commands to run.

### Video Converting

The given video conversion is great at taking the (very large) movies from a phone and shrinking the file size while preserving quality.  The way to convert a video is:

```bash
just convert-video /path/to/movie.mp3
```

This will create a converted video in a `converted` folder in the same place as the original file.

## Contributing

To contribute, please create an Issue detailing the problem and a potential solution you have in mind; we'll triage from there!
