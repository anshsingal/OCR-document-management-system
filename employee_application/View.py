import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.core.window import Window
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
import pymongo
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('localhost', 27017)
db = client['accounts']

class view_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class view(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3
        self.cols = 1

        top = GridLayout(rows=1, size_hint_y=0.08)
        revenue_button = Button(text = 'Revenue')
        revenue_button.bind(on_press = self.revenue_button_pressed)
        expense_button = Button(text = 'Expense')
        expense_button.bind(on_press = self.expense_button_pressed)
        assets_button = Button(text = 'Assets')
        assets_button.bind(on_press = self.assets_button_pressed)
        liabilities_button = Button(text = 'Liabilities')
        liabilities_button.bind(on_press = self.liabilities_button_pressed)
        top.add_widget(revenue_button)
        top.add_widget(expense_button)
        top.add_widget(assets_button)
        top.add_widget(liabilities_button)
        top.add_widget(Label())
        top.add_widget(Label())
        top.add_widget(Label())
        top.add_widget(Button(text = 'Search'))
        self.add_widget(top)

        self.head = GridLayout(rows=1, size_hint_y=0.08)
        self.add_widget(self.head)

        self.root = ScrollView()
        self.root.bar_width = 10
        self.add_widget(self.root)

        self.layout = GridLayout(cols=6, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.root.add_widget(self.layout)

    def revenue_button_pressed(self, instance):
        self.head.clear_widgets()
        self.layout.clear_widgets()
        self.head.add_widget(Label(text = "Amount"))
        self.head.add_widget(Label(text = "Cashflow ID"))
        self.head.add_widget(Label(text = "Tax Rate"))
        self.head.add_widget(Label(text = "Time Stamp"))
        self.head.add_widget(Label(text = "Tax Payed?"))
        self.head.add_widget(Label(text = "Download documents"))

        sql.execute(f"select distinct k.AMOUNT, k.CASHFLOW_ID, s.TAX, k.DATE_TIME, k.TAX_PAYED, k.ID from keep_in_book k, client c, source_of_cashflow s where k.amount>0 AND k.CASHFLOW_ID = s.CASHFLOW_ID AND c.BOOK_NO = k.BOOK_NO AND c.CLIENT_ID = '{cid}' ORDER BY k.DATE_TIME DESC")
        cashflows = sql.fetchall()
        for cashflow in cashflows:
            amount_label = Label(text = f"{cashflow[0]}", size_hint_y=None, height=40)
            self.layout.add_widget(amount_label)

            cashflow_label = Label(text = f"{cashflow[1]}", size_hint_y=None, height=40)
            self.layout.add_widget(cashflow_label)

            tax_label = Label(text = f"{cashflow[2]}", size_hint_y=None, height=40)
            self.layout.add_widget(tax_label)

            date_time_label = Label(text = f'{cashflow[3].strftime("%d-%m-%Y %H:%M")}', size_hint_y=None, height=40)
            self.layout.add_widget(date_time_label)

            if cashflow[4]:
                tax_payed_label = Label(text = "Yes", size_hint_y=None, height=40)
            else:
                tax_payed_label = Label(text = "No", size_hint_y=None, height=40)
            self.layout.add_widget(tax_payed_label)

            download_button = Button(text = "Download File", size_hint_y=None, height=40)
            # lam = lambda c = cashflow[-1]: self.download_button_pressed(c)
            download_button.bind(on_press = lambda instance, c = cashflow[-1]: self.download_button_pressed(c))
            # download_button.bind(on_press = lambda instance: lambda c = cashflow[-1]: print(c))
            self.layout.add_widget(download_button)



    def expense_button_pressed(self, instance):
        self.head.clear_widgets()
        self.layout.clear_widgets()
        self.head.add_widget(Label(text = "Amount"))
        self.head.add_widget(Label(text = "Cashflow ID"))
        self.head.add_widget(Label(text = "Tax Rate"))
        self.head.add_widget(Label(text = "Time Stamp"))
        self.head.add_widget(Label(text = "Tax Payed?"))
        self.head.add_widget(Label(text = "Download documents"))
        # self.layout = GridLayout(cols=6, spacing=10, size_hint_y=None)
        # self.layout.bind(minimum_height=self.layout.setter('height'))

        sql.execute(f"select distinct k.AMOUNT, k.CASHFLOW_ID, s.TAX, k.DATE_TIME, k.TAX_PAYED, k.ID from keep_in_book k, client c, source_of_cashflow s where k.amount<0 AND k.CASHFLOW_ID = s.CASHFLOW_ID AND c.BOOK_NO = k.BOOK_NO AND c.CLIENT_ID = '{cid}' ORDER BY k.DATE_TIME DESC")
        cashflows = sql.fetchall()
        for cashflow in cashflows:
            amount_label = Label(text = f"{cashflow[0]}", size_hint_y=None, height=40)
            self.layout.add_widget(amount_label)

            cashflow_label = Label(text = f"{cashflow[1]}", size_hint_y=None, height=40)
            self.layout.add_widget(cashflow_label)

            tax_label = Label(text = f"{cashflow[2]}", size_hint_y=None, height=40)
            self.layout.add_widget(tax_label)

            date_time_label = Label(text = f'{cashflow[3].strftime("%d-%m-%Y %H:%M")}', size_hint_y=None, height=40)
            self.layout.add_widget(date_time_label)

            if cashflow[4]:
                tax_payed_label = Label(text = "Yes", size_hint_y=None, height=40)
            else:
                tax_payed_label = Label(text = "No", size_hint_y=None, height=40)
            self.layout.add_widget(tax_payed_label)

            download_button = Button(text = "Download File", size_hint_y=None, height=40)
            download_button.bind(on_press = lambda instance, c = cashflow[-1]: self.download_button_pressed(c))
            self.layout.add_widget(download_button)

    def assets_button_pressed(self, instance):
        self.head.clear_widgets()
        self.layout.clear_widgets()
        self.head.add_widget(Label(text = "Amount"))
        self.head.add_widget(Label(text = "Download documents"))

        sql.execute(f"select distinct a.AMOUNT, a.ID from keep_in_book k, client c, asset a where k.ID = a.ID AND c.BOOK_NO = k.BOOK_NO AND c.CLIENT_ID = '{cid}'")
        cashflows = sql.fetchall()
        for cashflow in cashflows:
            self.layout.add_widget(Label())

            amount_label = Label(text = f"{cashflow[0]}", size_hint_y=None, height=40)
            self.layout.add_widget(amount_label)

            self.layout.add_widget(Label())
            self.layout.add_widget(Label())
            # print("cashflow[-1] = " ,cashflow[-1])
            download_button = Button(text = "Download File", size_hint_y=None, height=40)
            download_button.bind(on_press = lambda instance, c = cashflow[-1]: self.download_button_pressed(c))
            self.layout.add_widget(download_button)

            self.layout.add_widget(Label())

    def liabilities_button_pressed(self, instance):
        self.head.clear_widgets()
        self.layout.clear_widgets()
        self.head.add_widget(Label(text = "Amount"))
        self.head.add_widget(Label(text = "Download documents"))

        sql.execute(f"select distinct l.AMOUNT, l.ID from keep_in_book k, client c, liability l where k.ID = l.ID AND c.BOOK_NO = k.BOOK_NO AND c.CLIENT_ID = '{cid}'")
        cashflows = sql.fetchall()
        for cashflow in cashflows:
            self.layout.add_widget(Label())

            amount_label = Label(text = f"{cashflow[0]}", size_hint_y=None, height=40)
            self.layout.add_widget(amount_label)

            self.layout.add_widget(Label())
            self.layout.add_widget(Label())

            download_button = Button(text = "Download File", size_hint_y=None, height=40)
            download_button.bind(on_press = lambda instance, c = cashflow[-1]: self.download_button_pressed(c))
            self.layout.add_widget(download_button)

            self.layout.add_widget(Label())


    def download_button_pressed(self, id):
        print("Received ID = ", id)
        doc = db['files'].find_one({'_id':ObjectId(id)})
        with open('C:\\Users\\anshs\\Desktop\\DOCUMENT'+doc['extension'], 'wb') as file:
            file.write(doc['file_data'])
