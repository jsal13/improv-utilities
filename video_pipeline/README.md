# Video Pipeline

This folder deals with the pipeline for videos: converting, uploading, etc.

- [Video Pipeline](#video-pipeline)
  - [Quickstart](#quickstart)

## Quickstart

To Convert a directory of movies:

```bash
# With Python:
python instagram_video_conversion/converter.py /path/to/the/mp4s/

# With `just` from the repo root:
just convert-movie-dir /path/to/the/mp4s/
```

## TODO:

- Docker for individual things.  That way we _parallelize_.
