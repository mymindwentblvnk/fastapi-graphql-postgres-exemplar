from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper
from strawberry.fastapi import GraphQLRouter

from app.schema import schema


app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url="postgresql://postgres:postgres@localhost:5432/postgres")
app.include_router(GraphQLRouter(schema), prefix="/graphql")
