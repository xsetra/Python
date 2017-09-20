# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from intro import Base, Person, Address

engine = create_engine('sqlite:///:memory:')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

new_person = Person(name='new_person')
session.add(new_person)
session.commit()
