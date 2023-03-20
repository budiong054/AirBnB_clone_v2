#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False,
                              default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False,
                            default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    # amenity_ids = []
    # for caution and was added in Task 9
    reviews = relationship("Review", cascade="delete", backref="place")
    amenities = relationship("Amenity", secondary='place_amenity',
                             back_populates="place_amenities", viewonly=False)

    @property
    def reviews(self):
        """ reviews method """
        dict_reviews = models.storage.all(Review)
        list_reviews = []
        for rev in dict_reviews.values():
            if rev.place_id == self.id:
                list_reviews.append(rev)
        return list_reviews

    @property
    def amenities(self):
        """ getter attribute amenitites that returns the list of...
            ...Amenity instances """
        list_obj = []
        amen_objs = models.storage.all(Amenity)
        for am in amen_objs.values():
            if amenity.id in amenity_ids:
                list_obj.append(amenity)
        return list_obj

    @amenities.setter
    def amenitites(self, obj):
        """ setter attribute amenities that handles append method for adding...
            ...an Amenity.id to the attribute amenity_ids """
        if isinstance(obj, Amenity):
            if self.id == obj.place_id:
                self.amenity_ids.append(obj.id)
