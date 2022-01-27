from flask import render_template, request
from app.views import app_views


@app_views.route('/<int:user_id>/add-task')
def add_task(user_id: int = None):
    constext = {}
    return render_template('add_task.html', **constext)


@app_views.route('/<int:user_id>/task')
def show_task(user_id: int = None):
    constext = {}
    task_id = request.args.get('id', None)
    return render_template('task.html', **constext)


@app_views.route('/<int:user_id>/')
@app_views.route('/<int:user_id>/tasks')
def all_tasks(user_id: int = None):
    constext = {}
    return render_template('tasks.html', **constext)
