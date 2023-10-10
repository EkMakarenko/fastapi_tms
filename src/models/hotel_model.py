from sqlalchemy import Column, String, Integer, Boolean, Float

from src.models.abstract_model import AbstractModel


class Hotel(AbstractModel):
    __tablename__ = 'hotels'

    name = Column('name', String, nullable=False)
    country = Column('country', String, nullable=False)
    city = Column('city', String, nullable=False)
    street = Column('street', String, nullable=False)
    house_number = Column('house_number', Integer, nullable=False)
    longitude = Column('longitude', Float, nullable=True)
    latitude = Column('latitude', Float, nullable=True)