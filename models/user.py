#!/usr/bin/python3
'''
    Implementation of the User class which inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    '''
        Definition of the User class
    '''
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
