# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
eid = "binod"
sql.execute("SELECT * FROM client WHERE E_ID = '{%s}'", (eid))
result = sql.fetchall()
for row in result:
    print(row)

# sql("INSERT INTO client ()")
# class first(App):
#     def build(self):
#         return Label(text = "hi")
#
# if __name__ == '__main__':
#     first().run()
