﻿import os

import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
