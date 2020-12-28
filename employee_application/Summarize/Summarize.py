import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()

class summarize_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen
        app.summarize_object.update()

class summarize(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3
        self.cols = 2

        self.total_asset_label = Label()
        self.add_widget(self.total_asset_label)

        self.total_liability_label = Label()
        self.add_widget(self.total_liability_label)

        self.unpaid_tax_label = Label()
        self.add_widget(self.unpaid_tax_label)

        # sql.execute("select sum(AMOUNT) from asset")
        # total_asset = sql.fetchone()
        self.net_asset_label = Label()
        self.add_widget(self.net_asset_label)

        self.back = Button(text = "Back")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

    def back_pressed(self, instance):
        app.screenmanager.current = 'main_menu_screen'

    def update(self):

        sql.execute(f"select sum(asset.AMOUNT) from asset, client, keep_in_book where asset.ID = keep_in_book.ID AND client.BOOK_NO = keep_in_book.BOOK_NO AND client.CLIENT_ID = '{cid}'")
        total_asset = sql.fetchone()
        self.total_asset_label.text = "Total Assets: "+str(total_asset[0])
        print(total_asset)

        sql.execute(f"select sum(liability.AMOUNT) from liability, client, keep_in_book where liability.ID = keep_in_book.ID AND client.BOOK_NO = keep_in_book.BOOK_NO AND client.CLIENT_ID = '{cid}'")
        total_liability = sql.fetchone()
        self.total_liability_label.text = "Total Liability: "+str(total_liability[0])
        print(self.total_liability_label.text)

        # sql.execute(f"select sum(ABS(AMOUNT*TAX/100)) from revenue r, keep_in_book k, client c where r.ID = k.ID AND s.BOOK_NO = k.BOOK_NO AND r.TAX_PAYED = '0' AND k.C_ID = '{cid}'")
        # revenue_unpaid_tax = sql.fetchone()[0]
        # sql.execute(f"select sum(ABS(AMOUNT*TAX/100)) from expense r, keep_in_book k, client c where r.ID = k.ID AND s.BOOK_NO = k.BOOK_NO AND r.TAX_PAYED = '0' AND k.C_ID = '{cid}'")
        sql.execute(f"select sum(ABS(k.AMOUNT*s.TAX/100)) from source_of_cashflow s, keep_in_book k, client c where k.BOOK_NO = c.BOOK_NO AND k.CASHFLOW_ID = s.CASHFLOW_ID AND k.TAX_PAYED = '0' AND c.CLIENT_ID = '{cid}'")
        unpaid_tax = sql.fetchone()[0]
        self.unpaid_tax_label.text = "Total Unpaid Tax: "+str(unpaid_tax)
        print(self.unpaid_tax_label.text)

        self.net_asset_label.text = "Net Assets: "+str(total_asset[0]-total_liability[0])
        print(self.net_asset_label.text)
