from fastapi import APIRouter
from .schema import Eventschema, Eventlistschema, Eventcreateschema, Eventupdateschema

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



#  GET api/events/12 
@router.get("/{event_id}")
# single items 
def get_events(event_id:int)->Eventschema:
    return {
        "id" : event_id
    }


# POST method  create

@router.post("/")
# single items 
def create_event(payload:Eventcreateschema)->Eventschema:
    data=payload.model_dump()     #payload->dict ->pyndamic
    print(payload)
    return {
        "id" : 125
    }

#  PUT api/events/12
@router.put("/{event_id}")
# single items 
def update_event(event_id:int , payload:Eventupdateschema)->Eventschema:
    print(payload)
    return {
        "id" : event_id
    }


#  delete api/events/12
@router.delete("/{event_id}")
# single items 
def update_event(event_id:int , payload:dict={})->Eventschema:
    print(payload)
    return {
        "id" : event_id
    }

