from getpass import getpass as pas

class User:
    username = ""
    password = ""
    logged = False
    
    def __init__(self, username, password):
        self.username = username
        self.password = password        
    
    def login(self):
        username = input("Enter username: ")
        password = pas("Enter password: ")
        if(self.username == username and self.password == password):
            self.logged = True
            print("login success")
        else:
            self.logged = False
            print("Incorrect credentials")
    def logout(self):
        self.logged = False
        print("Successfully logged out")
    def isLogged(self):
        return self.logged
    
class Details(User):
    def __init__(self, username, password):
        super().__init__(username, password)
    
user1 = Details("admin", "password")

while user1.isLogged() == False:
    user1.login()
    
input()



            