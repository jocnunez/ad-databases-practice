
# Get environment variables and initialize db connection
from dotenv import dotenv_values
from pymongo import MongoClient

ENV = dotenv_values()

user = ENV["USER"]
password = ENV["PASSWORD"]
host = ENV["HOST"]
port = ENV["PORT"]

client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}")
db = client.testdb

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
