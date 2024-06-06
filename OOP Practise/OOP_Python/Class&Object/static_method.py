class student:
    @staticmethod #decorator
    def greet():
        print("Hello Everyone.")
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id
        
class studymaterial(student):
    def __init__(self, name, id,book_subject) -> None:
        super().__init__(name, id)
        self.booksub = book_subject
    def displayinfo(self):
        print(self.name)
        print(self.id)
        print(self.booksub)
nis = studymaterial("Nishat","5586","physics")
nis.name = "Nirob"
nis.greet()
nis.displayinfo()
# del nis --> it will delete nis object
# nis.displayinfo()