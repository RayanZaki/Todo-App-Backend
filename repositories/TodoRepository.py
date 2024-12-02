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
        """
        Constructor to initialize the TodoRepository.

        Args:
        - db (Session): The database session injected via Depends.
        """
        self.db = db

    def list(
        self,
        limit: Optional[int],
        start: Optional[int],
    ) -> Tuple[List[Todo], int]:
        """
        Retrieve a paginated list of todos.

        Args:
        - limit (int, optional): The number of todos to retrieve.
        - start (int, optional): The starting index to paginate the results.

        Returns:
        - A tuple containing:
          1. A list of Todo objects.
          2. The total count of todos in the database.
        """
        query = self.db.query(Todo)
        query = query.order_by(Todo.id.desc())

        if limit == -1:
            return query.all(), query.count()
        # order 
        
        return query.offset(start).limit(limit).all(), query.count()

    def get(self, todo: Todo) -> Todo:
        """
        Retrieve a single todo by its ID.

        Args:
        - todo (Todo): The todo object with the ID to search for.

        Returns:
        - The Todo object with the corresponding ID, or None if not found.
        """
        return self.db.get(
            Todo, todo.id
        )

    def create(self, todo: Todo) -> Todo:
        
        """
        Create a new todo in the database.

        Args:
        - todo (Todo): The Todo object to be created.

        Returns:
        - The created Todo object after being committed to the database.
        """
        self.db.add(todo)
        self.db.commit()
        self.db.refresh(todo)
        return todo

    def update(self, id: int, todo: dict) -> Todo:
        """
        Update an existing todo by its ID.

        Args:
        - id (int): The ID of the todo to update.
        - todo (dict): A dictionary containing the fields to update.

        Returns:
        - The updated Todo object.
        """
        upd = ( update(Todo).where(Todo.id == id).values(**todo))
        self.db.execute(upd)
        self.db.commit()
        return self.get(Todo(id=id))

    def delete(self, todo: Todo) -> None:
        """
        Delete a todo from the database.

        Args:
        - todo (Todo): The todo object to delete.

        Returns:
        - None: The method has no return value.
        """
        todo = self.db.query(Todo).filter(Todo.id == todo.id).first()
        self.db.delete(todo)
        self.db.commit()
        self.db.flush()
