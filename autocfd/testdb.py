"""Just some testing."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from base import Base
import flotables
import basetables


engine = create_engine('sqlite:///my_test_db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()


# Create table
Base.metadata.create_all(engine)

myblade = basetables.Blade()
myairfoil = basetables.Airfoil(airfoil_name='jfoil')
airfoil2 = basetables.Airfoil(airfoil_name='bfoil')

myblade.airfoils.append(myairfoil)
myblade.airfoils.append(airfoil2)

session.add(myblade)
session.commit()
