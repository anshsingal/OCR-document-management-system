import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from .register import *

class login_employee_launch():
    def __init__(self, main_app, screen):
        global app
        app = main_app
        app.screenmanager.current = screen

class login_employee(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3#attribute of GridLayout
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

    def register_pressed(self, instance):
        register_employee_launch(app, "register_employee_screen")

    def login_pressed(self, instance):
        app.screenmanager.current = "enterMenu_screen"
