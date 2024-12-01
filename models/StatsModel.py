from sqlalchemy import (
    Column,
    Integer,
    PrimaryKeyConstraint,
    String,
)

from models.BaseModel import EntityMeta



class Statistics(EntityMeta):
    __tablename__ = "stats"

    id = Column(Integer)
    n_total_todos = Column(Integer, nullable=False, default=0)
    n_todos = Column(Integer, nullable=False, default=0)
    n_modified = Column(Integer, nullable=False, default=0)
    n_modifications = Column(Integer, nullable=False, default=0)
    n_deleted = Column(Integer, nullable=False, default=0)
    

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "n_total_todos": self.n_total_todos,
            "n_todos": self.n_todos,
            "n_modified": self.n_modified,
            "n_modifications": self.n_modifications,
            "n_deleted": self.n_deleted,
        }

