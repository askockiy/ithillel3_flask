#!/usr/bin/env python3
import csv, requests
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

@app.route('/mean/')
def mean():
    heights = []
    weights = []
    with open('hw.csv', 'r') as f:
        reader = csv.DictReader(f, fieldnames=["Index", "Height(Inches)", "Weight(Pounds)"])
        next(reader)
        for row in reader:
            heights.append(float(row['Height(Inches)']))
            weights.append(float(row['Weight(Pounds)']))
    avg_height = sum(heights) / len(heights)
    avg_weight = sum(weights) / len(weights)
    return render_template('mean.html', avg_height=avg_height, avg_weight=avg_weight)

@app.route('/space/')
def space():
    rd = requests.get("http://api.open-notify.org/astros.json").json()
    count = rd['number']
    return render_template('space.html', num_astronauts=count)
    

if __name__ == '__main__':
    app.debug = True
    app.run()