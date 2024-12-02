from typing import Any, Dict, List, Optional

from schemas.pydantic.StatisticsSchema import StatisticsSchema
from models.StatsModel import Statistics
from fastapi import APIRouter, Depends, status, BackgroundTasks

from schemas.pydantic.TodoSchema import (
    TodoPatchRequestSchema,
    TodoPostRequestSchema,
    TodoSchema,
)
from services.StatsService import StatsService

StatsRouter = APIRouter(prefix="/v1/stats", tags=["todo", "stats"])


@StatsRouter.get("/", response_model=StatisticsSchema)
def index(
    statsService: StatsService = Depends(),
):
    """
    Retrieves the current statistics for todos.

    Endpoint:
    - `GET /v1/stats/`

    Parameters:
    - `statsService` (StatsService): Injected service to manage statistics.

    Returns:
    - `StatisticsSchema`: A normalized representation of the current statistics.

    Behavior:
    - Calls the `get()` method from `StatsService` to fetch statistics.
    - Normalizes the returned data using the model's `normalize()` method for a structured output.
    """    
    return statsService.get().normalize()