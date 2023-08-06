# file handeling 
# file creating 
# open("file name","permission")
s="this is my file handeling program"
file=open("python_23_file.txt","w")
file.write(s)
print(" your file is created")
file.close()

#file read
file=open("python_23_file.txt","r")
filecontent =file.read()
print(filecontent)

# list store into file 
l1=["1","2","3"]
file=open("demo.txt","w")
file.writelines(l1)
print("file created")
file.close()
 # read demo.txt file
file=open("demo.txt","r")
filecontent=file.readlines()
print(filecontent)

# appending the value into file
s="python file handling"
file=open("demo.txt","a")
file.write(s)
print("file updated")
file.close()
file=open("demo.txt","r")
file=file.read()
print(file)