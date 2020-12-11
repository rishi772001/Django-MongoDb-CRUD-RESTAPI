import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Database Name
db = client["student"]