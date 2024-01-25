from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
) 

# Link python file to Chinook database using create_engine component. 
db = create_engine("postgresql:///chinook") # create variable db and tell it to point to postgresql db called chinook. 
# three slashes means database is hosted locally within workspace environment. 

meta = MetaData(db) # Use the MetaData class and save to variabe meta. Data about and within tables.

# connect to the database, using the .connect() method, and the Python with-statement.
# saves connection to database in the connection variable. 
with db.connect() as connection:  
