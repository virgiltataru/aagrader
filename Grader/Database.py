from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
client = MongoClient("mongodb://localhost/database")
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
