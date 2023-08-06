# exceotion creating 


a=int(input("enter the value of a:"))
print(a) # we got a wrong input by the user 
print("bye")

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=a/b # exception occur on runtime becouse division by zero 
print("answer :",c) # we divide 10 into 0 becouse zero doesn't divide any number 
print("bye")

try:       # the code which is written try block can be occur error at runtime
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))

    c=a/b

    print("answer :",c)
except Exception as e:
# this block will run when the error will occur
   print("exception occur:",e)

print("bye")

# many exception
try:
    # we have not define variable m
    print(m)
except NameError:
    print("variabe is not define")
except:
    print("exception caught")   



# how to use else with except 
try:
    print("hello")
except:
    print("something went wrong ")
else:
    print("nothing went wrong")



#  finally block 
# the block which run compulsory if error occur or not 
try:
    print("hello")
   # print("k")
except:
    print("something went wrong")
finally:
    print("finally block")


# user define exception
class MyException(Exception):
    pass
c=2
if c>5:
    raise MyException("bro something went wrong")
