from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, status, BackgroundTasks

from schemas.pydantic.TodoSchema import (
    TodoPatchRequestSchema,
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
    """
    List all todos with pagination.

    Endpoint:
    - `GET /v1/todos/`

    Parameters:
    - `pageSize` (int): Number of items per page.
    - `startIndex` (int): The index of the first page to retrieve.
    - `todoService` (TodoService): Injected service for managing todos.

    Returns:
    - A dictionary containing a paginated list of todos.
    """ 
    
    return todoService.list(
            pageSize, startIndex
        )


@TodoRouter.get("/{id}", response_model=TodoSchema)
def get(id: int, todoService: TodoService = Depends()):
    """
    Retrieve a specific todo by ID.

    Endpoint:
    - `GET /v1/todos/{id}`

    Parameters:
    - `id` (int): The ID of the todo to retrieve.
    - `todoService` (TodoService): Injected service for managing todos.

    Returns:
    - A normalized representation of the todo.
    """
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
    """
    Create a new todo.

    Endpoint:
    - `POST /v1/todos/`

    Parameters:
    - `todo` (TodoPostRequestSchema): The details of the todo to create.
    - `backgroundTasks` (BackgroundTasks): Background tasks for additional processing.
    - `todoService` (TodoService): Injected service for managing todos.

    Returns:
    - A normalized representation of the created todo.
    """
    
    return todoService.create(todo, backgroundTasks).normalize()


@TodoRouter.patch("/{id}", response_model=TodoSchema)
def update(
    id: int,
    todo: TodoPatchRequestSchema,
    todoService: TodoService = Depends(),
):
    """
    Update an existing todo by ID.

    Endpoint:
    - `PATCH /v1/todos/{id}`

    Parameters:
    - `id` (int): The ID of the todo to update.
    - `todo` (TodoPatchRequestSchema): Partial fields for updating the todo.
    - `todoService` (TodoService): Injected service for managing todos.

    Returns:
    - A normalized representation of the updated todo.
    """
    return todoService.update(id, todo).normalize()

@TodoRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(id: int, backgroundTasks: BackgroundTasks, todoService: TodoService = Depends()):
    """
    Delete a todo by ID.

    Endpoint:
    - `DELETE /v1/todos/{id}`

    Parameters:
    - `id` (int): The ID of the todo to delete.
    - `backgroundTasks` (BackgroundTasks): Background tasks for additional processing.
    - `todoService` (TodoService): Injected service for managing todos.

    Returns:
    - None, with a status code of 204 if the deletion is successful.
    """
    return todoService.delete(id, backgroundTasks)

