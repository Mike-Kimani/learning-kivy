from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from database import DataBase

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != " " and self.email.text != " " and self.email.text.count("@") ==1 and self.email.text.count(".")>0:
            if password != " ":
                db.add_user(self.email.text, self.namee.text, self.password.text)
                self.reset()
                sm.current = "login"
            else:
                invalid_form()
        else:
            invalid_form()        

    def login(self):
        self.reset()
        sm.current = "login"
    def reset(self):
        self.email.text = ""
        self.namee.text = ""
        self.password.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text,self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalid_login()


        
    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""    


class MainWindow(Screen):
    n = ObjectProperty(None)
    email = ObjectProperty(None)
    created = ObjectProperty(None)  
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, **args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " +created    

class WindowManager(ScreenManager):
    pass 

def invalid_login():
    pop = Popup(title= 'Invalid login', content = Label(text = 'Invalid email or password'),size_hint = (None, None), size =(400,400))
    pop.open()

def invalid_form():
    pop = Popup(title= 'Invalid form', content = Label(text = 'Please fill all required fields with valid information'),size_hint = (None, None), size =(400,400))
    pop.open()

sm = WindowManager()
db = DataBase("users.txt")     

kv = Builder.load_file("cred.kv")    

screens = [LoginWindow(name = "login"), CreateAccountWindow(name = "create"), MainWindow(name = "main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyApp().run()