# encapsulation
# archiving encapsulation by private 
class A: # parent calss 
    def __init__(self,a) -> None:
        self.__a # the variabe is a private variable 
    def show(self):
        print("private variable :", self.__a) # printing a private varible using function
class B(A): # child class 
    def __init__(self,b) -> None:
        super().__init__(b)
    def show(self):
        print(self.__a)
# creating an object of class B
obj=B(20)
obj.showB()

# archiving encapsulation by protected 
class A: # parent class 
    def __init__(self,a) -> None:
        self._a=a #this variable a is a protected variable 
    def show(self):
        print("protected variable :",self._a)
class B(A): # child class 
    def __init__(self,b) -> None:
        super().__init__(b)
    def showB(self):
        print("variable value :",self._a)
obj=B(30)
obj.showB()

