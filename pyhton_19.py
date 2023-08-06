# creating a dictionary
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("dictionary :",d1)
# check datatype of dictionary
print(type(d1))

# storing a list into dictionary in a single key
d2={1:"python",2:"java","fruit":["apple","orange","mango"]}
print(d2)
print(type(d2))

# tuple into dictionary store 
# storing a tuple into dictionary an a single key
d3={1:"python",2:"java","language":("java","pyhton","php")}
print(d3)

# access the value of dictionary 
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
# access the value using key 
x=d1[3]
print(x)
# get(): access the value using get method
y= d1.get(1)
print(y)
# item(): access the value using item method 
z=d1.items()
print(z)

# change the value 
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
d1[3]="kivi"
print("upadted dictionary :",d1)

# update(): upadte the dictionary by using upadte method 
print("current dictionary :",d1)
# update(); upadte dictionary by using update method 
d1.update({2:"banana"})
print("updated dictionary :",d1)

# remove values from dictionary 
# pop(): using pop method 
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
d1.pop(2)
print("updated dictionary :",d1)

# using popitem():
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
d1.popitem()
print("updated dictionary :",d1)

# del(): using del method
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
del d1[2] # delete second item using del method
print("upadted dictioanry :",d1)

# clear(): using clear method
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
d1.clear()
print("updated dictionary :",d1)

# access the only keys from dictionary
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
k=d1.keys() # keys(): display the only keys of the dictionary using keys method
print("keys :",k)

# access the only values from dictionary
d1 = { 1:"apple",2:"mango",3:"orange",4:"apple"}
print("current dictionary :",d1)
v=d1.values()
print("values :",v)