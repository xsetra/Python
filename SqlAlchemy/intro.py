# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


class Address(Base):
    __tablename__ = 'adresses'

    id = Column(Integer, primary_key=True)
    street_name = Column(String(100))
    street_number = Column(Integer)
    person_id = Column(Integer, ForeignKey('people.id'))
    person = relationship(Person)

engine = create_engine('sqlite:///')
Base.metadata.create_all(engine)
