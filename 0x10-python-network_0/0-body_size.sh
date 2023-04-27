#!/bin/bash
# Get the body size of a request
curl -s "$1" | wc -c
