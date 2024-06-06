class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)

x = person("Abid","nishat")
x.printname()

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.bornyear = year
    def printname(self):
        print(self.firstname,self.lastname,self.bornyear)
    
x1 = student("nishat","khan",2002)
x1.printname()