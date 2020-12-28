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
cid = 'ki'
sql.execute(f"select distinct k.AMOUNT, k.CASHFLOW_ID, s.TAX, k.DATE_TIME, k.TAX_PAYED, k.ID from keep_in_book k, client c, source_of_cashflow s where k.amount>0 AND k.CASHFLOW_ID = s.CASHFLOW_ID AND c.BOOK_NO = k.BOOK_NO AND c.CLIENT_ID = '{cid}' ORDER BY k.DATE_TIME DESC")
cashflows = sql.fetchall()
# print(len(cashflows))
for cashflow in cashflows:
    print(cashflow)
    # print(f'{cashflow[3].strftime("%d-%m-%Y %H:%M")}')

# sql("INSERT INTO client ()")
# class first(App):
#     def build(self):
#         return Label(text = "hi")
#
# if __name__ == '__main__':
#     first().run()
