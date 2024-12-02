from routers.v1.StatsRouter import StatsRouter 
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

# from strawberry import Schema
# from strawberry.fastapi import GraphQLRouter

from configs.Environment import get_environment_variables
# from configs.GraphQL import get_graphql_context
from metadata.Tags import Tags
from models.BaseModel import init
from routers.v1.TodoRouter import TodoRouter
# from schemas.graphql.Query import Query
# from schemas.graphql.Mutation import Mutation

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title="env.APP_NAME",
    version="env.API_VERSION",
    openapi_tags=Tags,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Routers
app.include_router(TodoRouter)
app.include_router(StatsRouter)

# print(app.openapi())
# Initialise Data Model Attributes
# init()


