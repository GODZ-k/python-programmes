# write the program to find out the grade of given percentage value ( accept from the user ) and print the message according given cretia 
# grater then 70% print A grade message to the user 
# grater then 65% and less then 70% print B+ grade message to the user 
# grater then 60% and less then 65% print B grade message to the user 
# grater then 55% and less then 60% print C grade message to the user 
# less then 55%  print fail message to the user
x=int(input("enter the percentage that you have: "))
if x>=70:
    print("A grade ")
elif x>=65 and x<70:
    print("B+ grade")
elif x>=60 and x<65:
    print("B grade ")
elif x>=55 and x<60:
    print("C grade")
else:
    print("fail")
           