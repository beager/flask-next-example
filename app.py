"""Flask application with Next.js server-side rendered (SSR) support.

This application provides support for typical Flask endpoints, and provides catch-all endpoints to
deliver static Next.js pages and assets. This example is useful for Flask applications that want
to incorporate Next.js in a piecemeal fashion."""
import json
import re

from flask import Flask, send_from_directory, abort, render_template

app = Flask(__name__)

# Next.js static path routes
NEXT_JS_STATIC_ROUTES = {}

# Next.js dynamic path routes (like "/path/to/[itemId]", new in Next.js 9)
NEXT_JS_DYNAMIC_ROUTES = []

# Regular expression used to identify dynamic routes
DYNAMIC_ROUTE_REGEX = re.compile('\[[^\/]+\]')

# Discern Next.js routes from the Next server's page manifest JSON
with open('.next/server/pages-manifest.json') as fh:
    for path, file_location in json.load(fh).items():
        if DYNAMIC_ROUTE_REGEX.search(path):
            # If we determine that a route is dynamic, transform that path into a regex
            NEXT_JS_DYNAMIC_ROUTES.append(
                ('^' + DYNAMIC_ROUTE_REGEX.sub('[^\/]+', path) + '$', file_location))
        else:
            # Otherwise, this route is static, and it can be put into a static routes dict
            NEXT_JS_STATIC_ROUTES[path] = file_location


@app.route('/')
def index():
    """A typical Flask route with a Jinja2 template."""
    return render_template('index.html')


@app.route('/_next/static/<path:path>')
def next_static(path):
    """Catch-all that sends a static asset requested by a Next.js page."""
    return send_from_directory('.next/static', path)


@app.route('/<path:path>')
def next_route(path):
    """Catch-all that sends a Next.js page."""
    # Prepend the received path with a slash so it matches Next.js's routing format
    path = '/' + path

    # Check if our path matches a static path in Next.js. If it does, send the corresponding file.
    if path in NEXT_JS_STATIC_ROUTES:
        return send_from_directory('.next/server', NEXT_JS_STATIC_ROUTES[path])

    # Otherwise, check the dynamic path regexes in order to see if any of them match.
    for path_regex, file_location in NEXT_JS_DYNAMIC_ROUTES:
        if re.match(path_regex, path):
            send_from_directory('.next/server', file_location)

    # If this matches neither a static nor a dynamic route, fail through to HTTP 404
    abort(404)
