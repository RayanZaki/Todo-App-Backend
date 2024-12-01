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
        self.db = db
        if not self.db.query(Statistics).first():
            self.create(Statistics())

    

    def get(self) -> Statistics:
        return self.db.query(Statistics).first()

    def create(self, stats: Statistics) -> Statistics:
        self.db.add(stats)
        self.db.commit()
        self.db.refresh(stats)
        return stats

    def update(self, stats: Statistics) -> Statistics:
        stats.id = 1
        self.db.merge(stats)
        self.db.commit()
        self.db.refresh(stats)
        return stats
