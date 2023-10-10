from fastapi import FastAPI

from src.core.db import Base, engine
from src.rest.api.router import router as api_router

app = FastAPI(
    title='Hotel App',
    docs_url='/api/docs',
)

app.include_router(api_router, prefix='/api')

Base.metadata.create_all(engine)
