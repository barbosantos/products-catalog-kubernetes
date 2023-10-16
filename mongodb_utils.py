from pymongo import MongoClient

# TODO: Get local credentials from .env file
connection_string = ""
client = MongoClient(connection_string)

# List the database names
database_names = client.list_database_names()

for db_name in database_names:
    print(db_name)