from typing import Any, Generic, List, Optional, Type, TypeVar

import sqlalchemy
from fastapi import HTTPException

from app.db.models import Base
from pydantic import BaseModel
from sqlalchemy.orm import Session


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseService(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model:Type[ModelType], session: Session):
        self.model = model
        self.session = session

    def get(self, id:Any) -> Optional[ModelType]:
        obj = self.session.query(self.model).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj

    def create(self, obj: CreateSchemaType) -> ModelType:
        db_obj: ModelType = self.model(**obj.dict())
        self.session.add(db_obj)
        try:
            self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_obj

