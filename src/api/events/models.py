# from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import List, Optional

class EventModel(SQLModel , table=True):
    id:Optional[int]=Field(default=None , primary_key=True)
    # id:int 
    page:Optional[str]=""
    description:Optional[str]=""

class Eventcreateschema(SQLModel):
    page:str
    description:Optional[str]=""


class Eventupdateschema(SQLModel):
    description:str    

class Eventlistschema(SQLModel):
    result:List[EventModel]
    count:int