from typing import Optional
from pydantic import BaseModel, Field


class TodoPostRequestSchema(BaseModel):
    title: str = Field(description="Title of the Todo", default="No Title")
    text: str = Field(description="Text of the Todo")


class TodoPatchRequestSchema(BaseModel):
    title: Optional[str] = Field(description="Title of the Todo", default=None)
    text: Optional[str] = Field(description="Text of the Todo", default=None)
    done: Optional[bool] = Field(description="Done status of the Todo", default=None)
    modified: Optional[bool] = Field(description="Modified status of the Todo", default=None)

class TodoSchema(TodoPatchRequestSchema):
    id: int = Field(...,description="ID of the Todo")
