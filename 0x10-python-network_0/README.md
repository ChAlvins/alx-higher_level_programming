﻿
# 0x10. Python - Network #0

## [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#resourcesbooks)Resources📚

Read or watch:

-   [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
-   [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

----------

## [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#learning-objectivesbulb)Learning Objectives💡

What you should learn from this project:

-   What a URL is
-   What HTTP is
-   How to read a URL
-   The scheme for a HTTP URL
-   What a domain name is
-   What a sub-domain is
-   How to define a port number in a URL
-   What a query string is
-   What an HTTP request is
-   What an HTTP response is
-   What HTTP headers are
-   What the HTTP message body is
-   What an HTTP request method is
-   What an HTTP response status code is
-   What an HTTP Cookie is
-   How to make a request with cURL
-   What happens when you type google.com in your browser (Application level)

----------

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#0-curl-body-size)[0. cURL body size](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/0-body_size.sh)

-   Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
-   The size must be displayed in bytes
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#1-curl-to-the-end)[1. cURL to the end](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/1-body.sh)

-   Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
-   Display only body of a 200 status code response
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#2-curl-method)[2. cURL Method](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/2-delete.sh)

-   Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#3-curl-only-methods)[3. cURL only methods](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/3-methods.sh)

-   Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#4-curl-headers)[4. cURL headers](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/4-header.sh)

-   Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
-   A header variable X-HolbertonSchool-User-Id must be sent with the value 98
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#5-curl-post-parameters)[5. cURL POST parameters](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/5-post_params.sh)

-   Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
-   A variable email must be sent with the value  [hr@holbertonschool.com](mailto:hr@holbertonschool.com)
-   A variable subject must be sent with the value I will always be here for PLD
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: hr@holbertonschool.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#6-find-a-peak)[6. Find a peak](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/6-peak.py)

-   Technical interview preparation:
-   You are not allowed to google anything
-   Whiteboard first

Write a function that finds a peak in a list of unsorted integers.

-   Prototype: def find_peak(list_of_integers):
-   You are not allowed to import any module
-   Your algorithm must have the lowest complexity
-   6-peak.py must contain the function
-   6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
-   Note: there may be more than one peak in the list

```
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#7-only-status-code)[7. Only status code](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/100-status_code.sh)

-   Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
-   You are not allowed to use any pipe, redirection, etc.
-   You are not allowed to use ; and &&
-   You have to use curl

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#8-curl-a-json-file)[8. cURL a JSON file](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/101-post_json.sh)

-   Write a Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
-   Your script must send a POST request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
-   You have to use curl

Please test your scripts in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 

```

### [](https://github.com/vpnchengo/alx-higher_level_programming/tree/master/0x10-python-network_0#9-catch-me-if-you-can)[9. Catch me if you can!](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x10-python-network_0/102-catch_me.sh)

-   Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
-   You have to use curl
-   You are not allow to use echo, cat, etc. to display the final result

Please test your script in the container provided, using the web server running on port 5000

```
guillaume@ubuntu:~/0x10$ ./102-catch_me.sh ; echo ""
You got me!
guillaume@ubuntu:~/0x10$ 

```
## [](https://github.com/vpnchengo/alx-higher_level_programming#authors)AUTHORS

-   [Alvin](https://github.com/vpnchengo)


