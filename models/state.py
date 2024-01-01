#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')
    if (HBNB_TYPE_STORAGE == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """getter for list of city instances related to the state"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
