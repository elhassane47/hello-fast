from typing import Any
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

import uuid

from sqlalchemy.orm import declarative_base

Base: Any = declarative_base()


class Store(Base):
    __tablename__ = "stores"
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.Text, nullable=False)
    phone = sa.Column(sa.Text)
    street = sa.Column(sa.Text, nullable=False)
    zipcode = sa.Column(sa.Text, nullable=False)
    email = sa.Column(sa.Text)


