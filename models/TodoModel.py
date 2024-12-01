from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import relationship

from models.BaseModel import EntityMeta



class Todo(EntityMeta):
    __tablename__ = "todos"

    id = Column(Integer)
    title = Column(String(40), nullable=True)
    text = Column(String(100), nullable=False)
    done = Column(Boolean, nullable=False, default=False)
    modified = Column(Boolean, nullable=False, default=False)

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id,
            "title": self.title.__str__(),
            "text": self.text.__str__(),
            "done": self.done,
            "modified": self.modified,
        }

