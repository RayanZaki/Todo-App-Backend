from typing import List, Optional, Tuple

from fastapi import Depends
from models.TodoModel import Todo

from repositories.TodoRepository import TodoRepository
from schemas.pydantic.TodoSchema import (
    TodoPostRequestSchema,
    TodoSchema,
)


class TodoService:
    bookRepository: TodoRepository

    def __init__(
        self,
        bookRepository: TodoRepository = Depends(),
    ) -> None:
        self.bookRepository = bookRepository

    def create(self, todo_body: TodoSchema) -> Todo:
        db_todo = self.bookRepository.create(
            Todo(text=todo_body.text, title=todo_body.title)
        )
        return db_todo

    def delete(self, todo_id: int) -> None:
        return self.bookRepository.delete(Todo(id=todo_id))

    def get(self, todo_id: int) -> Todo:
        return self.bookRepository.get(Todo(id=todo_id))

    def list(
        self,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> Tuple[List[Todo], int]:
        
        return self.bookRepository.list(
            pageSize, startIndex
        )

    def update(
        self, book_id: int, todo_body: TodoSchema
    ) -> Todo:
        return self.bookRepository.update(
            book_id, Todo(title=todo_body.title, text=todo_body.text)
        )

