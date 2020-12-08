import kivy
from kivy.app import App
# from kivy.uix.label import Label
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.image import Image
# from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from login.try_main import *

class Test(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.th = TabbedPanelHeader(text='Log in')
        self.th.content = Login().run()
        self.add_widget(self.th)

class Accounts(App):
    def build(self):
        return Test()

if __name__ == "__main__":
    app = Accounts()
    app.run()
