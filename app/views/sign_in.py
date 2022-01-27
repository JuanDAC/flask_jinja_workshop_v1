from flask import render_template
from app.views import app_views 


@app_views.route('/')
def sign_in():
    constext = {}
    return render_template('sign_in.html', **constext)


