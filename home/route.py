from flask import Blueprint

home=Blueprint("home",__name__)

@home.route('/')

def homes():
    return "This The Landing page"

