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
from Add_CashFlows import *
from Create_Transaction import *
from Enter_Tax_Details import *
from Summarize import *
from View import *
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()

class main_menu_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class main_menu(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 6#attribute of GridLayout
        self.cols = 1

        self.add_cashflow = Button(text = "Add CashFlows")
        self.add_cashflow.bind(on_press = self.add_cashflow_pressed)
        self.add_widget(self.add_cashflow)

        self.create_transaction = Button(text = "Create Transaction")
        self.create_transaction.bind(on_press = self.create_transaction_pressed)
        self.add_widget(self.create_transaction)

        self.enter_tax_details = Button(text = "Enter Tax Details")
        self.enter_tax_details.bind(on_press = self.enter_tax_details_pressed)
        self.add_widget(self.enter_tax_details)

        self.summarize = Button(text = "Summarize")
        self.summarize.bind(on_press = self.summarize_pressed)
        self.add_widget(self.summarize)

        self.view = Button(text = "View")
        self.view.bind(on_press = self.view_pressed)
        self.add_widget(self.view)

        self.back = Button(text = "Back")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

    def add_cashflow_pressed(self, instance):
        add_cashflow_launch(cid, app, 'add_cashflow_screen')

    def create_transaction_pressed(self, instance):
        create_transaction_launch(cid, app, 'create_transaction_screen')

    def enter_tax_details_pressed(self, instance):
        enter_tax_details_launch(cid, app, 'enter_tax_details_screen')

    def summarize_pressed(self, instance):
        summarize_launch(cid, app, 'summarize_screen')

    def view_pressed(self, instance):
        view_launch(cid, app, 'view_screen')

    def back_pressed(self, instance):
        app.screenmanager.current = "client_select_screen"
