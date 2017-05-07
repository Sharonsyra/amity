import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Sequence
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

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.first_name, self.last_name, self.password)

class Room(Base):
    __tablename__ = 'room'
    id = Column(Integer(10), Sequence('room_id'), primary_key=True)
    room_name = Column(String(30), nullable=False)
    room_capacity = Column(Integer(10), nullable=False)
    room_type = Column(String(20), nullable=False)
    member1 = Column(String(30), ForeignKey('person.id'))
    member2 = Column(String(30), ForeignKey('person.id'))
    member3 = Column(String(30), ForeignKey('person.id'))
    member4 = Column(String(30), ForeignKey('person.id'))
    member5 = Column(String(30), ForeignKey('person.id'))
    member6 = Column(String(30), ForeignKey('person.id'))

    def __repr__(self):
        if self.room_type.lower() == 'office':
            return """<Room(room name='%s', member1='%s',
            member2='%s', member3='%s', member4='%s',
            member5='%s', member6='%s')>""" % (self.room_name,
                                               self.member1,
                                               self.member2,
                                               self.member3,
                                               self.member4,
                                               self.member5,
                                               self.member6)

        elif self.room_type.lower() == "living_space":
            return """<Room(room name='%s',
             member1='%s',member2='%s',
              member3='%s', member4='%s')>""" % (self.room_name,
                                                 self.member1,
                                                 self.member2,
                                                 self.member3,
                                                 self.member4)

# end of file code
engine = create_engine('sqlite:///userideas.db')
Base.metadata.create_all(engine)
