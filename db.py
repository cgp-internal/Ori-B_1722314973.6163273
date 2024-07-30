from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_config import DB_PATH

engine = create_engine(DB_PATH)
Session = sessionmaker(bind=engine)

def db_session():
    return Session()