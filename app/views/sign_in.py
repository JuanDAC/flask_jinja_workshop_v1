from flask import render_template, request, session, redirect, url_for
from app.models.user import User, users
from app.views import app_views
from functools import reduce


@app_views.route('/', methods=["GET"])
def index():
    return render_template('sign_in.html')


@app_views.route('/', methods=["POST"])
def sign_in():
    name = request.form.get('name', False)
    password = request.form.get('password', False)

    if name and password:
        user_ckeck = list(filter(
            lambda user: user.check_credentials(name, password), users))
        user = None
        if len(user_ckeck) > 0:
            user = user_ckeck[0]
        else:
            user = User(**request.form)
            users.append(user)

        session['user_id'] = user.id
        return redirect(url_for('app_views.all_tasks', user_id=user.id))

    return redirect('/')
