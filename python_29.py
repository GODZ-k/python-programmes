# abstraction 
from re import L


class RBI: # abstract class 
    def intrest(self): # abstract method 
        pass
class SBI(RBI): # child class
    def intrest(self):  # RBI intrest implements here 
        print("SBI intrest is  5%")
class HDFC(RBI): # child class
    def intrest(self):  #RBI intrest implements here
        print("HDFC intrest is 2%")
# creating an object of class of SBI
s=SBI()
# creating an object of class HDFC
h=HDFC()
s.intrest() # SBI intrest method called
h.intrest() # HDFC intrest method called 


# examlpe 2
class animal:
    def move(self):
        pass
class dog(animal):
    def move(self):
        print("dogs are animal")
class tiger(animal):
    def move(self):
        print("tiger is also an animal")
d=dog()
t=tiger()
d.move()
t.move()