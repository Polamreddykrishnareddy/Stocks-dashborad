import pymongo as 
import pandas as pd
db_name="Stocks"
def mongodb_connection(collection_name):
    client=pm.MongoClient("mongodb://localhost:27017")
    database=client[db_name]
    collection=database[collection_name].find()
    df=pd.DataFrame(list(collection))
    return df 
