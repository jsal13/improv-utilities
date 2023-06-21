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

MP4 Container format
H.264 Video Codec
AAC Audio
3500kbps bitrate
30 FPS
60 seconds maximum in length
1080p 16:9 max (vertical or horizontal)
