import datetime
class DataBase:
    def __init__(self,filename):
        self.filname = filename
        self.users = None
        self.file = None
        #self.load()
    def load(self):
        self.file = open(self.filname, "r")
        self.users = {}

        for line in self.file:
            email,password,name,created = line.strip().split(",")
            self.users[email] = (password,name,created)    
        self.file.close()
    
    def add_user(self,email,name,password):
        if email.strip() not in self.users:
            self.users[email.strip] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1     
    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

