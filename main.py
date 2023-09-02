from fastapi import FastAPI, Depends

from app.schemas import StoreCreate, Store
from app.serivces.stores import StoresService, get_stores_service
from app.db.models import User
from app.schemas import UserCreate, UserRead, UserUpdate
from app.serivces.users import auth_backend, current_active_user, fastapi_users

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
) -> Store:
    return store_service.create(store)


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}