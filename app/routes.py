from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'Brian'
    title = 'Coding Temple Intro to Flask'
    return render_template('index.html', name=name, title=title)

@app.route('/test')
def test():
    colors = ['blue', 'green', 'red', 'orange', 'pink', 'black']
    return render_template('test.html', title='Test Title!', colors=colors)