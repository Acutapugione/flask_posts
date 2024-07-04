from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, scoped_session


engine = create_engine("sqlite:///my_db.sql", echo=True)
session_factory = sessionmaker(bind=engine, autoflush=True)
Session = scoped_session(session_factory)


from .models import Base, Author, Comment, Post, CRUD


def up():
    Base.metadata.create_all(engine)


def down():
    Base.metadata.drop_all(engine)
