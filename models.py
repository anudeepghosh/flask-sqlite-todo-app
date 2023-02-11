from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///task.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = "task"
    t_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    remind_on = db.Column(db.DateTime)
    status = db.Column(db.String(20))