from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('men_id', Integer, ForeignKey('men.id')),
    Column('women_id', Integer, ForeignKey('women.id'))
)

class Boys(Base):
    __tablename__ = 'men'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    girls = relationship(
        "Girls",
        secondary=association_table,
        back_populates="boys")

class Girls(Base):
    __tablename__ = 'women'
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    boys = relationship(
        "Boys",
        secondary=association_table,
        back_populates="girls")

engine = create_engine('mysql+pymysql://root@localhost:3306/testMtoM')
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
