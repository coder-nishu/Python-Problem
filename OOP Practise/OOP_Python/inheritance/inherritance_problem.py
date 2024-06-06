
class user:
    def __init__(self,userid,password,login,register):
        self.userid = userid
        self.password = password
        self.login = login
        self.register = register
        
    def verifylogin(self):
        print(f"your UserID:{self.userid}\npassword:{self.password}")
class administrator(user):
    def __init__(self,userid,password,login,register,AName,email):
        super().__init__(userid,password,login,register,AName,email)
        self.Aname = AName
        self.email = email
    def updatemenu():
        print("you can update anything")
        
class Customer(user):
    def __init__(self, userID, password, CName, address, email) -> None:
       super().__init__(userID, password)
       self.__CName = CName
       self.__email = email
       self.__address = address
    
    def register(self):
        print(f"youre registered {self.__userid}")
        
nishat_customer = Customer("221","5586","nishat","kazipara","gmail")
nishat_customer.register