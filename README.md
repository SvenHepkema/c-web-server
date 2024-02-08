# Tiny-Django

This project consists of c code that interoperates with python to create my own implementation of a backend server that can be used from python code. The goal is to let the programmer respond via python to http requests.

# Features

The python code will support:

- Defining paths.
- Returning a response when a request is made to a path.
- Some python classes to standardize writing a response.
- A C server to handle all of the low level server stuff.

# Inspiration

This project is heavily inspired by [tiny-web-server](https://github.com/shenfeng/tiny-web-server/tree/master) and the general idea of [Django](https://github.com/django/django). A lot of the initial structure and code was taken from [How I Built a Simple HTTP Server from Scratch using C](https://dev.to/jeffreythecoder/how-i-built-a-simple-http-server-from-scratch-using-c-739) ([Github Code](https://github.com/JeffreytheCoder/Simple-HTTP-Server/blob/master/server.c)).
