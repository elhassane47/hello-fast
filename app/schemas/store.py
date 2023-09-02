from typing import Optional

from pydantic import BaseModel, EmailStr, HttpUrl
from pydantic.types import UUID4, constr


def to_camel(string: str) -> str:
    if "_" not in string:
        return string
    words = string.split("_")
    words = [words[0]] + [word.capitalize() for word in words[1:]]
    return "".join(words)


class StoreBase(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    street: Optional[str]
    email: Optional[EmailStr]
    zipcode: Optional[str]


class StoreUpdate(StoreBase):
    pass


class StoreCreate(StoreBase):
    name: str
    phone: str
    zipcode: str
    street: str


class Store(StoreBase):
    id: UUID4

    class Config:
        orm_mode = True
        alias_generator = to_camel
        allow_population_by_field_name = True




