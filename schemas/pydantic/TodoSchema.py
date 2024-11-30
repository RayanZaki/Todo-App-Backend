from pydantic import BaseModel, Field


class TodoPostRequestSchema(BaseModel):
    title: str = Field(title="Title of the Todo", default="No Title")
    text: str = Field(..., title="Text of the Todo")

class TodoSchema(TodoPostRequestSchema):
    id: int = Field(title="ID of the Todo")
