import kivy
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
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
commit = accounts.commit

class enter_tax_details_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class enter_tax_details(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3
        self.cols = 1

        self.cashflow = Button(text = "Select Cashflow")
        self.cashflow.bind(on_press = self.cashflow_selected)
        self.add_widget(self.cashflow)

        self.tax = TextInput()
        self.add_widget(self.tax)


        self.button_layout = GridLayout(cols = 2)
        self.back = Button(text = "Back")
        self.back.bind(on_press = self.back_pressed)
        self.button_layout.add_widget(self.back)

        self.submit = Button(text = "Submit")
        self.submit.bind(on_press = self.submit_pressed)
        self.button_layout.add_widget(self.submit)

        self.add_widget(self.button_layout)

    def cashflow_selected(self, instance):
        self.cashflows_dropdown = DropDown()
        # print("EID = ", eid)
        sql.execute(f"SELECT CASHFLOW_ID FROM source_of_cashflow WHERE CLIENT_ID = '{cid}'")
        cashflows = sql.fetchall()
        for cashflow in cashflows:
            # print(client)
            self.cf_option = Button(text = cashflow[0], size_hint_y=None, height=44)
            self.cf_option.bind(on_release=lambda btn: self.cashflows_dropdown.select(btn.text))
            self.cashflows_dropdown.add_widget(self.cf_option)
        self.cashflows_dropdown.open(self.cashflow)
        self.cashflows_dropdown.bind(on_select = lambda instance, x: self.set_button_text(x))

    def set_button_text(self, name):
        self.cashflow.text = name
        sql.execute(f"SELECT TAX FROM source_of_cashflow WHERE CLIENT_ID = '{cid}' AND CASHFLOW_ID = '{name}'")
        cashflows = sql.fetchone()
        self.tax.text = str(cashflows[0])
        # print(cashflows[0])

    def submit_pressed(self, instance):
        # print(self.tax.text)
        # print(cid)
        # print(self.cashflow.text)
        sql.execute(f"UPDATE source_of_cashflow SET TAX = '{self.tax.text}' WHERE CLIENT_ID = '{cid}' AND CASHFLOW_ID = '{self.cashflow.text}'")
        commit()

    def back_pressed(self, instance):
        app.screenmanager.current = 'main_menu_screen'
