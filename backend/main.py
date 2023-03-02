from fastapi import FastAPI

from database.postgres.base_model import BaseModel
from database.postgres.core import engine

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)

@app.get("/")
def read_root():
    return {"Hello": "World"}
