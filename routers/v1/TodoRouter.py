from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, status, BackgroundTasks

from schemas.pydantic.TodoSchema import (
    TodoPostRequestSchema,
    TodoSchema,
)
from services.TodoService import TodoService

TodoRouter = APIRouter(prefix="/v1/todos", tags=["todo"])


@TodoRouter.get("/", response_model=Dict[str, Any])
def index(
    pageSize: Optional[int] = 5,
    startIndex: Optional[int] = 0,
    todoService: TodoService = Depends(),
):
    
    return todoService.list(
            pageSize, startIndex
        )


@TodoRouter.get("/{id}", response_model=TodoSchema)
def get(id: int, todoService: TodoService = Depends()):
    return todoService.get(id).normalize()


@TodoRouter.post(
    "/",
    response_model=TodoSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    todo: TodoPostRequestSchema,
    backgroundTasks: BackgroundTasks,
    todoService: TodoService = Depends(),
):
    
    return todoService.create(todo, backgroundTasks).normalize()


@TodoRouter.patch("/{id}", response_model=TodoSchema)
def update(
    id: int,
    todo: TodoPostRequestSchema,
    todoService: TodoService = Depends(),
):
    return todoService.update(id, todo).normalize()

@TodoRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, backgroundTasks: BackgroundTasks, todoService: TodoService = Depends()):
        return todoService.delete(id, backgroundTasks)

