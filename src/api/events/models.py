# from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session,DateTime
from typing import Optional
# from sqlalchemy import DateTime
from datetime import datetime, timezone
from fastapi import Depends
from typing import List

def get_utc_now():
    return datetime.now(timezone.utc)  # already UTC aware


class EventModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    page: Optional[str] = ""
    description: Optional[str] = ""
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=DateTime(timezone=True),
        nullable=False,
    )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=DateTime(timezone=True),
        nullable=False,
    )

class Eventcreateschema(SQLModel):
    page:str
    description:Optional[str]=""


class Eventupdateschema(SQLModel):
    description:str    

class Eventlistschema(SQLModel):
    result:List[EventModel]
    count:int