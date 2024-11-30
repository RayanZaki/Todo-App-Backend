from sqlalchemy import (
    Column,
    Integer,
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
    

    PrimaryKeyConstraint(id)

    def normalize(self):
        return {
            "id": self.id,
            "title": self.title.__str__(),
            "text": self.text.__str__(),
        }

