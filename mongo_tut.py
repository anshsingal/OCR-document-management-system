import pymongo
from pymongo import MongoClient
from bson import ObjectId
import sys
import re
client = MongoClient('localhost', 27017)
print(client)
db = client['accounts']
# print(db)
# collection = db['try']
# result = (db['try'].insert_one({'name': 'kya', 'surname': 're'})).inserted_id
# print(result)
# final = str(result)
# print("size of final: ", sys.getsizeof(final))
# new MongoID(result)

# recv = db['try'].find_one({'_id':ObjectId(final)})
string = "DIFFERENCE"
pat = re.compile(rf'{string}', re.I)
results = db.files.find({ "text": {'$regex': pat}})
print(results.count())
# for result in results:
#     print(type(str(result['_id'])))
#     print(result['_id'])
