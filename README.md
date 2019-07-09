# Flask + Next.js example

## Overview

This example shows how you can serve Next.js server-side rendered (SSR) files alongside Flask
endpoints. This is potentially useful for existing Flask projects that want to transition to a full
Next.js frontend and Flask backend without an all-or-nothing cutover.

## How to run this

1. Render Next.js static assets
```
yarn install
yarn build
```
1. Run the Flask app
```
pip install requirements.txt
FLASK_APP=app.py flask run
```
