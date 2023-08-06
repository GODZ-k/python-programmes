# creating a list 
# this list is store the integer values 
l1 =[1,2,3,4,5,6,7]
# this list store the string values
l2 =["mango","apple","orange"]
print("integer list: ",l1)
print("string list :",l2) 

# dulpicate values in list
l1=[1,2,3,4,5,1,2,3,4,5]
print("duplicate values:",l1) 

# list constructor
l1=list(("apple","mango","orange")) # note there is double brackets
print(l1)

# list slicing 
l1=[1,2,3,4,5,6,7,8,9,10] # the indexing of the list runs from 0.
print("current list :",l1)
# access the value of intex 1 
print("index 1 value :",l1[1])
# access the value between index 1 to 6
print(" index between 1 to 6 :",l1[1:6])
# access the value till index 6
print(" index till 6 :",l1[:6])
# access the last value of list
print("last value of the list :",l1[-1])

# list item change
x =["apple","bannan","cherry","orange"]
print("current list :",x)
# change the value into the list
x[1:3]=["graps","watermelon"]
print("updated list :",x)

# insert into list 
l1=[1,2,3,4,5,6]
print(" current list :",l1)
l1.insert(2,"python") # updating the list using insert method
print("updated list :",l1)

# extend the list 
l1=[1,2,3,4,5]
l2=['a','b','c','d','e']
l1.extend(l2) #extending the list of l2 into list of l1
print(" extended list :",l1)

# remove items from list 
# remove(): this methid is used to remove elements from list
l1=[1,2,3,4,5,6,7]
print("current list :",l1)
l1.remove(2) # removing the item using remove method
print("updated list :",l1)

# pop(): this methid is used to remove last value from list
l1=[1,2,3,4,5,6]
print("current list :",l1)
l1.pop() # remove item using pop method
print(" updated list :",l1)

# del(): this method is used to remove item from the index
l1=[1,2,3,4,5,6]
print("current list :",l1)
del l1[2] # remove item using del method
print("updated list :",l1)

# clear(): this method is used to clear list
l1=[1,2,3,4,5,6]
print("current list :",l1)
l1.clear()
print("updated list :",l1)