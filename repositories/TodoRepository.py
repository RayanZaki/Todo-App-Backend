from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.TodoModel import Todo


class TodoRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> List[Todo]:
        query = self.db.query(Todo)


        return query.offset(start).limit(limit).all()

    def get(self, book: Todo) -> Todo:
        return self.db.get(
            Todo, book.id
        )

    def create(self, book: Todo) -> Todo:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, id: int, book: Todo) -> Todo:
        book.id = id
        self.db.merge(book)
        self.db.commit()
        return book

    def delete(self, book: Todo) -> None:
        self.db.delete(book)
        self.db.commit()
        self.db.flush()
