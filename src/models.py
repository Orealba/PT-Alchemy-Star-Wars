import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
  __tablename__ = 'user'
  ID = Column(Integer, primary_key=True)
  nombre = Column(String(250), nullable=False)
  email = Column(String(250), nullable=False)
  password= Column(String(250), nullable=False)
  
  
class Favoritos_PL(Base):
    __tablename__ = 'favoritos_PL'
    IdFav = Column(Integer, primary_key=True)
    id_user = Column(Integer,ForeignKey("user.id"))
    id_pl = Column(Integer,ForeignKey("planetas.id"))
    user = relationship ('user')
    Favoritos_PL= relationship ('favoritos_PL')


class Planetas(Base):
  __tablename__= 'planetas'
  ID = Column(Integer, primary_key=True)
  nombre =Column(String(250), nullable=False)
  population = Column(String(250), nullable=False)
  gravity= Column(String(250), nullable=False)
  Favoritos_PL= relationship ('id_pl')

class Favoritos_Pj (Base):
  __tablename__= 'favoritos_Pj'
  IdFav = Column(Integer, primary_key=True)
  id_user = Column(Integer,ForeignKey("user.id"))
  id_pj = Column(Integer,ForeignKey("personajes.id"))


class Personajes (Base):
    __tablename__= 'personajes'
    ID = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    estatura = Column(Integer)
    colorOjos = Column(String(250), nullable=False)
    favoritos_Pj= relationship ('favoritos_Pj')

  


# class Person(Base):
#    __tablename__ = 'person'
# Notice that each column is also a normal Python instance attribute.
# Here we define columns for the table person
# id = Column(Integer, primary_key=True)
#name = Column(String(250), nullable=False)
#last_name = Column(String(250), nullable=False)

#class Address(Base):
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
  #  id = Column(Integer, primary_key=True)
 #   __tablename__ = 'address'
   # street_name = Column(String(250))
    #street_number = Column(String(250))
    #post_code = Column(String(250), nullable=False)
    #person_id = Column(Integer, ForeignKey('person.id'))
    #person = relationship(Person)

    #def to_dict(self):
     #   return {}

## Draw from SQLAlchemy base
try:
  result = render_er(Base, 'diagram.png')
  print("Success! Check the diagram.png file")
except Exception as e:
  print("There was a problem genering the diagram")
  raise e