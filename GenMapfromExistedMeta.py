from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
from sqlalchemy.ext.automap import automap_base
engine = create_engine("mysql+pymysql://root@localhost:3306/test1toM")

# produce our own MetaData object
metadata = MetaData()

# we can reflect it ourselves from a database, using options
# such as 'only' to limit what tables we look at...
metadata.reflect(engine, only=['user', 'address'])

# ... or just define our own Table objects with it (or combine both)
Table('user_order', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', ForeignKey('user.id'))
            )

# we can then produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)

# calling prepare() just sets up mapped classes and relationships.
Base.prepare()

# mapped classes are ready
User, Address, Order = Base.classes.user, Base.classes.address,\
    Base.classes.user_order
