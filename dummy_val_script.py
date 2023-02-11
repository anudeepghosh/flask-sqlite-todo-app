from app.extensions import db
from app.models.task import Task
import random
from datetime import datetime

year_range = [i for i in range(1900, 2014)]
month_range = [i for i in range(1,13)]
day_range = [i for i in range(1,28)]
hour_range = [i for i in range(0,24)]
min_range = [i for i in range(0,60)]
sec_range = [i for i in range(0,60)]
status_list = ['Active', 'Done', 'Active|Expired']


for i in range(0, 10):
    random_num = random.randrange(1, 1000)
    random_status = random.choice(status_list)
    random_ts = datetime(random.choice(year_range), random.choice(month_range), random.choice(day_range), random.choice(hour_range), random.choice(min_range), random.choice(sec_range))
    task = Task(task=f'Task #{random_num}', created_on=random_ts, status=f'{random_status}')
    db.session.add(task)
    print(task)
    print(task.created_on)
    print(task.status)
    print('--')
    db.session.commit()