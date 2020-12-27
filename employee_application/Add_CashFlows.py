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
commit = accounts.commit

class add_cashflow_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class add_cashflow(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 5
        self.cols = 2

        self.cashflow_id_label = Label(text = "CashFlow ID")
        self.add_widget(self.cashflow_id_label)
        self.cashflow_id = TextInput()
        self.add_widget(self.cashflow_id)

        self.name_label = Label(text = "Name")
        self.add_widget(self.name_label)
        self.name = TextInput()
        self.add_widget(self.name)

        self.type_label = Label(text = "Type")
        self.add_widget(self.type_label)
        self.type = TextInput()
        self.add_widget(self.type)

        self.tax_label = Label(text = "Tax Rate")
        self.add_widget(self.tax_label)
        self.tax = TextInput()
        self.add_widget(self.tax)

        self.back = Button(text = "Back")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

        self.submit = Button(text = "Submit")
        self.submit.bind(on_press = self.submit_pressed)
        self.add_widget(self.submit)

    def back_pressed(self, instance):
        app.screenmanager.current = 'main_menu_screen'

    def submit_pressed(self, instance):
        sql.execute("INSERT INTO `source_of_cashflow` VALUES (%s, %s, %s, %s, %s)", (self.cashflow_id.text, cid, self.name.text, self.type.text, self.tax.text))
        commit()
        # back_pressed(None)
        popup_layout = GridLayout(rows = 2)
        popup_layout.add_widget(Label(text='CashFlow Added'))

        close_popup = Button(text = "OK")
        popup_layout.add_widget(close_popup)

        success_popup = Popup(title='Success', content=popup_layout, size_hint=(.3, .3))
        close_popup.bind(on_press = success_popup.dismiss)
        success_popup.open()
        self.back_pressed(None)
