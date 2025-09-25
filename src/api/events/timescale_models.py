# from pydantic import BaseModel
from sqlmodel import SQLModel, Field, Session
from typing import Optional
from sqlalchemy import DateTime
from datetime import datetime, timezone
from fastapi import Depends
from typing import List
from timescaledb import TimescaleModel

def get_utc_now():
    return datetime.now(timezone.utc)  # already UTC aware

# // page visits at any point in time

class EventModel(TimescaleModel, table=True):
    # id: Optional[int] = Field(default=None, primary_key=True) 
    # page: Optional[str] = ""
    page:str=Field(index=True) # / about , /contact 
    description: Optional[str] = "" 
    # created_at: datetime = Field(
    #     default_factory=get_utc_now,
    #     sa_type=DateTime(timezone=True),
    #     nullable=False,
    # )
    updated_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=DateTime(timezone=True),
        nullable=False,
    )
    __chunk_time_interval__= "INTERVAL  1 day"
    __drop_after__= "INTERVAL 90 days"

class Eventcreateschema(SQLModel):
    page:str
    description:Optional[str]=""


class Eventupdateschema(SQLModel):
    description:str    

class Eventlistschema(SQLModel):
    result:List[EventModel]
    count:int