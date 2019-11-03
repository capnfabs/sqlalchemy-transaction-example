from sqlalchemy import Column, String, DateTime, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Zebra(Base):
    __tablename__ = 'zebras'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    when_born = Column(DateTime, nullable=False)
    when_stripes_counted = Column(DateTime)
    number_of_stripes = Column(Integer)

    def __repr__(self):
        return f"Zebra(name='{self.name}')"


class WateringHole(Base):
    __tablename__ = 'watering_holes'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Numeric(precision=6), nullable=False)
    longitude = Column(Numeric(precision=6), nullable=False)
