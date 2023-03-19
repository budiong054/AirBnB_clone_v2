#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = ""
    name = Column(string(128), nullable=False)
    state_id = Column(string(60), Foreignkey('state.id'),
                       nullable=False)
    places = relationship("Place", cascade="delete", backref='cities')  
