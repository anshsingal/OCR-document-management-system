import kivy
import os
import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from Add_CashFlows import *
from Create_Transaction import *
from Enter_Tax_Details import *
from Summarize import *
from View import *
# from .Log_Out import *
# from .mainmenu import *

class MainMenu(GridLayout):
    def __init__(self, **kwargs):
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

        self.logout = Button(text = "Log Out")
        self.logout.bind(on_press = self.logout_pressed)
        self.add_widget(self.logout)

    def add_cashflow_pressed(self, instance):
        add_cashflow_launch(app, 'add_cashflow_screen')

    def create_transaction_pressed(self, instance):
        create_transaction_launch(app, 'create_transaction_screen')

    def enter_tax_details_pressed(self, instance):
        enter_tax_details_launch(app, 'enter_tax_details_screen')

    def summarize_pressed(self, instance):
        summarize_launch(app, 'summarize_screen')

    def view_pressed(self, instance):
        view_launch(app, 'view_screen')

    def logout_pressed(self, instance):
        header.remove_widget(tab)
        header.clear_widgets()

class app_home():
    def __init__(self, **kwargs):
        self.screenmanager = ScreenManager()

        self.MainMenu_object = MainMenu()
        MainMenu_screen = Screen(name = 'MainMenu_screen')
        MainMenu_screen.add_widget(self.MainMenu_object)
        self.screenmanager.add_widget(MainMenu_screen)

        self.add_cashflow_object = add_cashflow()
        add_cashflow_screen = Screen(name = 'add_cashflow_screen')
        add_cashflow_screen.add_widget(self.add_cashflow_object)
        self.screenmanager.add_widget(add_cashflow_screen)

        self.create_transaction_object = create_transaction()
        create_transaction_screen = Screen(name = 'create_transaction_screen')
        create_transaction_screen.add_widget(self.create_transaction_object)
        self.screenmanager.add_widget(create_transaction_screen)

        self.enter_tax_details_object = enter_tax_details()
        enter_tax_details_screen = Screen(name = 'enter_tax_details_screen')
        enter_tax_details_screen.add_widget(self.enter_tax_details_object)
        self.screenmanager.add_widget(enter_tax_details_screen)

        self.summarize_object = summarize()
        summarize_screen = Screen(name = 'summarize_screen')
        summarize_screen.add_widget(self.summarize_object)
        self.screenmanager.add_widget(summarize_screen)

        self.view_object = view()
        view_screen = Screen(name = 'view_screen')
        view_screen.add_widget(self.view_object)
        self.screenmanager.add_widget(view_screen)

        # self.logout_object = logout()
        # logout_screen = Screen(name = 'logout_screen')
        # logout_screen.add_widget(self.logout_object)
        # self.screenmanager.add_widget(logout_screen)
    def run(self, eid, main_header, main_tab):
        global app
        global header
        global tab
        tab = main_tab
        header = main_header
        app = self
        return self.screenmanager
