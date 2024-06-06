class vehicle:
    def __init__(self,M_name,model,color):
        self.__M_name = M_name
        self.__model = model
        self.__color = color
    def set_Mname(self,newM):
        self.__M_name = newM
    def get_Mname(self):
        return self.__M_name
    
    def set_model(self,new_model):
        self.__model = new_model
    def get_model(self):
        return self.__model
    
    def set_color(self,color):
        self.__color = color
    def get_color(self):
        return self.__color
    
    def displayinfo(self):
        print(f"Model name: {self.get_Mname()}\nmodel name: {self.get_model()}\ncolor: {self.get_color()}")

class car(vehicle):
    def __init__(self,M_name,model,color,cartype):
        super().__init__(M_name,model,color)
        self.__cartype = cartype
    
    def set_cartype(self,cartype):
        self.__cartype = cartype
    def get_cartype(self):
        return self.__cartype
      
    def displayinfo(self):
        super().displayinfo()
        print(f"{self.get_cartype()}")

v1 = vehicle("BMW","Xseries","black")
bmw = car("BMW","Xseries","black","4 wheel")
bmw.displayinfo()
   