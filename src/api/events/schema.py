from pydantic import BaseModel
from typing import List, Optional

class Eventcreateschema(BaseModel):
    page:str

class Eventupdateschema(BaseModel):
    description:str    

class Eventschema(BaseModel):
    id:int
    name:Optional[str]=""

class Eventlistschema(BaseModel):
    result:List[Eventschema]
    count:int