from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


class Base(MappedAsDataclass, DeclarativeBase):
    pass


from .author import Author
from .comment import Comment
from .post import Post
from .crud import CRUD
