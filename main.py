#!/usr/bin/env python3
from flask import Flask, Response, render_template, request, abort
from faker import Faker

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

fake = Faker()
@app.route('/generate-users/')
def generate_users():
    count = request.args.get('count', default=100, type=int)
    if count > 10000:
        abort(400, 'GET par: count max >= 9999')
    users = [fake.name() + ' ' + fake.email() for _ in range(count)]
    return render_template('generate_users.html', users=users)

if __name__ == '__main__':
    app.debug = True
    app.run()