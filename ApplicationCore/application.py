"""Application module."""
from flask import Flask
from DependenciesResources.containers import Container
from . import views

def create_app() -> Flask:
    container = Container()

    app = Flask(__name__)
    app.container = container
    app.add_url_rule("/", "index", views.index)

    return app