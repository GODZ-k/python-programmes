# single inheritance 
class parentclass:
    def myfunction(self): # parent class property
        print("my first class is this ")
class childclass(parentclass): # child class which inherit parent class 
    def myfunction1(self):  # child class property
        print("child class function called ")
# creating an object of childclass
c1=childclass()
c1.myfunction()
c1.myfunction1()

# multilevel inheritance 
class parentclass: # parent class 
    def myfunction1(self):
        print("hello parentclass")

class subparentclass(parentclass): # sub parent class 
    def myfunction2(self):
        print("hello subparent class")
class childclass(subparentclass): # clild class 
    def myfunction3(slef):
        print("hello child class")
m1=childclass()
m1.myfunction1()
m1.myfunction2()
m1.myfunction3()

# multiple inheritance
class parentclass:
    def function(self):
        print(" parent class ")
class parentclass1:
    def function2(self):
        print(" parent class 2 ")
class childclass(parentclass,parentclass1):
    def myfunction3(self):
        print(" child class")
    # creting an object of child class 
m1=childclass()
m1.function()
m1.function2()
m1.myfunction3()

# hierarchical inheritance
class parentclass:
    def function(self):
        print("this is my first parent class")
class childclass(parentclass):
    def function1(self):
        print("this is my child class ")
class subchildclass(parentclass):
    def function2(self):
        print("this is my subchild class ")
        # creating 2 object 1 for childclass and 2 for subchildclass
m1=childclass()
m2=subchildclass()
m1.function() # function of parent class
m1.function1() # function of child class 
m2.function() # function  of parent class
m2.function2()# function of subchild class

# hybrid inheritance 
class parentclass:# parent class 
    def myfunction(self):
        print("function of parent class")
class childclass1(parentclass): # child class
    def myfunction1(self):
        print("function of childclass1")
class childclass2(parentclass): # child class
    def myfunction2(self):
        print("function of childclass2")
class childclass3(childclass1,childclass2): # child class
    def myfunction3(self):
        print("function of childclass3")
# creating an object of childclass3
m1=childclass3() #object of childclass3
m1.myfunction()
m1.myfunction1()
m1.myfunction2()
m1.myfunction3()



