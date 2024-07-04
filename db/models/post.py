from typing import List
from . import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from datetime import datetime
from sqlalchemy import func


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    content: Mapped[str]
    published_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
    comments: Mapped[List["Comment"]] = relationship(back_populates="post", init=False)  # type: ignore

    author: Mapped["Author"] = relationship(back_populates="posts", init=False)  # type: ignore
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), init=False)
