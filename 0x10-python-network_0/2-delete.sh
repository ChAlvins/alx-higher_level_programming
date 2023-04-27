#!/bin/bash
# deletes request to URL passed as 1st argument and displays the body of the response
curl -sX DELETE "$1"
