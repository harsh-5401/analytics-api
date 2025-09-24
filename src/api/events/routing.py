from fastapi import APIRouter
from .schema import Eventschema, Eventlistschema

router=APIRouter()

@router.get("/")
def read_events()->Eventlistschema:
    # buunch of item in table 
    return {
        "result" : [
            {"id" : 1},
            {"id" : 2},
        ],
        "count" : 88
    }


@router.get("/{event_id}")
# single items 
def get_events(event_id:int)->Eventschema:
    return {
        "id" : event_id
    }