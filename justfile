set shell := ["zsh", "-cu"]

default:
  just --list

docs-serve:
  mkdocs serve

docs-build:
  mkdocs build

env: poetry-install
  poetry shell 

poetry-install:
  poetry install

test:
  pytest --doctest-modules

docker-build-convert-video-image:
  @docker build -f ./improvutilities/video_conversion/Dockerfile -t video_conversion ./improvutilities/video_conversion

convert-video path_to_vid: docker-build-convert-video-image
  @video_path=$(realpath -- "$(dirname -- {{path_to_vid}})") \
  && video_filename=$(basename -- {{path_to_vid}}) \
  && echo "* Video Path: $video_path" \
  && echo "* Video File: $video_filename" \
  && docker run -v $video_path:/app/videos video_conversion /bin/sh -c "python /app/converter.py /app/videos/$video_filename"