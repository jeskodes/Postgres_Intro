# Need to import items from SQLAlchemy 
# Don't need to import Table or metadata as won't be creating table classes will be creating python classes. 

from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook") # Using postgres server on a local host (three slashes = localhost)
base = declarative_base() # variable called base - grabs metadata from database then hands it back in a sub-class. 

# Create a class-based model for the "Programmer" table.  This is the table schema. 
class Programmer(base): 
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True) #The primary key is id and it will auto increment as add more to it
    # e.g. first item = ID 1, second ID 2. 

# The remaining 5 columns will be strings. 
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db) # using creeate_all() method. 

# Create records on table. 
# Record #1 
ada_lovelace = Programmer (
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "Female",
    nationality = "British",
    famous_for = "First Programmer"
)

# Add each programmer to the table
session.add(ada_lovelace)

# Commit to the table
session.commit()