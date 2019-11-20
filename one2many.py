from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Man(Base):
    __tablename__ = 'man'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    pet = relationship("Pets", back_populates="man")

class Pets(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name=Column(String(25))
    parent_id = Column(Integer, ForeignKey('man.id'))
    man = relationship("Man", back_populates="pet")

engine = create_engine('mysql+pymysql://root@localhost:3306/test1toM')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
