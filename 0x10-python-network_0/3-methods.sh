#!/bin/bash
# a scrpt taking in a URL and displays all HTTP methods the server will accept
curl -Is "$1" | grep "Allow:" | cut -c 8-
