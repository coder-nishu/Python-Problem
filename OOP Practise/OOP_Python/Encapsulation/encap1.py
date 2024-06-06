class A:
    def __init__(self):
        self.__c = 6
        self.__d = 3
    def setc(self,newc,newd = None):
        self.__c = newc
        self.__d = newd
    def getc(self):
        return self.__c
    # def setD(self,newD):
    #     self.__d = newD
    def getD(self):
        return self.__d

class B(A):
    def display(self):
        n1 = A.getc(self)
        n2 = A.getD(self)
        print(n1 + n2)  # type: ignore
        
        
A1 = A()
print("before set:")
print(A1.getc())
print(A1.getD())

A1.setc("10")
print("After set:")
print(f"{A1.getc()}")

# class newClass:
#     def __init__(self):
#         A2 = A()
#         self.c = A2.getc()
#         self.D = A2.getD()
    
# N = newClass()
# print(N.c)
