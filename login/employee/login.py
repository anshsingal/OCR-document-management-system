import kivy
import os
import sys
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from .register import *
from kivy.uix.popup import Popup
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()

uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
app_path_emp = os.path.join(uppath(__file__, 3), 'employee_application')
sys.path.append(app_path_emp)
from emp_app import app_home

class login_employee_launch():
    def __init__(self, main_app, main_header, screen):
        global app
        global header
        header = main_header
        app = main_app
        app.screenmanager.current = screen

class login_employee(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 4#attribute of GridLayout
        self.cols = 2

        self.eid_label = Label(text = "Employee ID")
        self.add_widget(self.eid_label)

        self.eid = TextInput()
        self.add_widget(self.eid)

        self.pass_label = Label(text = "Password")
        self.add_widget(self.pass_label)

        self.password = TextInput()
        self.add_widget(self.password)

        self.register = Button(text = "Register")
        self.register.bind(on_press = self.register_pressed)
        self.add_widget(self.register)

        self.login = Button(text = "Log In")
        self.login.bind(on_press = self.login_pressed)
        self.add_widget(self.login)

        self.back = Button(text = "Back")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

    def back_pressed(self, instance):
        # app.screenmanager.transition = SlideTransition(direction = 'right')
        app.screenmanager.current = "enterMenu_screen"

    def register_pressed(self, instance):
        register_employee_launch(app, "register_employee_screen")

    def login_pressed(self, instance):
        sql.execute("SELECT EID FROM employee WHERE EID = %s AND PASSWORD = %s", (self.eid.text, self.password.text))
        result = sql.fetchall()
        if len(result) == 0:
            popup_layout = GridLayout(rows = 2)
            popup_layout.add_widget(Label(text='Invalid Username / Password'))

            close_popup = Button(text = "Close")
            popup_layout.add_widget(close_popup)

            invalid_login_popup = Popup(title='Error', content=popup_layout, size_hint=(.3, .3))
            close_popup.bind(on_press=invalid_login_popup.dismiss)
            invalid_login_popup.open()
        else:
            th = TabbedPanelHeader(text=self.eid.text)
            th.content = app_home().run(self.eid.text, header, th)
            header.add_widget(th)
