from re import I


def fibRecursion(n):
    if n<=1:
        return n
    else:
        return(fibRecursion(n-1)+fibRecursion(n-2))
x=int(input("enter the item "))
if x<=0:
    print("no is not valid")
else:
    print("fibonacci sequence :")
    for i in range(x):
        print(fibRecursion(i))

# program 1
for i in range(1,6):
    for j in range(i):
        print("*" , end=" ")
    print()
for a in range(6,0,-1):
    for b in range(a):
        print("*", end=" ")
    print()


#x=int(input("enter the no :"))   
x=1
for i in range(1,6):
    x=1
    for j in range(i):
     print(x,end=" ")
     x+=1
    print()