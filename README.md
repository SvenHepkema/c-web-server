# tiny-django

This project consists of c code that interoperates with python to create my own implementation of a server that can serve simple html webpages. Users can create their own website by simply registrating webpages with, and the framework handles all of the server stuff via the C code that it interoperates with.

The following piece of code is a full example of how a programmer can create their own website in just a few lines of code. To create the server, simply create a `Server` object. To then create webpages, the user can create `HtmlPage` objects and use it's functions via the builder pattern to create a html page. There are also methods to insert plain html into the webpage, to give the user the freedom to use other elements of html as well. After the object is done, simply call the register function on the page, and the server will then know what to return when a user accesses the corresponding url. After all necessary pages are added, start the server via the `start()` method.

```python
from server import Server, HtmlPage

server = Server(port=8080)

home_page = (HtmlPage(server, "home")
    .header("Home")
    .paragraph("This is the home page.")
    .subheader("Introduction")
    .paragraph("Here is some information about my subject")
    .register())

about_page = (HtmlPage(server, "about")
    .header("About")
    .paragraph("This is the about page.")
    .link_button("Go back to the homepage", home_page)
    .register())

server.start()
```

Obviously this framework is not meant for serious use, but simply a hobby project to become more familiar with programming a server in C, interoperating C with Python and creating a simple but user friendly API in python.

# Running & Compilation

An example webserver can be run by simply running the shell script in the root of the directory. There is a makefile in the c-server directory to compile the shared library separately. To run the server from python, simply import the `server.py` module and follow the example above.

# Features

The python code supports:

- Defining paths and static responses.
- A python class that can be used to easily create a simple html webpage.
- A C server that interoperates with the python code to handle all of the low level server stuff.

# Inspiration

This project is heavily inspired by [tiny-web-server](https://github.com/shenfeng/tiny-web-server/tree/master) and the idea of generating webpages using python was taken from [Django](https://github.com/django/django). A lot of the initial structure and code was taken from [How I Built a Simple HTTP Server from Scratch using C](https://dev.to/jeffreythecoder/how-i-built-a-simple-http-server-from-scratch-using-c-739) ([Github Code](https://github.com/JeffreytheCoder/Simple-HTTP-Server/blob/master/server.c)).
