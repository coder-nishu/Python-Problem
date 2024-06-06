class car:
    def __init__(self) -> None:
        self.accelarator = False
        self.brk = False
        self.cluth = False
    def start(self):
        self.accelarator = True
        self.brk = True
        print("car is startting...")
    

bmw = car()
bmw.start()  #just i hide how start is performing