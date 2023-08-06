 # reverse this program
   # *****                #range ( start point, end point , step(jump))
   # ****
   # ***
   # **
   # *
for i in range(5,0,-1): # why we are use -1 " becouse we are telling to system to decrement the stars(*) to one "
    for j in range(i):    # we also use this function in increment but they don't need this . that's  why we didn't use . but you use when you wish .
         print("*",end="")
    print()  