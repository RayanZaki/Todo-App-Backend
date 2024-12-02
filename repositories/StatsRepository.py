from models.StatsModel import Statistics
from fastapi import Depends
from sqlalchemy.orm import Session

from configs.Database import (
    get_db_connection,
)
from models.TodoModel import Todo


class StatsRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        """
        Constructor to initialize the StatsRepository with a database session.
        
        If no statistics data exists, it creates the initial stats entry.
        
        Args:
        - db (Session): The database session injected via Depends.
        """
        self.db = db
        if not self.db.query(Statistics).first():
            self.create(Statistics())

    

    def get(self) -> Statistics:
        """
        Retrieve the statistics object from the database.

        Returns:
        - The first Statistics object found in the database.
        """
        return self.db.query(Statistics).first()

    def create(self, stats: Statistics) -> Statistics:
        """
        Create a new statistics record in the database.

        Args:
        - stats (Statistics): The Statistics object to create.

        Returns:
        - The created Statistics object after it has been committed to the database.
        """
        self.db.add(stats)
        self.db.commit()
        self.db.refresh(stats)
        return stats

    def update(self, stats: Statistics) -> Statistics:
        """
        Update an existing statistics record in the database.

        Args:
        - stats (Statistics): The updated Statistics object.

        Returns:
        - The updated Statistics object after it has been committed to the database.
        """
        stats.id = 1
        self.db.merge(stats)
        self.db.commit()
        self.db.refresh(stats)
        return stats
