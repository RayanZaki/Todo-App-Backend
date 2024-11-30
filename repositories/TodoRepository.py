from typing import List, Optional, Tuple

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
    ) -> Tuple[List[Todo], int]:
        query = self.db.query(Todo)

        
        return query.offset(start).limit(limit).all(), query.count()

    def get(self, todo: Todo) -> Todo:
        return self.db.get(
            Todo, todo.id
        )

    def create(self, todo: Todo) -> Todo:
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def update(self, id: int, todo: Todo) -> Todo:
        todo.id = id
        self.db.merge(todo)
        self.db.commit()
        return todo

    def delete(self, todo: Todo) -> None:
        todo = self.db.query(Todo).filter(Todo.id == todo.id).first()
        self.db.delete(todo)
        self.db.commit()
        self.db.flush()
