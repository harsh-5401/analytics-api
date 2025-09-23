from fastapi import APIRouter
from .schema import Eventschema

router=APIRouter()

@router.get("/")
def read_events():
    # buunch of item in table 
    return {
        "items" : [1,2,3]
    }


@router.get("/{event_id}")
# single items 
def get_events(event_id:int)->Eventschema:
    return {
        "id" : event_id
    }