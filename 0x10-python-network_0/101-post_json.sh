#!/bin/bash
# sends a JSON POST request to URL passed as first argument and displays body of the response
curl -sH "Content-Type: application/json" -d @"$2" -X POST "$1"
