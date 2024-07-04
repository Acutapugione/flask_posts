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


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    title: Mapped[str]
    content: Mapped[str]
    post: Mapped["Post"] = relationship(back_populates="comments", init=False)  # type: ignore
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), init=False)

    author: Mapped["Author"] = relationship(back_populates="comments", init=False)  # type: ignore
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), init=False)

    published_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), default=None
    )
