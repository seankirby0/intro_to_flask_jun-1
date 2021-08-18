from app import app, db
from flask import jsonify, request
from app.models import User, Post


@app.route('/api/users')
def users():
    """
    [GET] /api/users
    """
    users = [u.to_dict() for u in User.query.all()]
    return jsonify(users=users)


@app.route('/api/create-user', methods=['POST'])
def create_user():
    """
    [POST] /api/create-user
    """
    data = request.get_json()
    # print(data)
    # print(type(data))
    # print(data['test1'])
    # print(type(data['test1']))

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

# Sad path - request body is missing key
    if not username or not email or not password:
        return jsonify('error: You need a username, email, and password'), 400

# Create new user
    new_user =User(username, email, password)

# Add new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict)

@app.route('/api/posts')
def posts():
    """
    [GET] /api/posts
    """
    posts = [p.to_dict() for p in Post.query.all()]
    return jsonify(posts=posts)


@app.route('/api/create-post', methods=['POST'])
def create_post():
    pass
    """
    [POST] /api/create-post
    """
    data = request.get_json()

    title = data.get('title')
    body = data.get('body')
    
    # if user not :
    #     return jsonify('error: You need a to sign in!'), 400

# Create new user
    new_post = Post(title, body,)

# Add new user to the database
    db.session.add(new_post)
    db.session.commit()

    return jsonify(new_post.to_dict)
