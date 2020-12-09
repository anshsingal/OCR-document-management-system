import kivy
from kivy.app import App
from kivy.uix.label import Label

class app_home():
    def __init__(self, **kwargs):
        self.label = Label(text = "This is app")
    def run(self):
        return self.label
