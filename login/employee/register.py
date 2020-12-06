import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
commit = accounts.commit

class register_employee_launch():
    def __init__(self, main_app, screen):
        global app
        app = main_app
        app.screenmanager.current = screen

class register_employee(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 8#attribute of GridLayout
        self.cols = 2

        self.name_label = Label(text = "Name")
        self.add_widget(self.name_label)
        self.name = TextInput()
        self.add_widget(self.name)

        self.email_label = Label(text = "E-Mail")
        self.add_widget(self.email_label)
        self.email = TextInput()
        self.add_widget(self.email)

        self.sex_label = Label(text = "Sex")
        self.add_widget(self.sex_label)
        self.sex = TextInput()
        self.add_widget(self.sex)

        self.age_label = Label(text = "Age")
        self.add_widget(self.age_label)
        self.age = TextInput()
        self.add_widget(self.age)

        self.phone_label = Label(text = "Phone No.")
        self.add_widget(self.phone_label)
        self.phone = TextInput()
        self.add_widget(self.phone)

        self.eid_label = Label(text = "Employee ID")
        self.add_widget(self.eid_label)
        self.eid = TextInput()
        self.add_widget(self.eid)

        self.password_label = Label(text = "Password")
        self.add_widget(self.password_label)
        self.password = TextInput()
        self.add_widget(self.password)

        self.back = Button(text = "Back to Log-in")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

        self.register = Button(text = "Register")
        self.register.bind(on_press = self.register_pressed)
        self.add_widget(self.register)

    def register_pressed(self, instance):
        sql.execute("INSERT INTO `employee` VALUES (%s, %s, %s, %s, %s, %s, %s)", (self.name.text, self.email.text, self.sex.text, self.age.text, self.phone.text, self.eid.text, self.password.text))
        commit()
        app.screenmanager.current = "login_employee_screen"

    def back_pressed(self, instance):
        app.screenmanager.transition = SlideTransition(direction = 'right')
        app.screenmanager.current = "login_employee_screen"
