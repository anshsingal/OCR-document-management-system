# import re
# import datetime
# print(datetime.datetime.now().strftime("%H:%M"))
# import FILE
# with open('README.txt', encoding="utf8") as file:
#     long_description = file.read()
import re
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
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
string = 'canon'
pat = re.compile(rf'{string}', re.I)
results = db.files.find({ "text": {'$regex': pat}})


# for result in results:
    # print(str(cashflow['_id']))
    # print(result['_id'])
    # sql.execute(f"select distinct k.AMOUNT, k.CASHFLOW_ID, s.TAX, k.DATE_TIME, k.TAX_PAYED, k.ID from keep_in_book k, source_of_cashflow s where k.amount>0 AND k.CASHFLOW_ID = s.CASHFLOW_ID AND k.ID = '{str(result['_id'])}'")
    # cashflow = sql.fetchone()
    # print(cashflow)


sql.execute(f"select * from keep_in_book k, source_of_cashflow s where k.amount>0 AND k.CASHFLOW_ID = s.CASHFLOW_ID AND k.ID = '{str(result['_id'])}'")
cashflow = sql.fetchone()



# else:
#     print("NOPE")
# with open('C:\\Users\\anshs\\Desktop\\DOCUMENT.png', 'wb') as file:
#     file.write(file_data)
#
# with open('C:\\Users\\anshs\\Desktop\\EE_CIE1.pdf', 'wb') as file:
#     file.write(data)
# pattern = re.compile("^[0-9]:[0-9]")
# print(pattern.match(string))
