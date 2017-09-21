# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(Department, backref=backref('employees', uselist=True))

engine = create_engine('sqlite:///')
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = DBSession()

john = Employee(name='john')
it_department = Department(name='IT')
john.department=(it_department)

session.add(john)
session.add(it_department)
session.commit()

