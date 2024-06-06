class studentmanagement:
    def __init__(self,name,id,email):
        self.name = name
        self.id = id
        self.email = email
    def getStudentinfo(self):
        return self.name + self.id + self.email
    
    def courseinfo(self):
        print("course information")
    def results(self):
        print("results is uploading")

class administrator:
    def __init__(self,accounts):
        self.__accounts = accounts
    def setAccounts(self,newaccount):
        self.newaccount = newaccount
    def getAccount(self):
        return self.newaccount
    def getStudeninfo(self):
        return "fetching student info"
    def examInfo(self):
        return "fetching exam routine for students"
    def accountsledge(self):
        return "All acount info"

class ExamController(administrator):
    def __init__(self,accounts,cgpa,duration):
        super().__init__(accounts)
        self._cgpa = cgpa
        self.__duration = duration
    
    def __results(self):
        return "only access people will see results"
    def results(self):
        self.__results()
        
    def __Examdetails(self):
        return "only access people will see results"
    def Examdetails(self):
        self.__Examdetails()
        
class studentinformatgion(administrator):
    def __init__(self, accounts,othersinformation,getothers):
        super().__init__(accounts)
        self.__othersinformation = othersinformation
        self.__getothersinformation = getothers