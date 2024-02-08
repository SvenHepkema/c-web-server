#!/usr/bin/python3

from server import Server, HtmlPage

server = Server(port=8080)

server.register(HtmlPage(server, "home")
                .header("Home")
                .paragraph("This is the home page."))
server.register(HtmlPage(server, "about")
                .header("About")
                .paragraph("This is the about page.")
                .subheader("Author")
                .paragraph("I am the author."))

server.start()

