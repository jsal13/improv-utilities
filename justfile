set shell := ["zsh", "-cu"]

default:
    just --list

build-converter-docker:
    @docker build -t movieconverter -f ./video_pipeline/Dockerfile ./video_pipeline

convert-movie-dir DIR: build-converter-docker
    @docker run -v $(realpath {{DIR}}):/videos movieconverter

upload-to-s3 FILE:
    aws s3 cp {{FILE}} s3://industry-darlings-improv