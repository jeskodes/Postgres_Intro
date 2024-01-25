from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
) 

# Link python file to Chinook database using create_engine component. 
db = create_engine("postgresql:///chinook") # create variable db and tell it to point to postgresql db called chinook. 
