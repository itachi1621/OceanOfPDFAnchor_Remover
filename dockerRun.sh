#!/bin/bash
docker run --rm -v "$(pwd)/input:/app/input" -v "$(pwd)/output:/app/output" oceanepubcleaner

