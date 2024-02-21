from pymongo import MongoClient

def init():
    client = MongoClient("mongodb://root:example@localhost:27017")
    database = client.testdb

    try: database.command("serverStatus")
    except Exception as e: print(e)
    else: print("You are connected!")

    client.close()
