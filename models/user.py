#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Foreignkey
from sqlalchemy.orm import relationship



class User(BaseModel):
    """This class defines a user by various attributes"""
    __tablename__ = 'user'
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=False)
    last_name = Column('first_name', String(128), nullable=False)
    #this was implemented in task 8
    places = relationship("place", cascade="delete", backref="user")
    #for caution
    revives = relationship("review", cascade="delete", backref="user")
