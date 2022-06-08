from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker



engine = create_engine('mysql+pymysql://root:password@34.94.79.113:9098/sensors')
#engine = create_engine('mysql+pymysql://root:password@127.0.0.1:9098/sensors')


conn = engine.connect()
Session = sessionmaker(bind=engine)

session = Session()
meta_data = MetaData()
