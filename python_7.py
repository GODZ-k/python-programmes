# how to use string in python
#single quote string
print('hello world')
print("hello world")

# multi line string
a="""pyhton is booming in the market ,
python is smart language , 
pyhton used in AI , machine learning , data science"""
print(a)

# update string
a="hello world!"
print(a)
print("update string :" , a[:6]+"python")
# string slicing
a ="hello world"
# access the value of index 1
print("index 1 :" , a[1])
# acess value between under 1 to 6
print("index 2 :", a[1:6])
# access the value till index 6
print("index 3 :", a[0:6])
# access the last value from string 
print(" index 4 :", a[-1]) # print("index : ",a[10:11]) 

# string in - built methods
# capitalize():this method converts the first character in string
a ="hello and welcome to learnvern "
x =a.capitalize()
print(x)

# casefold(): this method converts all capital letter into small
a="Hello Welcome to Learnver"
x=a.casefold()
print(x)

# center(): this is use to bring your into center
a = "python"
print(a)
x =a.center(20)  # update using center method 
print(x)

#count(): this method is used to count the repeated word in string 
a=" python is a booming method used in all over the world"
x =a.count("python")
print(x)

# how to compare string 
str1="learnvern"
str2="learnvern"
result = str1==str2
print(result)

str1="learnvern"
str2="python"
result =str1==str2
print(result)

sre1='a'
str2='b'
str3='c'
result = str1>str2
print(result)