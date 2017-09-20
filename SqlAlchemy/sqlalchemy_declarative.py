# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(70), nullable=False)
    password = Column(String(128), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street = Column(String(200), nullable=False)
    city = Column(String(50), nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
