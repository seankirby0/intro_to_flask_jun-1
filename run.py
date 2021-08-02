from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Brian'
    title = 'Coding Temple Intro to Flask'
    return render_template('index.html', name=name, title=title)

@app.route('/test')
def test():
    colors = ['blue', 'green', 'red', 'orange', 'pink', 'black']
    return render_template('test.html', title='Test Title!', colors=colors)