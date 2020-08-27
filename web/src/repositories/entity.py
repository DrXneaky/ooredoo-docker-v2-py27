
from sqlalchemy import create_engine, Column, Integer, Sequence, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import src.entities

from config import Config

""" db_url = 'localhost:5432'
db_name = 'db_app'
db_user = 'postgres'
db_password = 'root' """

db_url = Config.DB_URL
db_name = Config.DB_NAME
db_user = Config.DB_USER
db_password = Config.DB_PASSWD

#engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')
engine = create_engine('postgresql://{0}:{1}@{2}/{3}'.format(db_user,db_password, db_url, db_name))

Session = sessionmaker(bind=engine, autocommit=False)
Base = declarative_base()
Metadata = MetaData()

class Entity():
    id = Column(Integer, primary_key=True)

def init_db():
    Base.metadata.create_all(engine)

def shutdown_db_session():
    print("app closed")