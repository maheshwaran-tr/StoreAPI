from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

uri = f"mongodb+srv://{username}:{password}@cluster0.awznyyb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.store

product_collection = db.get_collection("prodcuts")
user_collection = db.get_collection("users")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)