import datetime
class DataBase:
    def __init__(self,filename):
        self.filname = filename
        self.users = None
        self.file = None
        self.load()
    def load(self):
        self.file = open(self.filname, "r")
        self.users = {}

        for line in self.file:
            email,password,name,created = line.strip().split(",")
            self.users[email] = (password,name,created)    
        self.file.close()
    def get_user(self,email):
        if email in self.users:
            return self.users[email]
        else:
            return -1    


    def add_user(self,email,name,password):
        if email.strip() not in self.users:
            self.users[email.strip] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1
    def validate (self,email,password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False    

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

