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
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from Main_Menu import *
# from .Log_Out import *
# from .mainmenu import *

class client_select(GridLayout):
    def __init__(self, eid, **kwargs):
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 2#attribute of GridLayout
        self.cols = 1
        clients_button = Button(text = "Select Client")
        clients_dropdown = DropDown()
        sql.execute(f"SELECT * FROM client WHERE E_ID = '{eid}'")
        clients = sql.fetchall()
        # print("Getting clients, eid = "+eid)
        for client in clients:
            # print(client)
            cli_option = Button(text = client[7], size_hint_y=None, height=44)
            cli_option.bind(on_release=lambda btn: clients_dropdown.select(btn.text))
            clients_dropdown.add_widget(cli_option)
        clients_button.bind(on_press = clients_dropdown.open)
        self.add_widget(clients_button)
        clients_dropdown.bind(on_select = lambda instance, x: main_menu_launch(x, app, "main_menu_screen"))

        self.logout = Button(text = "Log Out")
        self.logout.bind(on_press = self.logout_pressed)
        self.add_widget(self.logout)
# (on_press = lambda *args: main_menu_launch(client[7], app, "main_menu_screen"))
    def logout_pressed(self, instance):
        header.remove_widget(tab)
        header.clear_widgets()

class app_home():
    def __init__(self, main_eid, **kwargs):
        self.screenmanager = ScreenManager()
        global eid
        eid = main_eid

        self.client_select_object = client_select(eid)
        client_select_screen = Screen(name = 'client_select_screen')
        client_select_screen.add_widget(self.client_select_object)
        self.screenmanager.add_widget(client_select_screen)

        self.main_menu_object = main_menu()
        main_menu_screen = Screen(name = 'main_menu_screen')
        main_menu_screen.add_widget(self.main_menu_object)
        self.screenmanager.add_widget(main_menu_screen)

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
    def run(self, main_header, main_tab):
        global app
        global header
        global tab
        tab = main_tab
        header = main_header
        app = self
        return self.screenmanager
