from fastapi import APIRouter, Depends, HTTPException
# from .schema import Eventschema, Eventlistschema, Eventcreateschema, Eventupdateschema
from api.db.config import DATABASE_URL
# from .models import EventModel, Eventlistschema, Eventcreateschema, Eventupdateschema, get_utc_now
from .timescale_models import EventModel, Eventlistschema, Eventcreateschema, Eventupdateschema, get_utc_now

from api.db.session import get_session
from sqlmodel import Session, select

router=APIRouter()
 
# api/events/ 
@router.get("/" , response_model=Eventlistschema)
def read_events(session:Session= Depends(get_session)):
    # buunch of item in table 
    query=select(EventModel).order_by(EventModel.id.desc()).limit(1000)
    result=session.exec(query).all()
    print(result)
    return {
        "result":result,
        "count":len(result)
    }



#  GET api/events/12 b
@router.get("/{event_id}" , response_model=EventModel)
# single items 
def get_events(event_id:int , session:Session= Depends(get_session)):
    query=select(EventModel).where(EventModel.id==event_id)
    result=session.exec(query).first()
    if not result:
        raise HTTPException(status_code=404 , detail="not found")
    return result


# POST method  create

@router.post("/", response_model=EventModel)
def create_event(
    payload: Eventcreateschema, session: Session = Depends(get_session)
):
    data = payload.model_dump()   # dict from schema
    obj = EventModel(**data)      # ✅ build ORM object
    session.add(obj)
    session.commit()              # ✅ no argument here
    session.refresh(obj)
    return obj


#  PUT api/events/12
@router.put("/{event_id}" , response_model=EventModel) 
def update_event(event_id:int , payload:Eventupdateschema , session:Session= Depends(get_session) )->EventModel:
    print(payload)
    query=select(EventModel).where(EventModel.id==event_id)
    obj=session.exec(query).first()
    if not obj:
        raise HTTPException(status_code=404 , detail="not found")
    data=payload.model_dump()
    for k, v in data.items():
        if k==id:
            continue
        setattr(obj , k , v)
    obj.updated_at=get_utc_now()        
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj




#  delete api/events/12
from fastapi import HTTPException

@router.delete("/{event_id}", response_model=EventModel)
def delete_event(event_id: int, session: Session = Depends(get_session)):
    query = select(EventModel).where(EventModel.id == event_id)
    data = session.exec(query).first()
    
    if not data:
        raise HTTPException(status_code=404, detail="Event not found")
    
    session.delete(data)
    session.commit()
    return data


