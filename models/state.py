#!/usr/bin/python3
'''
    Implementation of the State class
'''
from sqlalchemy import Column, String,
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
    '''
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='State',
                              cascade='all, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            '''Getter for cities'''
            list_cities = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
