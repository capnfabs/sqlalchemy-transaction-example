from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Zebra(Base):
    __tablename__ = 'zebras'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    when_born = Column(DateTime, nullable=False)
    when_stripes_counted = Column(DateTime)
    number_of_stripes = Column(Integer)