from sqlalchemy.ext.automap import automap_base
from sqlalchemy import Column, Integer, String, DateTime, Table, create_engine, MetaData
from sqlalchemy.orm import relationship, backref, Session
# from sqlalchemy.ext.declarative import declarative_base

Base = automap_base()

# class Task(Base):
#     __tablename__ = "task"
#     t_id = Column(Integer, primary_key=True)
#     task = Column(String)
#     created_on = Column(DateTime)
#     remind_on = Column(DateTime)
#     status = Column(String)

conn_str = 'sqlite:///task.db'
engine = create_engine(conn_str, echo=True)
Base.prepare(engine, reflect=True)
Task = Base.classes.task
session = Session(engine)
