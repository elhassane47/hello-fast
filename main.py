from fastapi import FastAPI, Depends

from app.db.schemas import StoreCreate, Store
from app.serivces import get_stores_service
from app.serivces.stores import StoresService
from app.db import models
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post(
    "/",
    response_model=Store,
    status_code=201,
    responses={409: {"description": "Conflict Error"}},
)
def create_store(
    store: StoreCreate, store_service: StoresService = Depends(get_stores_service)
) -> models.Store:
    return store_service.create(store)

