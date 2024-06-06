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
        super().__init__(userid,password,login,register)
        self.Aname = AName
        self.email = email
    def updatemenu(self):
        if self.Aname == "Nishat" and self.password == "Nishat123":
            print("You can update system menu.")
        else:
            print("you have no access in system.")
        
class Customer(user):
    def __init__(self,userid,password,login,register,CName,address,email) -> None:
       super().__init__(userid,password,login,register)
       self.CName = CName
       self.address = address
       self.email = email
    
    def register1(self):
        print(f"your registered name is: hafiz")
       
    
    def login(self):
        if self.userid == "5678" and self.password == "221":
            print("youre verifier")
        else:
            print("password errror or please register.")
            
    def update(self):
        if self.email == "hapi@gmail.com" and self.password == "221":
            print("youre verifier")
        else:
            print("password errror or please register.")
        

N1 = Customer("5678","123","hafiz","ANJUM","hafizur rahman","khagan","hapi@gmail.com")
nishat = administrator("5586","Nishat123","Nishat","Khagan","Nishat","nishat@gmail.com")
N1.register1()
nishat.updatemenu()