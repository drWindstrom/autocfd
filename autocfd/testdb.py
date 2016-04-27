"""Just some testing."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import blade
import airfoil
import flosim
import flosolver


engine = create_engine('sqlite:///my_test_db.sqlite3')
Session = sessionmaker(bind=engine)
session = Session()


# Create table
Base.metadata.create_all(engine)

myblade = blade.Blade()
myairfoil = airfoil.Airfoil(airfoil_name='jfoil')
airfoil2 = airfoil.Airfoil(airfoil_name='bfoil')

myblade.airfoils.append(myairfoil)
myblade.airfoils.append(airfoil2)

session.add(myblade)
session.commit()
