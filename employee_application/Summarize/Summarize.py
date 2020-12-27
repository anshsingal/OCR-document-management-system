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

        self.total_unpaid_tax_label = Label()
        self.add_widget(self.total_unpaid_tax_label)

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

        sql.execute(f"select sum(AMOUNT) from asset, client where asset.BOOK_NO = client.BOOK_NO AND client.CLIENT_ID = '{cid}'")
        total_asset = sql.fetchone()
        self.total_asset_label.text = "Total Assets: "+str(total_asset[0])
        print(total_asset)

        sql.execute(f"select sum(AMOUNT) from liability, client where liability.BOOK_NO = client.BOOK_NO AND client.CLIENT_ID = '{cid}'")
        total_liability = sql.fetchone()
        self.total_liability_label.text = "Total Liability: "+str(total_liability[0])
        print(self.total_liability_label.text)

        sql.execute(f"select sum(ABS(AMOUNT*TAX/100)) from source_of_cashflow s, keep_in_book k where s.CASHFLOW_ID = k.CASHFLOW_ID AND s.CLIENT_ID = k.C_ID AND TAX_PAYED = '0' AND k.C_ID = '{cid}'")
        total_unpaid_tax = sql.fetchone()
        self.total_unpaid_tax_label.text = "Total Unpaid Tax: "+str(total_unpaid_tax[0])
        print(self.total_unpaid_tax_label.text)

        self.net_asset_label.text = "Net Assets: "+str(total_asset[0]-total_liability[0])
        print(self.net_asset_label.text)
