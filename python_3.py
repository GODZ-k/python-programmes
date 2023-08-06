 #nested for loop
   # *                 #range ( start point, end point , step(jump))
   # **
   # ***
   # ****
   # *****
for i in range(1,6,1): # we write the end point with one increment of the range of i ( start point , end point ) acctual end point is 5 but we write 6
    for j in range(i):
     print("*",end="")
    print()

                    