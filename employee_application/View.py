import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from kivy.core.window import Window
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()

class view_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class view(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3
        self.cols = 1

        top = GridLayout(rows=1, size_hint_y=0.08)
        top.add_widget(Button(text = 'btn1'))
        top.add_widget(Button(text = 'btn2'))
        top.add_widget(Label())
        top.add_widget(Label())
        top.add_widget(Label())
        top.add_widget(Button(text = 'btn3'))
        self.add_widget(top)

        head = GridLayout(rows=1, size_hint_y=0.08)
        head.add_widget(Label(text = "Heading1"))
        head.add_widget(Label(text = "Heading2"))
        head.add_widget(Label(text = "Heading3"))
        head.add_widget(Label(text = "Heading4"))
        self.add_widget(head)

        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        root = ScrollView()
        root.bar_width = 10
        # slider = Slider()
        root.add_widget(layout)
        self.add_widget(root)
        # root2 = Widget()
        # root2.add_widget(Button())
        # slider = Slider()
        # root2.add_widget(slider)
        # self.add_widget(root2)
