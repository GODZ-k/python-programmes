
   # break statement
for letter in "python":
    if letter == "h":
        #here i am using btreak statement to break execution 
        break
    print("current latter :", letter)
print("bye")

#continue statement
for letter in "python":
    if letter == "h":
        #continue statement will skip "h"
        continue
    print("current letter :",letter)
    print("bye")

    # pass statement
for letter in "python":
    if letter == 'h':
        pass
        print("pass block")
    print("current letter:", letter)
print("bye")