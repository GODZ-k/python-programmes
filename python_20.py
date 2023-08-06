# in build function
# print()
# range() function
for i in range(1,10,1):
 print(i)
 # round() function
 x=round(2.110292,2)
print(x)
# user define function
# create function
def myfunction():
    print("hello")

# calling a function
myfunction()
# funtion with one arguments
# creting a function
def myfunction(a):
    print("A :",a)
# calling the function
myfunction(10) # passing argument as a 10

# multiple argument into function
# creating a function
def myfunction(a,b):
    print("A :",a)
    print("B :",b)

# calling a function
myfunction(10,20)  # passing 2 arguments

# keys arguments
# creating a function
def myfunction(child3,child2,child1):
    print(" youngest child is :"+child1)

# calling a function
myfunction(child1="ritesh",child2="ram",child3="geeta")

# default parameter value 
# creating a function
def myfunction(state="gujarat"):
    print("i am from :"+state)

# calling a function
myfunction("rajasthan")
myfunction("meerut")
myfunction("delhi")
myfunction()

# passsing a list into function
# creating a function
def myfunction(fruit):
    for i in fruit:
        print(i)
f=["apple","mango","orange"]
# calling a function
myfunction(f)

# return values from function
# creating a function
def  myfunction(x):
    return 5*x
# calling a function
print(myfunction(3))
print(myfunction(6))
print(myfunction(4))

# recursion function
# the function which call itself
# creating a function
def factorial(x):
    if x==1:
        return 1
    else:
        # calling recursion function
        return(x*factorial(x-1))
num=int(input("num :"))
print(" the factorial of ",num,"is :",factorial(num))

# anonymous function(lambda function)
# creating a function
x=lambda a: a+10
print(x(5))

# lambda function with multiple arguments 
y= lambda a,b:a*b
print(y(5,5))

# global variable 
# global variable means the variable can be use anywhere in the program 
z=25 # global variable 
def myfunction():
    global z
    print(z)
    z=20
myfunction()
print(z)

# local variable 
# the variable which can be used in it scope
def sum(x,y):
 sum=x+y
 return sum
print(sum(5,10))
print(x) # variable x is a local variable 
