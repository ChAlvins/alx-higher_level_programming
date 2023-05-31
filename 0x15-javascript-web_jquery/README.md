
# 0x15. JavaScript - Web jQuery


### Concepts

_For this project, we expect you to look at these concepts:_

-   [JavaScript in the browser](https://intranet.alxswe.com/concepts/3)
-   [Dealing with data statically versus dynamically](https://intranet.alxswe.com/concepts/35)


![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/4724718.jpg)

## Resources

-   [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
-   [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
-   [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
-   [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
-   [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
-   [API](https://oscarotero.com/jquery/)
-   [Introduction](https://jquery-tutorial.net/ajax/introduction/)
-   [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
-   [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
-   [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
-   [JQuery](https://jquery.com/)
-   [JQuery API](https://api.jquery.com/)
-   [JQuery Ajax](https://learn.jquery.com/ajax/)

## Learning Objectives

### General

-   Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
-   How to select HTML elements in JavaScript
-   How to select HTML elements with JQuery
-   What are differences between  `ID`,  `class`  and  `tag name`  selectors
-   How to modify an HTML element style
-   How to get and update an HTML element content
-   How to modify the DOM
-   How to make a  `GET`  request with JQuery Ajax
-   How to make a  `POST`  request with JQuery Ajax
-   How to listen/bind to DOM events

## Requirements

### General

-   Allowed editors:  `vi`,  `vim`,  `emacs`
-   All your files will be interpreted on Chrome (version 57.0)
-   All your files should end with a new line
-   A  `README.md`  file, at the root of the folder of the project, is mandatory
-   Your code should be  `semistandard`  compliant with the flag  `--global $`:  `semistandard *.js --global $`
-   You must use JQuery version 3.x
-   You are not allowed to use  `var`
-   HTML should not reload for each action: DOM manipulation, update values, fetch data…

## More Info

### Import JQuery

```
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>

```

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/305/1f1ihd.jpg)

### [0. No jQuery](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/0-script.js)

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`):

-   You must use  `document.querySelector`  to select the HTML tag
-   You can’t use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 0-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="0-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [1. With jQuery](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/1-script.js)

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`):

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 1-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="1-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [2. Click and turn red](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/2-script.js)

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`) when the user clicks on the tag  `DIV#red_header`:

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 2-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="2-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```


### [3. Add  `.red`  class](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/3-script.js)

Write a JavaScript script that adds the class  `red`  to the  `<header>`  element when the user clicks on the tag  `DIV#red_header`

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 3-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
    </style>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <div id="red_header">Red header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="3-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [4. Toggle classes](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/4-script.js)

Write a JavaScript script that toggles the class of the  `<header>`  element when the user clicks on the tag  `DIV#toggle_header`:

-   The  `<header>`  element must always have one class:  `red`  or  `green`, never both in the same time and never empty.
-   If the current class is  `red`, when the user click on  `DIV#toggle_header`, the class must be updated to  `green`  ; and the reverse.
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 4-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <style>
      .red {
        color: #FF0000;
      }
      .green {
        color: #00FF00;
      }
    </style>
  </head>
  <body>
    <header class="green"> 
      First HTML page
    </header>
    <div id="toggle_header">Toggle header</div>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="4-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [5. List of elements](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/5-script.js)

Write a JavaScript script that adds a  `<li>`  element to a list when the user clicks on the tag  `DIV#add_item`:

-   The new element must be:  `<li>Item</li>`
-   The new element must be added to  `UL.my_list`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 5-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="5-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [6. Change the text](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/6-script.js)

Write a JavaScript script that updates the text of the  `<header>`  element to  `New Header!!!`  when the user clicks on  `DIV#update_header`

-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 6-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="update_header">Update the header</div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="6-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [7. Star wars character](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/7-script.js)

Write a JavaScript script that fetches the character  `name`  from this URL:  `https://swapi-api.alx-tools.com/api/people/5/?format=json`

-   The name must be displayed in the HTML tag  `DIV#character`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 7-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars character
    </header>
    <br />
    <div id="character"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="7-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [8. Star Wars movies](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/8-script.js)

Write a JavaScript script that fetches and lists the  `title`  for all movies by using this URL:  `https://swapi-api.alx-tools.com/api/films/?format=json`

-   All movie titles must be list in the HTML tag  `UL#list_movies`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 8-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
  </head>
  <body>
    <header> 
      Star Wars movies
    </header>
    <br />
    <ul id="list_movies">
    </ul>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
    <script type="text/javascript" src="8-script.js"></script>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [9. Say Hello!](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/9-script.js)

Write a JavaScript script that fetches from  `https://fourtonfish.com/hellosalut/?lang=fr`  and displays the value of  `hello`  from that fetch in the HTML tag  `DIV#hello`.

-   The translation of “hello” must be displayed in the HTML tag  `DIV#hello`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   Your script must work when it is imported from the  `<head>`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 9-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="9-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello!
    </header>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [10. No jQuery - document loaded](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/100-script.js)

Write a JavaScript script that updates the text color of the  `<header>`  element to red (`#FF0000`):

-   You must use  `document.querySelector`  to select the HTML tag
-   You can’t use the jQuery API
-   Note: Your script must be imported from the  `<head>`  tag, not at the end of the HTML

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 100-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script type="text/javascript" src="100-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [11. List, add, remove](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/101-script.js)

Write a JavaScript script that adds, removes and clears  `LI`  elements from a list when the user clicks:

-   The new element must be:  `<li>Item</li>`
-   The new element must be added to  `UL.my_list`
-   When the user clicks on  `DIV#add_item`: a new element is added to the list
-   When the user clicks on  `DIV#remove_item`: the last element is removed from the list
-   When the user clicks on  `DIV#clear_list`: all elements of the list are removed
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   You script must work when it imported from the  `HEAD`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 101-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="101-script.js"></script>
  </head>
  <body>
    <header> 
      First HTML page
    </header>
    <br />
    <div id="add_item">Add item</div>
    <div id="remove_item">Remove item</div>
    <div id="clear_list">Clear list</div>
    <br />
    <ul class="my_list">
      <li>Item</li>
    </ul>
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [12. Say hello to everybody!](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/102-script.js)

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

-   You should use this API service:  `https://www.fourtonfish.com/hellosalut/hello/`
-   The language code will be the value entered in the tag  `INPUT#language_code`  (ex:  `es`,  `fr`,  `en`  etc.)
-   The translation must be fetched when the user clicks on  `INPUT#btn_translate`
-   The translation of “Hello” must be displayed in the HTML tag  `DIV#hello`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   You script must work when imported from the  `<head>`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 102-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="102-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```
### [13. And press ENTER](https://github.com/vpnchengo/alx-higher_level_programming/blob/master/0x15-javascript-web_jquery/103-script.js)

Write a JavaScript script that fetches and prints how to say “Hello” depending on the language

-   You should use this API service:  `https://www.fourtonfish.com/hellosalut/hello/`
-   The language code will be the value entered in the tag  `INPUT#language_code`  (ex:  `es`,  `fr`,  `en`  etc.)
-   The translation must be fetched when the user clicks on  `INPUT#btn_translate`  OR presses  `ENTER`  when the focus is on  `INPUT#language_code`
-   The translation of “Hello” must be displayed in the HTML tag  `DIV#hello`
-   You can’t use  `document.querySelector`  to select the HTML tag
-   You must use the JQuery API
-   You script must work when imported from the  `<head>`  tag

Please test with this HTML file in your browser:

```
guillaume@ubuntu:~/0x15$ cat 103-main.html 
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Holberton School</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
    <script type="text/javascript" src="103-script.js"></script>
  </head>
  <body>
    <header> 
      Say Hello
    </header>
    <br />
    <input id="language_code" type="text" placeholder="Language code"/>
    <input id="btn_translate" type="button" value="Translate"/>
    <br />
    <div id="hello"></div>
    <br />
    <footer>
      Holberton School - 2017
    </footer>
  </body>
</html>
guillaume@ubuntu:~/0x15$ 

```

---

## Author
---
-   [Alvin](https://github.com/vpnchengo)


