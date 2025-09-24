from typing import Union

from fastapi import FastAPI, Depends
from sqlmodel import Session
from api.events import router as event_router
from api.db.session import initdb
from contextlib import asynccontextmanager





@asynccontextmanager
async def lifespan(app:FastAPI):
    await initdb()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(event_router , prefix="/api/events")    



@app.get("/")
def read_root():
    return {"Hello": "Worlder"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/health")
def read_api_health():
    return {"status": "OK"}