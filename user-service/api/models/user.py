from datetime import datetime

from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    mno = Column(Integer, primary_key=True,
                 autoincrement=True, index=True)
    userid = Column(String(18), nullable=False)
    passwd = Column(String(128), nullable=False)
    name = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    #regdate = Column(DateTime, default=datetime.now)
    #regdate = Column(String(20), default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    regdate = Column(String(20))








