import sqlmodel
from sqlmodel import SQLModel, Session
from .config import DATABASE_URL, DB_TIMEZONE
import timescaledb

if DATABASE_URL== "":
    raise NotImplementedError("Database url need to set")

# engine=sqlmodel.create_engine(url=DATABASE_URL)
engine=timescaledb.create_engine(url=DATABASE_URL , timezone=DB_TIMEZONE)

def initdb():
    print("creating database")
    SQLModel.metadata.create_all(engine)
    print("creating hyper tables")
    timescaledb.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session