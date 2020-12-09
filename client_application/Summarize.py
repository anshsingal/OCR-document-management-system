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

class summarize_launch():
    def __init__(self, main_app, screen):
        global app
        app = main_app
        app.screenmanager.current = screen

class summarize(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 1
        self.cols = 1
        self.label = Label(text = "This is summarize")
        self.add_widget(self.label)
