# import kivy
# from kivy.app import App
# from kivy.uix.label import Label
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
# eid = 'a'
# sql.execute(f"SELECT * FROM client WHERE E_ID = '{eid}'")
# clients = sql.fetchall()
# for client in clients:
#     print(client)
cid = 'sos'
sql.execute(f"select AMOUNT from liability, client where liability.BOOK_NO = client.BOOK_NO AND client.CLIENT_ID = '{cid}'")
cashflows = sql.fetchone()
print(cashflows)

# sql("INSERT INTO client ()")
# class first(App):
#     def build(self):
#         return Label(text = "hi")
#
# if __name__ == '__main__':
#     first().run()
