# import re
# import datetime
# print(datetime.datetime.now().strftime("%H:%M"))
# import FILE
# with open('README.txt', encoding="utf8") as file:
#     long_description = file.read()
import pymongo
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('localhost', 27017)
db = client['accounts']


# with open('C:\\Users\\anshs\\Desktop\\study\\5th_sem\\EE\\CIE1\\1RV18CS026-18G5B18-1.pdf', 'rb') as file:
#     file_data = file.read()
#
#
# print((db['try'].insert_one({'file_data': file_data})).inserted_id)
id = '5fe95e1e3a3b4744d7cd826f'
doc = db['files'].find_one({'_id':ObjectId(id)})
print(doc['extension'])
# with open('C:\\Users\\anshs\\Desktop\\DOCUMENT.png', 'wb') as file:
#     file.write(file_data)
#
# with open('C:\\Users\\anshs\\Desktop\\EE_CIE1.pdf', 'wb') as file:
#     file.write(data)
# pattern = re.compile("^[0-9]:[0-9]")
# print(pattern.match(string))
