# match function 
from ast import pattern
import re
import sunau 
pattern = r"^abcd"
mystring ="abcdef"
x=re.match(pattern,mystring)
print(x)

# search function 
import re
txt="we are learning python"
x=re.search("\s",txt) # this expression is written for searching whitespace
print("the first whitespace :",x.start())


import re
txt="the rain in ahmedabad"
x=re.search("ahmedabad",txt)
print(x)

import re
str1="learnvern provide free online training"
print("before replace :",str1)

# after replace the provide with python 
result=re.sub(r"provide","python",str1)
print("after replace :",result)

import re
str1="Learnvern Provide Free Online Training"
print("before replace :",str1)
 # after replace 
result=re.sub(r"[a-z]","0",str1)
print("after replace :",result)