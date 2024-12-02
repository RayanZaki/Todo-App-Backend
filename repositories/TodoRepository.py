from typing import List, Optional, Tuple

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from sqlalchemy.sql import update

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
        query = query.order_by(Todo.id.desc())

        if limit == -1:
            return query.all(), query.count()
        # order 
        
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

    def update(self, id: int, todo: dict) -> Todo:
        upd = ( update(Todo).where(Todo.id == id).values(**todo))
        self.db.execute(upd)
        self.db.commit()
        return self.get(Todo(id=id))

    def delete(self, todo: Todo) -> None:
        todo = self.db.query(Todo).filter(Todo.id == todo.id).first()
        self.db.delete(todo)
        self.db.commit()
        self.db.flush()
