## need pip install sqlalchemy-multidb 

from sqlalchemy_multidb import DatabaseManager
from one2many import Man
from one2one import Parent


db = DatabaseManager()
db.add_database('test1to1','mysql+pymysql://root@localhost:3306/test1to1')
db.add_database('test1toM','mysql+pymysql://root@localhost:3306/test1toM')

with db.session('test1toM') as s1:
    h1 = s1.query(Man).filter(Man.id==1).one()

with db.session('test1to1') as s2:
    h2 = s2.query(Parent).filter(Parent.id==1).one()
