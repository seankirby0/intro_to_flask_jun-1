from app import app, db
from flask import render_template
from app.forms import RegisterForm
from app.models import User

@app.route('/')
def index():
    name = 'Brian'
    title = 'Coding Temple Intro to Flask'
    return render_template('index.html', name=name, title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Grab data from our submitted form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        # Create new instance of User
        new_user = User(username, email, password)

        # Add new_user to our database
        db.session.add(new_user)
        db.session.commit()

        
    return render_template('register.html', title='Register for CT Blog', form=form)