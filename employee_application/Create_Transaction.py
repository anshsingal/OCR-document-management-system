import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader
import datetime
import re
import mysql.connector
accounts = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'aaloo', database = 'accounts')
sql = accounts.cursor()
commit = accounts.commit


class create_transaction_launch():
    def __init__(self, main_cid, main_app, screen):
        global app
        global cid
        cid = main_cid
        app = main_app
        app.screenmanager.current = screen

class create_transaction(GridLayout):#innherit class GridLayout
    def __init__(self, **kwargs):#defining constructor for class page
        super().__init__(**kwargs)#defining constructor for class GridLayout
        self.rows = 6
        self.cols = 2
        self.cid = None
        self.chosen_cashflow = None

        cashflow_label = Label(text = "Select Cashflow")
        self.add_widget(cashflow_label)

        self.cashflows_button = Button(text = "Select CashFlow", height = 44)
        self.cashflows_button.bind(on_press = self.cashflows_button_pressed)
        self.add_widget(self.cashflows_button)

        self.book_label = Label(text = "Book No.")
        self.add_widget(self.book_label)
        self.book = TextInput()
        self.add_widget(self.book)

        self.amount_label = Label(text = "Amount")
        self.add_widget(self.amount_label)
        self.amount = TextInput()
        self.add_widget(self.amount)

        self.time_label = Label(text = "Time (If now, type 'Now')")
        self.add_widget(self.time_label)
        self.time = TextInput()
        self.add_widget(self.time)

        self.date_label = Label(text = "Date (If today, type 'Today')")
        self.add_widget(self.date_label)
        self.date = TextInput()
        self.add_widget(self.date)

        self.back = Button(text = "Back")
        self.back.bind(on_press = self.back_pressed)
        self.add_widget(self.back)

        self.submit = Button(text = "Submit")
        self.submit.bind(on_press = self.submit_pressed)
        self.add_widget(self.submit)


    def cashflows_button_pressed(self, instance):
        # print(cid)
        self.cashflows_dropdown = DropDown()
        sql.execute(f"SELECT CASHFLOW_ID FROM source_of_cashflow WHERE CLIENT_ID = '{cid}'")
        cashflows = sql.fetchall()
        print("Getting cashflows:")
        for cashflow in cashflows:
            # print(cashflow[0])
            cf_option = Button(text = cashflow[0], size_hint_y=None, height = 44)
            cf_option.bind(on_release=lambda btn: self.cashflows_dropdown.select(btn.text))
            self.cashflows_dropdown.add_widget(cf_option)
        self.cashflows_button.bind(on_press = self.cashflows_button_pressed)
        self.cashflows_dropdown.bind(on_select = lambda instance, x: self.set_chosen_cashflow(x))
        self.cashflows_dropdown.open(self.cashflows_button)


    def set_chosen_cashflow(self, x):
        self.chosen_cashflow = x
        self.cashflows_button.text = x

    def back_pressed(self, instance):
        app.screenmanager.current = 'main_menu_screen'

    def submit_pressed(self, instance):

        if self.chosen_cashflow == None:
            self.failed_popup()

        if self.time.text == 'Now' or self.time.text == 'now':
            time = datetime.datetime.now().strftime("%H:%M")
        elif re.match(r"^[0-2][0-9]:[0-5][0-9]", self.time.text):
            time = self.time.text
        else:
            self.failed_popup()

        if self.date.text == 'today' or self.date.text == 'Today':
            set_date = datetime.date.today().strftime("%d/%m/%Y")
        elif re.match(r"^[0-3][0-9]/[0-1][0-9]/[0-2][0-9][0-9][0-9]", self.date.text):
            set_date = self.date.text
        else:
            self.failed_popup()

        sql.execute("INSERT INTO `keep_in_book` VALUES (%s, %s, %s, %s, %s, %s)", (self.chosen_cashflow, cid, self.book.text, self.amount.text, time, set_date))
        commit()
        # back_pressed(None)
        popup_layout = GridLayout(rows = 2)
        popup_layout.add_widget(Label(text='Transaction Added'))

        close_popup = Button(text = "OK")
        popup_layout.add_widget(close_popup)

        success_popup = Popup(title='Success', content=popup_layout, size_hint=(.3, .3))
        close_popup.bind(on_press = success_popup.dismiss)
        success_popup.open()
        self.back_pressed(None)

    def failed_popup(self):
        popup_layout = GridLayout(rows = 2)
        popup_layout.add_widget(Label(text='Invalid Username / Password'))

        close_popup = Button(text = "Close")
        popup_layout.add_widget(close_popup)

        invalid_login_popup = Popup(title='Error', content=popup_layout, size_hint=(.3, .3))
        close_popup.bind(on_press=invalid_login_popup.dismiss)
        invalid_login_popup.open()
