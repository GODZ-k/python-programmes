# pyhton oops

# how to create a class 
class myclass:
    x=5 # property of class 
print(myclass)


# how to create object
class myclass:
    x=5 # property of class 
# creating abject of myclass 
m1=myclass() # m1 is an object of class myclass
print(m1.x) 

# calling a function by object 
class myclass:
    def myfunction(self): # property of myclass
        print("hello my function")
# creating an object 
m1=myclass()
m1.myfunction()


# how to create constructor 
class myclass:
    def __init__(self) -> None: # self is campulasory # __init__  is a constructor 
        print("hello this is my function")
        # creating an object
m1=myclass()

# change the value by object 
class myclass:
    def __init__(self,name,age):
        self.name=name 
        self.age=age 
    def myfunction(self):
        print("my name is :"+self.name)
# creating an object
m1=myclass("sumit",25)
m1.age
m1.name
# changing the age using object
m1.age=26
print("age :",m1.age)

# delete the object
del m1.age
print("age :",m1.age)