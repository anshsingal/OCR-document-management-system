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
from .tesseract import *
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

class negative_transaction_launch():
    def __init__(self, main_cashflow, main_book, main_amount, main_date_time, tax_payed_bool, main_app, screen):
        global app
        global book_no
        global amount
        global date_time
        global cashflow
        global tax_payed
        tax_payed = tax_payed_bool
        cashflow = main_cashflow
        date_time = main_date_time
        book_no = main_book
        amount = main_amount
        app = main_app
        app.screenmanager.current = screen

class negative_transaction(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 2
        self.cols = 1
        # self.label = Label(text = "This is negative transaction")
        # self.add_widget(self.label)
        self.add_liability = Button(text = "Add Liability")
        # self.add_liability.bind(on_press = self.add_liability_pressed)
        self.add_liability.bind(on_press = lambda instance : self.button_pressed(1))
        self.add_widget(self.add_liability)

        self.reduce_asset = Button(text = "Reduce Asset")
        # self.reduce_asset.bind(on_press = self.reduce_asset_pressed)
        self.reduce_asset.bind(on_press = lambda instance : self.button_pressed(2))
        self.add_widget(self.reduce_asset)

    def button_pressed(self, option):
        self.popup_layout = GridLayout(rows = 2)
        # popup_layout.add_widget(Label(text='Transaction Added'))
        self.file_chooser = FileChooserIconView(size_hint_y=4, path='C:\\Users\\anshs\\Desktop\\study\\5th_sem\\DBD\\project\\bills', multiselect = True)
        self.popup_layout.add_widget(self.file_chooser)

        self.close_popup = Button(text = "OK", height = 44)
        if option == 1:
            self.close_popup.bind(on_press = self.add_liability_pressed)
        else:
            self.close_popup.bind(on_press = self.reduce_asset_pressed)
        self.popup_layout.add_widget(self.close_popup)

        self.file_chooser_popup = Popup(title='Choose File', content=self.popup_layout, size_hint=(.7, .7))
        # close_popup.bind(on_press = success_popup.dismiss)
        self.file_chooser_popup.open()



    def reduce_asset_pressed(self, instance):
        print("you pressed reduce asset")
        self.file_path = self.file_chooser.selection
        self.file_chooser_popup.dismiss()
        # print(self.file_path)
        id = self.store_documents()
        sql.execute("INSERT INTO `asset` VALUES (%s, %s)", (str(id), amount))
        sql.execute("INSERT INTO `keep_in_book` VALUES (%s, %s, %s, %s, %s, %s)", (str(id), cashflow, book_no, date_time, amount, tax_payed))
        commit()
        self.go_back()


    def add_liability_pressed(self, instance):
        print("you pressed add liability")
        self.file_path = self.file_chooser.selection
        self.file_chooser_popup.dismiss()
        id = self.store_documents()
        sql.execute("INSERT INTO `liability` VALUES (%s, %s)", (str(id), amount[1:]))
        sql.execute("INSERT INTO `keep_in_book` VALUES (%s, %s, %s, %s, %s, %s)", (str(id), cashflow, book_no, date_time, amount, tax_payed))
        commit()
        self.go_back()




    def store_documents(self):
        # print(self.file_path)
        self.loading_popup_open()
        with open(self.file_path[0], 'rb') as file:
            self.data = file.read()
        text = convert(self.file_path[0])
        if self.file_path[0][-4:] == 'JPEG' or self.file_path[0][-4:] == 'jpeg':
            self.extension = self.file_path[0][-5:]
        else:
            self.extension = self.file_path[0][-4:]
        id = (db['files'].insert_one({'file_data': self.data, 'text': text, 'extension':self.extension})).inserted_id
        # sql.execute("INSERT INTO `expense` VALUES (%s, %s, %s)", (str(id), amount, tax_payed))
        self.loading_popup.dismiss()
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

    def loading_popup_open(self):
        print("Loading popup")
        self.loading_popup = Popup(title='Loading', content=Label(text = "Extracting text and uploading documents"), size_hint=(.3, .3))
        self.loading_popup.open()
