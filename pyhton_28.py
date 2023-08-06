# method overloading
class mo:
    def myfunction(self): # no arguments
        print("function with no argument ")
    def myfunction(self,a): # 1 arguments 
        print("function with 1 arguments ")
    def myfunction(self,a,b): # 2 arguments
        print("function with 2 arguments")
m=mo()
m.myfunction(10,20)
# note: method overloading is not supported in python language becouse python is a interpeted language

# method overriding
class a1: # parent class
    def myfunction(self,a):
        print("class a1 function called ")
class a2(a1): # child class 
    def myfunction(self,a):
        print("class a2 function called ")
        super().myfunction(10)
class a3(a2): #child class 
    def myfunction(self,a):
        print("class a3 function called ")
        # super method calling the method of class a2
        super().myfunction(10)
    # creating an object of class a3
m=a3() # object of a3
m.myfunction(10)

