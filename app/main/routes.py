from flask import render_template, redirect
from app.main import bp

@bp.route('/')
def index():
    # return 'This is The Main Blueprint'
    # return render_template('index.html')
    return redirect("/todos", code=302)