#navigation between multiple screens
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



#first screen
class MainWindow(Screen):
    pass
#second screen
class SecondWindow(Screen):
    pass
#for transition between sreens
class WindowManager(ScreenManager):
    pass
#Reading from a specific .kv file regardless of its name
kv = Builder.load_file("app.kv")

class MyMainApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()
