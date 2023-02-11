from flask import render_template
from app.todo import bp
from app.extensions import db
from app.models.task import Task


@bp.route('/todos')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)