from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DB = 'sqlite:///./events.db'

engine = create_engine(URL_DB)

SessionLocal = sessionmaker(autocommit=False, autoflush= False,bind= engine)

Base = declarative_base()


# , connect_args={''}