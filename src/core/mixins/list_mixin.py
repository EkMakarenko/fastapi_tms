from sqlalchemy import select

from src.core.db import Session
from src.core.mixins.base_mixin import BaseMixin


class ListMixin(BaseMixin):

    @classmethod
    def list (cls, session: Session) -> list:
        query = select(cls.table)
        objects = session.execute(query)
        return objects.scalars().all()
