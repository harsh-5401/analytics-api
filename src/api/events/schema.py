from pydantic import BaseModel
from typing import List

class Eventschema(BaseModel):
    id:int

class Eventlistschema(BaseModel):
    result:List[Eventschema]
    count:int