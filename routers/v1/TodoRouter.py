from typing import List, Optional

from fastapi import APIRouter, Depends, status

from schemas.pydantic.TodoSchema import (
    TodoPostRequestSchema,
    TodoSchema,
)
from services.TodoService import TodoService

TodoRouter = APIRouter(prefix="/v1/todos", tags=["todo"])


@TodoRouter.get("/", response_model=List[TodoSchema])
def index(
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    todoService: TodoService = Depends(),
):
    return [
        todo.normalize()
        for todo in todoService.list(
            pageSize, startIndex
        )
    ]


@TodoRouter.get("/{id}", response_model=TodoSchema)
def get(id: int, todoService: TodoService = Depends()):
    return todoService.get(id).normalize()


@TodoRouter.post(
    "/",
    response_model=TodoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    book: TodoPostRequestSchema,
    todoService: TodoService = Depends(),
):
    return todoService.create(book).normalize()


@TodoRouter.patch("/{id}", response_model=TodoSchema)
def update(
    id: int,
    book: TodoPostRequestSchema,
    todoService: TodoService = Depends(),
):
    return todoService.update(id, book).normalize()


@TodoRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, todoService: TodoService = Depends()):
    return todoService.delete(id)

