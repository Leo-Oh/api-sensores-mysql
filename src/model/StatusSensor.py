from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from src.db.DB import engine, meta_data


status_sensors = Table('status', meta_data,
    Column('topic',String(200), primary_key=True),
    Column('status', Integer, nullable=False),

)

meta_data.bind = engine
meta_data.create_all()