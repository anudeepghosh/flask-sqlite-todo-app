from app.extensions import db

class Task(db.Model):
    __tablename__ = "task"
    t_id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300), nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    remind_on = db.Column(db.DateTime)
    status = db.Column(db.String(50))

    def __repr__(self):
        return f'<Task "{self.task}">'