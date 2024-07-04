from contextlib import contextmanager
from sqlalchemy import select
from . import Base
from .. import engine, Session


class CRUD:
    def __init__(self) -> None:
        self.session = Session

    def get_list(self, model: Base, limit: int = -1, offset: int = 0) -> list[Base]:
        return self.session.scalars(select(model).offset(offset).limit(limit))
