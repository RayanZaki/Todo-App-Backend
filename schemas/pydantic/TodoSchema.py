from typing import Optional
from pydantic import BaseModel, Field


class TodoPostRequestSchema(BaseModel):
    title: str = Field(title="Title of the Todo", default="No Title")
    text: str = Field(title="Text of the Todo")


class TodoPatchRequestSchema(BaseModel):
    title: Optional[str] = Field(title="Title of the Todo", required=False, default=None)
    text: Optional[str] = Field(title="Text of the Todo", required=False, default=None)
    done: Optional[bool] = Field(title="Done status of the Todo", required=False, default=None)
    modified: Optional[bool] = Field(title="Modified status of the Todo", required=False, default=None)

class TodoSchema(TodoPatchRequestSchema):
    id: int = Field(...,title="ID of the Todo")
