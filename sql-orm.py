# Need to import items from SQLAlchemy 
# Don't need to import Table or metadata as won't be creating table classes will be creating python classes. 

from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook") # Using postgres server on a local host (three slashes = localhost)
base = declarative_base() # variable called base - grabs metadata from database then hands it back in a sub-class. 

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()