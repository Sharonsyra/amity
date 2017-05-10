import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, Sequence('person_id'), primary_key=True)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    person_type = Column(String(20), nullable=False)
    wants_accommodation = Column(String(10), nullable=True)
    allocated = Column(Boolean, unique=True, default=False)


class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer, Sequence('person_id'), primary_key=True)
    room_name = Column(String(30), nullable=False)
    room_capacity = Column(Integer, nullable=False)
    room_type = Column(String(20), nullable=False)
    members = Column(String(), nullable=True)

class Waiting_type(Base):
    __tab

# end of file code
engine = create_engine('sqlite:///userideas.db')
Base.metadata.create_all(engine)
