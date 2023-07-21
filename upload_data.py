from pymongo.mongo_client import MongoClient
import pandas as pd
import json
#from src.constant import *

# Uniform Resource identifier
uri = "mongodb+srv://Shehryar:Shehryar@cluster0.b5jva7x.mongodb.net/?retryWrites=true&w=majority"

import os
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'venv/Lib/site-packages/certifi/cacert.pem')

import certifi
client =MongoClient(f"mongodb+srv://Shehryar:Shehryar@cluster0.b5jva7x.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
# Create a new client and connect to the server
#client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    

# create database name and collection name
MONGO_DATABASE_NAME = "GondalDB"
MONGO_COLLECTION_NAME = "Cement"

# read the data as a dataframe
df=pd.read_csv(r"D:\JupyterNotebook\PW_Skills_Data_Science\Machine_learning\Machine_learning_projects\cement-strength-prediction-project\notebook\cement_data.csv")

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_record)
