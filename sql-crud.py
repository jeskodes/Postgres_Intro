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

# Create a class-based model for the "Programmer" table
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

# creating records on our Progammer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
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

another_one = Programmer(
    first_name="First Name",
    last_name="Last Name",
    gender="F",
    nationality="British",
    famous_for="Stuff"
)
# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(another_one)




# Update a single record - create variable programmer and 
# set to normal session query on programmer table
# query the database to find all Programmers
# use id and primary key of record to update
# primary key should be 7 but do not yet know how to reset primary keys when delete records
# use .first() method so don't have to use for loop to iterate over all records first. 
programmer = session.query(Programmer).filter_by(id=16).first()
programmer.famous_for = "Other Stuff"

# commit our session to the database
# session.commit()

# Update multiple records using for loop and else/if statement

people = session.query(Programmer)
for person in people:
    if person.gender == "F":
        person.gender = "Female"
    elif person.gender == "M":
        person.gender = "Male"
    else:
        print("Gender not defined")
    session.commit()



programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )