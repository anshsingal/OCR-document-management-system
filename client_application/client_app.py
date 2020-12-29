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
from client_Summarize.client_Summarize import *
from client_View.client_View import *
from client_View.client_Search import *

# from .Log_Out import *
# from .mainmenu import *

class MainMenu(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 3#attribute of GridLayout
        self.cols = 1

        self.summarize = Button(text = "Summarize")
        self.summarize.bind(on_press = self.client_summarize_pressed)
        self.add_widget(self.summarize)

        self.view = Button(text = "View")
        self.view.bind(on_press = self.client_view_pressed)
        self.add_widget(self.view)

        self.logout = Button(text = "Log Out")
        self.logout.bind(on_press = self.logout_pressed)
        self.add_widget(self.logout)

    def client_summarize_pressed(self, instance):
        client_summarize_launch(cid, app, 'client_summarize_screen')

    def client_view_pressed(self, instance):
        client_view_launch(cid, app, 'client_view_screen')

    def logout_pressed(self, instance):
        # logout_launch(app, header, 'logout_screen')
        header.remove_widget(tab)
        header.clear_widgets()

class app_home():
    def __init__(self, **kwargs):
        self.screenmanager = ScreenManager()

        self.MainMenu_object = MainMenu()
        MainMenu_screen = Screen(name = 'client_main_menu_screen')
        MainMenu_screen.add_widget(self.MainMenu_object)
        self.screenmanager.add_widget(MainMenu_screen)

        self.client_summarize_object = client_summarize()
        client_summarize_screen = Screen(name = 'client_summarize_screen')
        client_summarize_screen.add_widget(self.client_summarize_object)
        self.screenmanager.add_widget(client_summarize_screen)

        self.client_view_object = client_view()
        client_view_screen = Screen(name = 'client_view_screen')
        client_view_screen.add_widget(self.client_view_object)
        self.screenmanager.add_widget(client_view_screen)

        self.client_search_object = client_search()
        client_search_screen = Screen(name = 'client_search_screen')
        client_search_screen.add_widget(self.client_search_object)
        self.screenmanager.add_widget(client_search_screen)

        # self.logout_object = logout()
        # logout_screen = Screen(name = 'logout_screen')
        # logout_screen.add_widget(self.logout_object)
        # self.screenmanager.add_widget(logout_screen)
    def run(self, main_cid, main_header, main_tab):
        global app
        global header
        global tab
        global cid
        tab = main_tab
        cid = main_cid
        header = main_header
        app = self
        return self.screenmanager
