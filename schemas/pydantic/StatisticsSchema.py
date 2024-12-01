from pydantic import BaseModel, Field


class StatisticsSchema(BaseModel):
    n_total_todos: int = Field(..., title="Total number of created Todos")
    n_todos: int = Field(..., title="Total number of existing Todos")
    n_modified: int = Field(..., title="Total number of modified Todos")
    n_modifications: int = Field(..., title="Total number of modifications of Todos")
    n_deleted: int = Field(..., title="Total number of Deleted Todos")