import re
string = '23/11/1999'
# pattern = re.compile("^[0-9]:[0-9]")
# print(pattern.match(string))
if re.match(r"^[0-3][0-9]/[0-1][0-9]/[0-2][0-9][0-9][0-9]", string):
    print("yoyo")
