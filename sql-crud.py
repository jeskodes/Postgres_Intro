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

# Record #2 
alan_turing = Programmer (
    first_name = "Alan",
    last_name = "Turing",
    gender = "Male",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)
# Add each programmer to the table
# session.add(ada_lovelace) Need to comment out session already added or will add again.
# session.add(alan_turing)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_berners_lee)

# Commit to the table
session.commit()

# query the database to find all Programmers
programmers = session.query(Programmer)
for programmer in programmers: 
    print(
        programmer.id, 
        programmer.first_name + " " + programmer.last_name, 
        programmer.gender, 
        programmer.nationality, 
        programmer.famous_for, 
        sep=" | " # separate all these with a pipe
    )