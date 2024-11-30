from typing import Any, Dict, List, Optional, Tuple

from fastapi import Depends, status, HTTPException
from models.TodoModel import Todo

from repositories.TodoRepository import TodoRepository
from schemas.pydantic.TodoSchema import (
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
        if not self.bookRepository.get(Todo(id=todo_id)):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
        return self.bookRepository.delete(Todo(id=todo_id))

    def get(self, todo_id: int) -> Todo:
        if not self.bookRepository.get(Todo(id=todo_id)):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
        return self.bookRepository.get(Todo(id=todo_id))

    def list(
        self,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> Dict[str, Any]:
        
        todos, total = self.bookRepository.list(
            pageSize, startIndex
        )

        next_page = (startIndex + pageSize) // pageSize if startIndex + pageSize < total and todos else None
        prev_page = (startIndex - pageSize) // pageSize if startIndex - pageSize >= 0 and todos  else None
        
        return {
        "data": [
            todo.normalize()
            for todo in todos
        ], 
        "next_page": next_page, 
        "previous_page": prev_page
    }

    def update(
        self, book_id: int, todo_body: TodoSchema
    ) -> Todo:
        return self.bookRepository.update(
            book_id, Todo(title=todo_body.title, text=todo_body.text)
        )

