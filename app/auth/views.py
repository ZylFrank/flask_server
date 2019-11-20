from flask import request
from flask_login import login_required
from . import auth
from app.models import User
from .. import db


@auth.route('/login', methods=['POST'])
def login():
    return 'this is login page', 200


@auth.route('/register', methods=['POST'])
def register():
    user = User(
        username=request.form.get('username'),
        email=request.form.get('email'),
        password=request.form.get('password'),
    )
    db.session.add(user)
    return 'this is login page', 200


# 设置只用登录成功后才能访问
@auth.route('/view')
@login_required
def view():
    return 'only authenticated user are allowed!'
