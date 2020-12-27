# import re
# import datetime
# print(datetime.datetime.now().strftime("%H:%M"))
# import FILE
# with open('README.txt', encoding="utf8") as file:
#     long_description = file.read()
with open('C:\\Users\\anshs\\Desktop\\study\\5th_sem\\EE\\CIE1\\1RV18CS026-18G5B18-1.pdf', 'rb') as file:
    data = file.read()

with open('C:\\Users\\anshs\\Desktop\\EE_CIE1.pdf', 'wb') as file:
    file.write(data)
# pattern = re.compile("^[0-9]:[0-9]")
# print(pattern.match(string))
