from flask import Flask, render_template, request, jsonify
from models import session as session, Task as Task
from datetime import datetime
import traceback
from models import app

if __name__ == '__main__':
    app.run()

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        pass
        print('Fetch request received')
        # for task in session.query(Task).all():
            # print(json.dumps(rec))
        # print(session.query(Task.t_id, Task.task, Task.created_on, Task.remind_on, Task.status).all())
        return jsonify({'tasks':[]})
    except:
        traceback.print_exc()
        return 'Error fetching the task'

    

@app.route('/task/new', methods=['POST'])
def add_task():
    try:
        pass
        print('Request received')
        print(request.json)
        print(request.json['task'])
        print(request.json['reminder'])
        timestmp = datetime.now().isoformat()
        session.add(Task(task=request.json['task'], remind_on=request.json['reminder'], created_on=timestmp, status='Active'))
        session.commit()
    except:
        traceback.print_exc()
        return 'Error adding the task'
    pass
    return 'Success'

@app.route('/task', methods=['PUT'])
def update_task():
    try:
        pass
        print('Request received')
        print(request.json)
        print(request.json['task_id'])
        print(request.json['task'])
        print(request.json['reminder'])
    except:
        return 'Error updating the task'
    pass
    return 'Success'