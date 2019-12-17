#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base, Column, String, ForeignKey
from sqlalchemy import Float, Integer
from sqlalchemy.orm import relationship
from models.city import City
from models.user import User


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(City.id))
    user_id = Column(String(60), ForeignKey(User.id))
    name = Column(String(128))
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", "place")

    @property
    def reviews(self):
        """returns a list of reviews with same place_id"""
        ret = []
        for k, v in storage.all().keys():
            if k.split(".")[0] == "Review":
                if v.place_id == self.id:
                    ret.append(v)
        return ret
