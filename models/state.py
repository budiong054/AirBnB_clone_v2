#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.orm import relationship
import models
from models.city import City
import os


class State(BaseModel):
    """ State class """
    __tablename__ = 'state'
    name = Column(String(128), nullable=false)
    cities = relationship("city", cascade="delete", backref="state")

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            """cities getter attribute"""
        cit_lis = []
        all_cit = models.storage.all(city)
        for city in all_cit.values():
            if city.state_id == self.id:
                cit_lis.append(city)
        return cit_lis
