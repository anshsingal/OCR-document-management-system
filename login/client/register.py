import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
commit = accounts.commit

class register_client_launch():
    def __init__(self, main_app, screen):
        global app
        app = main_app
        app.screenmanager.current = screen

class register_client(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 11#attribute of GridLayout
        self.cols = 2

        self.name_label = Label(text = "Name")
        self.add_widget(self.name_label)
        self.name = TextInput()
        self.add_widget(self.name)

        self.email_label = Label(text = "E-Mail")
        self.add_widget(self.email_label)
        self.email = TextInput()
        self.add_widget(self.email)

        self.age_label = Label(text = "Age")
        self.add_widget(self.age_label)
        self.age = TextInput()
        self.add_widget(self.age)

        self.pan_label = Label(text = "PAN")
        self.add_widget(self.pan_label)
        self.pan = TextInput()
        self.add_widget(self.pan)

        self.phone_label = Label(text = "Phone No.")
        self.add_widget(self.phone_label)
        self.phone = TextInput()
        self.add_widget(self.phone)

        self.aadhar_label = Label(text = "Aadhar No.")
        self.add_widget(self.aadhar_label)
        self.aadhar = TextInput()
        self.add_widget(self.aadhar)

        self.eid_label = Label(text = "Acting Employee")
        self.add_widget(self.eid_label)
        self.eid = TextInput()
        self.add_widget(self.eid)

        self.cid_label = Label(text = "Client ID")
        self.add_widget(self.cid_label)
        self.cid = TextInput()
        self.add_widget(self.cid)

        self.password_label = Label(text = "Password")
        self.add_widget(self.password_label)
        self.password = TextInput()
        self.add_widget(self.password)

        self.book_label = Label(text = "Book No.")
        self.add_widget(self.book_label)
        self.book = TextInput()
        self.add_widget(self.book)

        self.back = Button(text = "Back to Log-in")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

        self.register = Button(text = "Register")
        self.register.bind(on_press = self.register_pressed)
        self.add_widget(self.register)

    def register_pressed(self, instance):
        sql.execute("INSERT INTO `client` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.name.text, self.email.text, self.age.text, self.pan.text, self.phone.text, self.aadhar.text, self.eid.text, self.cid.text, self.password.text, self.book.text))
        commit()
        app.screenmanager.current = "login_client_screen"

    def back_pressed(self, instance):
        app.screenmanager.current = "login_client_screen"
