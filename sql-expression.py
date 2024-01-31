from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
) 

# Link python file to Chinook database using create_engine component. 
db = create_engine("postgresql:///chinook") # create variable db and tell it to point to postgresql db called chinook. 
# three slashes means database is hosted locally within workspace environment. 

meta = MetaData(db) # Use the MetaData class and save to variabe meta. Data about and within tables.

# connect to the database, using the .connect() method, and the Python with-statement.
# saves connection to database in the connection variable.
# Before start working with data need to create a schema for our tables so Python knows what we're working with.  
# Creating the schema can also be known as data models. 

# Create Variables for each table: 

# create variable for "Artist" table
# Our first table class, or model, will be for the Artist table
# which I'll assign to the variable of 'artist_table'.
# Using the Table import, we need to specify the name of our table, and provide the meta schema.
# Need to provide a breakdown of all the columns in the table. 

# Back within our file, the format when defining columns, is the column name, followed by the
# type of data presented (integer, string, float), and then any other optional fields after that.
# In our case, we have a column for "ArtistId", which is an Integer, and for this one, we
# can specify that primary_key is set to True.
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True), # this is the header of the column interrogating
    Column("Name", String)
)

# create variable for album table

album_table = Table(
    "Album", meta, 
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

track_table = table(
    "Track", meta, 
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", String),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# make the connection (almost like functions)
with db.connect() as connection:  

    
    # Use select() method and execute() method - these are using the expression language. 
    # Define all six queries into a variable called select_query - will comment out each time. 

    # Select all records from Artist table - use select() method
    select_query = artist_table.select()

    # Store the query results into a variable called results
    results = connection.execute(select_query)
    for result in results:
        print(result)


# execute using for loop:
    results = connection.execute(select_query)
    for result in results:
        print(result)
