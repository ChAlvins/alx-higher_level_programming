#!/bin/bash
# makes request to the URL (0.0.0.0:5000/catch_me) and display the body of the response (You got me!)
curl -sLX PUT -d -H "Origin: HolbertonSchool" "user_id=98" 0.0.0.0:5000/catch_me
