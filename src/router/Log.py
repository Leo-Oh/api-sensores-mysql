from fastapi import APIRouter, Response, Header
from fastapi.responses import JSONResponse 
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from src.schema.Log import Log
from src.db.DB import engine
from src.model.Log import log_model
from typing import List
from datetime import datetime

log = APIRouter()


@log.get("/logs", response_model=List[Log])
def get_logs():
  with engine.connect() as conn:
    result = conn.execute(log_model.select()).fetchall() 
    return result

@log.get("/logs/{where_is}/{sensor}/{place}", response_model=List[Log])
def get_logs_by_topic(where_is:str,sensor:str,place:str):
  with engine.connect() as conn:
    topic = '{}/{}/{}'.format(where_is,sensor,place) 
    result = conn.execute(log_model.select().where(log_model.c.topic == topic)).fetchall() 
    return result

@log.get("/log/{id}", response_model=Log)
def get_log(id: int):
  with engine.connect() as conn:
    result = conn.execute(log_model.select().where(log_model.c.id == id)).first()
  return result


@log.post("/log", status_code=HTTP_201_CREATED)
def create_log(data_log: Log):
  with engine.connect() as conn:
    new_log = data_log.dict()

    conn.execute(log_model.insert().values(new_log))

    return Response(status_code=HTTP_201_CREATED)


@log.delete("/log/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_log(id: int):
  with engine.connect() as conn:
    conn.execute(log_model.delete().where(log_model.c.id == id))

    return Response(status_code=HTTP_204_NO_CONTENT)