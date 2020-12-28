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
# from kivy.uix.slider import Slider
# from kivy.core.window import Window
import re
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
import pymongo
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('localhost', 27017)
db = client['accounts']

class search_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class search(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 4
        self.cols = 1

        top = GridLayout(rows=1, size_hint_y=0.08)

        search_label = Label(text = "Enter Search String:")
        self.search_input = TextInput()
        search_button = Button(text = 'Search')
        search_button.bind(on_press = self.search_button_pressed)

        top.add_widget(search_label)
        top.add_widget(self.search_input)
        top.add_widget(search_button)
        self.add_widget(top)

        self.head = GridLayout(rows=1, size_hint_y=0.08)
        self.head.add_widget(Label(text = "Search Results"))
        self.head.add_widget(Label())
        self.add_widget(self.head)

        self.root = ScrollView()
        self.root.bar_width = 10
        self.add_widget(self.root)

        self.layout = GridLayout(cols=6, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.root.add_widget(self.layout)

        back = Button(text = 'Back', size_hint_y=None, height = 20)
        back.bind(on_press = self.back_pressed)
        self.add_widget(back)

    def search_button_pressed(self, instance):
        self.layout.clear_widgets()
        pat = re.compile(rf'{self.search_input.text}', re.I)
        results = db.files.find({ "text": {'$regex': pat}})

        # if not len(list(results)) == 0:

        for result in results:
            print(result['_id'])
            # print(str(cashflow['_id']))
            print(result['_id'])
            sql.execute(f"select distinct k.AMOUNT, k.CASHFLOW_ID, s.TAX, k.DATE_TIME, k.TAX_PAYED, k.ID from keep_in_book k, source_of_cashflow s where k.amount>0 AND k.CASHFLOW_ID = s.CASHFLOW_ID AND k.ID = '{str(result['_id'])}'")
            cashflow = sql.fetchone()
            print(cashflow)

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

    def download_button_pressed(self, id):
        print("Received ID = ", id)
        doc = db['files'].find_one({'_id':ObjectId(id)})
        with open('C:\\Users\\anshs\\Desktop\\DOCUMENT'+doc['extension'], 'wb') as file:
            file.write(doc['file_data'])

    def back_pressed(self, instance):
        app.screenmanager.current = 'view_screen'
