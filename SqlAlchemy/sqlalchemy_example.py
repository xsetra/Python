# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_declarative import Base, User, Address

engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

new_user = User(username='Test', password='123')
session.add(new_user)
session.commit()
