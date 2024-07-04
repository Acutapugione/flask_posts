from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker


from .models import Base, Author, Comment, Post


engine = create_engine("sqlite:///my_db.sql", echo=True)
Session = sessionmaker(engine)


def up():
    Base.metadata.create_all(engine)


def down():
    Base.metadata.drop_all(engine)
