# import random variable 
# from random import functionname
#  import random

# choice() function
from random import choice

l1=[1,2,3,4,5,6]
print(choice(l1))

# randint() function

from random import randint
otp=randint(100,993)
print("your otp no is :",otp)

# shuffle() function
from random import shuffle
l2=["apple","banana","mango"]
shuffle(l2)
print(l2)