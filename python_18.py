# create tuple

t1=("apple","orange","cheery",1,2,3,4,5,1,2,3,4,5)
print("current tuple :",t1)

# how to check the length of tuple
t2=(1,2,3,4,5,6,7)
print("lenght :",len(t2)) #checking the length of tuple by using len()

# indexing/ slicing
t1=("apple","orange","cheery",1,2,3,4,5,1,2,3,4,5)
print("current :",t1)
# accessing the value by using index
print("index 1 value :",t1[1])
# accessing the value between index 1 to 6
print("index between 1 to 6 :",t1[1:6])
# access the value from last into tuple
print(" last value :",t1[-1])
# access the value till index 6
print(" value till index 6 :",t1[:6])


# convert tuple into list 
t1=("apple","orange","cheery",1,2,3,4,5,1,2,3,4,5)
print(" current tuple :",t1) #  before change
x=list(t1) # list(): to convert tuple into the list 
print(" updated tuple :",x) # after convert

# tuple constructor
t3=((1,2,3,4)) # note the double round brackets 
print(t3)

# add item but after converting tuple into list
t1=("apple","orange","cherry","mango")
print("current tuple :",t1) # before convert
print(type(t1)) 
x=list(t1) # convert tuple into list
print("list :",x) # after convert
print(type(x))
# add item into list
x.insert(4,"banana")
#x[1]="banana"
print("updated list :",x)
x=tuple(x) # convert list into tuple
print("updated tuple :",x)

# loops with tuple
# for loop with tuple
t5=('apple','mango','orange','banana')
for i in t5:
    print(i)

# while loop with tuple
t5=('apple','mango','orange','banana')
i=0
while i<len(t5):
 print(t5[i])
 i+=1
else:
    print("loop finished")

    # how to compare tuples
    t1=(1,2,3,4)
    t2=(1,2,4,5)
    # tuple is equal to tuple 2
    print(t1==t2)
    # tuple 1 is less then tuple 2
    print(t1<t2)
    # tuple 1 is grater then tuple 2
    print(t1>t2)