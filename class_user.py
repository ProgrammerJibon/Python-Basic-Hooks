class User:
    username = ""
    password = ""
    logged = False
    
    def __init__(self, username, password):
        self.username = username
        self.password = password        
    
    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
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
    
user1 = User("admin", "password")

while user1.isLogged() == False:
    user1.login()
    
input()


        
            
            