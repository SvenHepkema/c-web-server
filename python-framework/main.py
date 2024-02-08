#!/usr/bin/python3

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
