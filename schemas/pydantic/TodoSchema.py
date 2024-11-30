from pydantic import BaseModel


class TodoPostRequestSchema(BaseModel):
    id: str

class TodoSchema(TodoPostRequestSchema):
    title: str
    name: str
    content: str