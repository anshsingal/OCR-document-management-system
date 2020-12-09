import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from login.client.login import *
from login.employee.login import *
from login.employee.register import register_employee

class enterMenu(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 2#attribute of GridLayout
        self.employee = Button(text = "Employee")
        self.employee.bind(on_press = self.employee_pressed)
        self.client = Button(text = "Client")
        self.client.bind(on_press = self.client_pressed)
        self.add_widget(self.employee)#add label to gridlayout (add_widget is funct of GridLayout)
        self.add_widget(self.client)#add textinput

    def client_pressed(self, instance):
        login_client_launch(app, header, "login_client_screen")

    def employee_pressed(self, instance):
        login_employee_launch(app, header, "login_employee_screen")

class Login():#calling function
    def __init__(self, **kwargs):#.run() funct  of App class (inherited by application) calls the build function. if not found, there is a default definition of a black screen
        self.screenmanager = ScreenManager()

        self.enterMenu_object = enterMenu()
        enterMenu_screen = Screen(name = 'enterMenu_screen')
        enterMenu_screen.add_widget(self.enterMenu_object)
        self.screenmanager.add_widget(enterMenu_screen)

        self.login_client_object = login_client()
        login_client_screen = Screen(name = 'login_client_screen')
        login_client_screen.add_widget(self.login_client_object)
        self.screenmanager.add_widget(login_client_screen)

        self.login_employee_object = login_employee()
        login_employee_screen = Screen(name = 'login_employee_screen')
        login_employee_screen.add_widget(self.login_employee_object)
        self.screenmanager.add_widget(login_employee_screen)

        self.register_employee_object = register_employee()
        register_employee_screen = Screen(name = 'register_employee_screen')
        register_employee_screen.add_widget(self.register_employee_object)
        self.screenmanager.add_widget(register_employee_screen)

        self.register_client_object = register_client()
        register_client_screen = Screen(name = 'register_client_screen')
        register_client_screen.add_widget(self.register_client_object)
        self.screenmanager.add_widget(register_client_screen)
        #return an object of class page
    def run(self, main_header):
        global app
        global header
        app = self
        header = main_header
        return self.screenmanager
