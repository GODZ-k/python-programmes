from math import dist
from operator import truediv
from re import S, X
from tkinter import Y
from typing import List


a = 20
print(type(a))
b="tanmay"
print(type(b))
# complex number
c=2+4j
print(type(c))

d=True
print(type(d))

#set datatype 
e={'a','b','c'}
print(type(e))

f={a,b,c}
print(type(f))
#dictionary

q={'key':'value'}
print(type(q))
#list datatype
l1=[1,2,3,4,5]
print(type(l1))
# string datatype
y= "python program"
print(type(Y))
#tuple variable
z=(1,2,3,4,5)
print(type(z))
#variable
x="python"
y="programming"
z=x+y
print(z)
#type conversion
# converting from one datatype to another datatype 
# is called type conversion/type casting
a=int(input("enter the value of A:"))
print("A :",a)
print(type(a))
#arthmetic operator 
a=12
b=32
c=a+b
print("Answer :",c)
# assignement operator
x=5
x+=5 # x=x+5
print("Answer :",X)
#comparision operator
x=1
y=2
print(x==y)
#logical operator
x=5
print(x>3 and x<5)
#identity operator 
x=["mango","banana"]
y=["mango","banana"]
z=x
print(x is Y)
print( x is z)
#membership operator 
x=["mango","banana"]
print("banana" in x)
print("graps" in x)

# operator precedence
a=2
b=3
c=23
d=3
x=(a+b)+c**b//d*c
print("value of x :",x)
# condition statement
# simple if 
var=10
if(var==10):
    print("value of avriabe is 01")
    print("bye")
    # if_else statement
    a= int(input("enter the no of a:"))
    b=int(input("enter the no of b:"))
    if a>b:
     print("b is greater")
    else:
        print("a is greater")
        #if_else_ladder statement
        #1) percentage greater than 70== dist
        # 2) percentage greater or equalto 65 and less than 70 == 1st calss
        # 3) percentage greater or equalto 60 and less than 65 == 2nd calss
        # 4) percentage greater or equalto 55 and less than 60 == 3rd calss
        #5) percent#age below 55 == fail
        p=int(input("enter the percentage :"))
if p>=70:
        print(" dist")
elif p>=65 and p<70:
        print("1st class ")
elif p>=60 and p<65:
        print(" 2nd class ")
elif p>=55 and p<60:
        print(" 3rd class ")
else:
        print("fail")      

        #nested if satement

 # 1) Age >=18
 # 2) weight>=50
 # 3) if both age and match with criteria then the user can donate the blood
 # 4) if age is less than 18 show one msg under age 
 # 5) if weight is less than 50 show one msg under weight
 # 6) if age does not match then is should ask for weight 

age= int(input( " enter your age :"))
if age>=18:
   weight= int(input(" enter your weight :"))
   if weight>=50:
      print(" blood donate")  
   else:
      print(" under weight") 
else:
    print(" under age ")
 # loop statements
 # while loop 
 # 5,9,12,14,15
sum=0
n= int(input("enter the value of n: "))
while n>0:
 sum=sum+n
 n-=1 # n=n-1
 print("sum :" , sum)
print("bye")
# while loop with else part 
sum=0
n= int(input("enter the value of n: "))
while n>0:
 sum=sum+n
 n-=1 # n=n-1
 print("sum :" , sum)
else:
        print(" loop finished ")
print("bye")