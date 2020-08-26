import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
#from kivy.lang import Builder

class Widgets(Widget):
    def btn(self):
        show_popup()

        
class P(FloatLayout):
    pass
class MaApp(App):
    def build(self):
        return Widgets()

def show_popup():
    show = P()
    popupWindow = Popup(title="Popup Window", content = show, size_hint = (None,None), size= (200,200))
    #size_hint places the pop up while size determines the size of the popup
    popupWindow.open()

if __name__ == "__main__":
    MaApp().run()
