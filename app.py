from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title='REST API WITH FASTAPI AND MONGODB',
    description='this is a simple REST API using fastapi and mongo db',
    version='0.0.1',
    openapi_tags=tags_metadata
)

app.include_router(user)
