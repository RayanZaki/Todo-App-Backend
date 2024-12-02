from pydantic import BaseModel, Field


class StatisticsSchema(BaseModel):
    n_total_todos: int = Field(..., description="Total number of created Todos")
    n_todos: int = Field(..., description="Total number of existing Todos")
    n_modified: int = Field(..., description="Total number of modified Todos")
    n_modifications: int = Field(..., description="Total number of modifications of Todos")
    n_deleted: int = Field(..., description="Total number of Deleted Todos")