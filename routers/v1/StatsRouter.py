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
    
    return statsService.get().normalize()