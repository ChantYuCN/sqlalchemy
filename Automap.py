from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("mysql+pymysql://root@localhost:3306/test1to1")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Parent = Base.classes.parent
Child = Base.classes.child

session = Session(engine)

# rudimentary relationships are produced
session.add(Child(name="annyu", parent=Parent(name="fatw")))
session.commit()

# collection-based relationships are by default named
# "<classname>_collection"
#print (u1.address_collection)
