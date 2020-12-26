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
from kivy.uix.filechooser import FileChooserIconView
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
commit = accounts.commit
import pymongo
from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('localhost', 27017)
db = client['accounts']

class positive_transaction_launch():
    def __init__(self, main_cashflow, main_book, main_amount, set_date, main_app, screen):
        global app
        global book_no
        global amount
        global date
        global cashflow
        cashflow = main_cashflow
        date = set_date
        book_no = main_book
        amount = main_amount
        app = main_app
        app.screenmanager.current = screen

class positive_transaction(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 2
        self.cols = 1
        # self.label = Label(text = "This is positive transaction")
        # self.add_widget(self.label)
        self.add_asset = Button(text = "Add Asset")
        # self.add_liability.bind(on_press = self.add_liability_pressed)
        self.add_asset.bind(on_press = lambda instance : self.button_pressed(1))
        self.add_widget(self.add_asset)

        self.reduce_liability = Button(text = "Reduce Liability")
        # self.reduce_asset.bind(on_press = self.reduce_asset_pressed)
        self.reduce_liability.bind(on_press = lambda instance : self.button_pressed(2))
        self.add_widget(self.reduce_liability)

    def button_pressed(self, option):
        self.popup_layout = GridLayout(rows = 2)
        # popup_layout.add_widget(Label(text='Transaction Added'))
        self.file_chooser = FileChooserIconView(size_hint_y=4, path='C:\\Users\\anshs\\Desktop', multiselect = True)
        self.popup_layout.add_widget(self.file_chooser)

        self.close_popup = Button(text = "OK", height = 44)
        if option == 1:
            self.close_popup.bind(on_press = self.add_asset_pressed)
        else:
            self.close_popup.bind(on_press = self.reduce_liability_pressed)
        self.popup_layout.add_widget(self.close_popup)

        self.success_popup = Popup(title='Success', content=self.popup_layout, size_hint=(.7, .7))
        # close_popup.bind(on_press = success_popup.dismiss)
        self.success_popup.open()

    def reduce_liability_pressed(self, instance):
        print("you pressed reduce liability")
        self.file_path = self.file_chooser.selection
        self.success_popup.dismiss()
        print(self.file_path)
        id = self.store_documents()
        sql.execute("INSERT INTO `liability` VALUES (%s, %s, %s, %s)", (str(id), book_no, cashflow, amount))
        commit()
        self.go_back()


    def add_asset_pressed(self, instance):
        print("you pressed add asset")
        self.file_path = self.file_chooser.selection
        self.success_popup.dismiss()
        id = self.store_documents()
        sql.execute("INSERT INTO `asset` VALUES (%s, %s, %s, %s)", (str(id), book_no, cashflow, amount))
        commit()
        self.go_back()


    def store_documents(self):
        print(self.file_path)
        with open(self.file_path[0], 'rb') as file:
            self.data = file.read()
        id = (db['expense'].insert_one({'file_data': self.data})).inserted_id
        sql.execute("INSERT INTO `revenue` VALUES (%s, %s, %s, %s)", (str(id), book_no, date, amount))
        commit()
        return id

    def go_back(self):
        popup_layout = GridLayout(rows = 2)
        popup_layout.add_widget(Label(text='Transaction Added'))

        close_popup = Button(text = "OK")
        popup_layout.add_widget(close_popup)

        success_popup = Popup(title='Success', content=popup_layout, size_hint=(.3, .3))
        close_popup.bind(on_press = success_popup.dismiss)
        success_popup.open()
        app.screenmanager.current = 'main_menu_screen'
