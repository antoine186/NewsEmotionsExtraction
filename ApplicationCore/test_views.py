"""Views module."""

from flask import request, render_template

def index():
    query = request.args.get("query", "Dependency Injector")
    limit = request.args.get("limit", 10, int)

    repositories = []

    return render_template(
        "index.html",
        query=query,
        limit=limit,
        repositories=repositories,
    )