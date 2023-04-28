#!/bin/bash
# takes in a URL, sends POST request to the passed URL, and displays body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
