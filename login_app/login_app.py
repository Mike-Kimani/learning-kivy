from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import DataBase

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

class MainWindow(Screen):
    n = ObjectProperty(None)
    email = ObjectProperty(None)
    created = ObjectProperty(None)    
    