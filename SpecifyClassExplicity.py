from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine

# automap base
Base = automap_base()

# pre-declare User for the 'user' table
class User(Base):
    __tablename__ = 'user'

    # override schema elements like Columns
    user_name = Column('name', String)

    # override relationships too, if desired.
    # we must use the same name that automap would use for the
    # relationship, and also must refer to the class name that automap will
    # generate for "address"
    address_collection = relationship("address", collection_class=set)

# reflect
engine = create_engine("sqlite:///mydatabase.db")
Base.prepare(engine, reflect=True)

# we still have Address generated from the tablename "address",
# but User is the same as Base.classes.User now

Address = Base.classes.address

u1 = session.query(User).first()
print (u1.address_collection)

# the backref is still there:
a1 = session.query(Address).first()
print (a1.user)