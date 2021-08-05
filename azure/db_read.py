from pymongo import MongoClient

db_client=MongoClient('127.0.0.1',27017)
db=db_client['nitw']
c=db['dht11']

for i in c.find():
        print(i)
