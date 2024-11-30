from typing import List, Optional

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

    def create(self, book_body: TodoSchema) -> Todo:
        return self.bookRepository.create(
            Todo(name=book_body.name)
        )

    def delete(self, book_id: int) -> None:
        return self.bookRepository.delete(Todo(id=book_id))

    def get(self, book_id: int) -> Todo:
        return self.bookRepository.get(Todo(id=book_id))

    def list(
        self,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Todo]:
        return self.bookRepository.list(
            pageSize, startIndex
        )

    def update(
        self, book_id: int, book_body: TodoSchema
    ) -> Todo:
        return self.bookRepository.update(
            book_id, Todo(name=book_body.name)
        )

