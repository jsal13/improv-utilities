set shell := ["zsh", "-cu"]

default:
    just --list

build-converter-docker:
    @docker build -t movieconverter -f ./video_pipeline/Dockerfile ./video_pipeline

convert-movie-dir DIR: build-converter-docker
    @docker run -v $(realpath {{DIR}}):/videos movieconverter