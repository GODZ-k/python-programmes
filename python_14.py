# write a program to print following pattern
# 1
# 12
# 123
# 1234
x=1
for i in range(1,5):
    x=1
    for j in range(i):
        print( x, end="")
        x+=1
    print()
