# coding=utf-8

from fastapi import APIRouter, Response, Header
from fastapi.responses import JSONResponse 
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from src.schema.StatusSensor import StatusSensor
from src.db.DB import engine
from src.model.StatusSensor import status_sensors
from typing import List
from datetime import datetime

statusSensor = APIRouter()


@statusSensor.get("/status", response_model=List[StatusSensor])
def get_all_status():
  with engine.connect() as conn:
    result = conn.execute(status_sensors.select()).fetchall() 
    return result

@statusSensor.get("/status/{where_is}/{sensor}/{place}", response_model=StatusSensor)
def get_status_by_topic(where_is:str,sensor:str,place:str):
  with engine.connect() as conn:
    topic_consult = '{}/{}/{}'.format(where_is,sensor,place) 
    print(topic_consult)
    result = conn.execute(status_sensors.select().where(status_sensors.c.topic == str(topic_consult))).first()
    return result

@statusSensor.get("/status/{where_is}/{sensor}/{place}", response_model=StatusSensor)
def get_status_by_topic(where_is:str,sensor:str,place:str):
  with engine.connect() as conn:
    topic_consult = '{}/{}/{}'.format(where_is,sensor,place) 
    print(topic_consult)
    result = conn.execute(status_sensors.select().where(status_sensors.c.topic == str(topic_consult))).first()
    return result

@statusSensor.post("/status", status_code=HTTP_201_CREATED)
def create_status(data_status: StatusSensor):
  with engine.connect() as conn:
    try:
      new_status = data_status.dict()
      conn.execute(status_sensors.insert().values(new_status))
      return Response(status_code=HTTP_201_CREATED)
    except:
      return Response(status_code=HTTP_401_UNAUTHORIZED)


  
@statusSensor.put("/status/{where_is}/{sensor}/{place}", response_model=StatusSensor)
def update_status_by_topic(data_update: StatusSensor, where_is:str,sensor:str,place:str):
  with engine.connect() as conn:
    topic = '{}/{}/{}'.format(where_is,sensor,place)
    conn.execute(status_sensors.update().values(
        status = data_update.status,
      ).where(status_sensors.c.topic == topic))

    result = conn.execute(status_sensors.select().where(status_sensors.c.topic == topic)).first()
    return result



@statusSensor.delete("/status/{where_is}/{sensor}/{place}", status_code=HTTP_204_NO_CONTENT)
def delete_status_by_topic(where_is:str,sensor:str,place:str):
  with engine.connect() as conn:
    topic = '{}/{}/{}'.format(where_is,sensor,place)
    conn.execute(status_sensors.delete().where(status_sensors.c.topic == topic))

    return Response(status_code=HTTP_204_NO_CONTENT)