from typing import Any, Dict, List, Optional, Tuple

from services.StatsService import StatsService
from fastapi import Depends, status, HTTPException, BackgroundTasks
from models.TodoModel import Todo

from repositories.TodoRepository import TodoRepository
from schemas.pydantic.TodoSchema import (
    TodoPatchRequestSchema,
    TodoSchema,
)


class TodoService:
    statsService: StatsService
    todoRepository: TodoRepository

    def __init__(
        self,
        todoRepository: TodoRepository = Depends(),
        statsService: StatsService = Depends(),
    ) -> None:
        self.todoRepository = todoRepository
        self.statsService = statsService

    def create(self, todo_body: TodoSchema, backgroundTasks: BackgroundTasks) -> Todo:
        backgroundTasks.add_task(self.statsService.increment_todo_count)
        return self.todoRepository.create(
            Todo(text=todo_body.text, title=todo_body.title)
        )

    def delete(self, todo_id: int, backgroundTasks: BackgroundTasks) -> None:
        if not self.todoRepository.get(Todo(id=todo_id)):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
        
        backgroundTasks.add_task(self.statsService.increment_deleted_count)
        return self.todoRepository.delete(Todo(id=todo_id))

    def get(self, todo_id: int) -> Todo:
        if not self.todoRepository.get(Todo(id=todo_id)):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
        return self.todoRepository.get(Todo(id=todo_id))

    def list(
        self,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> Dict[str, Any]:
        
        todos, total = self.todoRepository.list(
            pageSize, startIndex * pageSize
        )

        next_page = (startIndex * pageSize + pageSize) // pageSize if startIndex * pageSize + pageSize < total and todos else None
        prev_page = (startIndex * pageSize - pageSize) // pageSize if startIndex * pageSize - pageSize >= 0 and todos  else None
        
        return {
        "data": [
            todo.normalize()
            for todo in todos
        ], 
        "next_page": next_page, 
        "previous_page": prev_page
    }

    def update(
        self, todo_id: int, todo_body: TodoPatchRequestSchema
    ) -> Todo:
        
        if not self.todoRepository.get(Todo(id=todo_id)):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

        todo_dict = todo_body.dict(exclude_unset=True)

        return self.todoRepository.update(
            todo_id, todo_dict
        )


