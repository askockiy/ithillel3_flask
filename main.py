#!/usr/bin/env python3
from flask import Flask, Response, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as f:
        content = f.read()
    resp = Response(content, mimetype='text/plain')
    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()