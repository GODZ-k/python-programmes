# write a program to print following pattern 
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()