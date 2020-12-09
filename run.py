import kivy
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
from login.main import *

class Test(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.th = TabbedPanelHeader(text='Log in')
        self.th.content = Login().run(self)
        self.add_widget(self.th)

class Accounts(App):
    def build(self):
        return Test()

if __name__ == "__main__":
    app = Accounts()
    app.run()
