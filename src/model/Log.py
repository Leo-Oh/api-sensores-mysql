from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Time, Float
from src.db.DB import engine, meta_data


log_model = Table('log', meta_data,
    Column('id', Integer, primary_key=True),
    Column('topic',String(200), nullable=False),
    Column('value',Float, nullable=False),
    Column('date', Date, nullable=False),
    Column('time', Time, nullable=False),
)


meta_data.bind = engine
meta_data.create_all()