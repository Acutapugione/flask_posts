from typing import List
from . import Base
from sqlalchemy import ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from datetime import datetime


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    nickname: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]

    comments: Mapped[List["Comment"]] = relationship(back_populates="author", init=False)  # type: ignore
    posts: Mapped[List["Post"]] = relationship(back_populates="author", init=False)  # type: ignore
