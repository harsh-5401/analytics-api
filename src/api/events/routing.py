from fastapi import APIRouter
from .schema import Eventschema, Eventlistschema

router=APIRouter()

# api/events/
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


# POST method 

@router.post("/")
# single items 
def create_event(data: dict={}):
    print(data)
    return data


#  GET api/events/12
@router.get("/{event_id}")
# single items 
def get_events(event_id:int)->Eventschema:
    return {
        "id" : event_id
    }


#  PUT api/events/12
@router.put("/{event_id}")
# single items 
def update_event(event_id:int , payload:dict={})->Eventschema:
    return {
        "id" : event_id
    }


#  delete api/events/12
@router.delete("/{event_id}")
# single items 
def update_event(event_id:int , payload:dict={})->Eventschema:
    return {
        "id" : event_id
    }

