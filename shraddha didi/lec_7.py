#f = open("practice.txt","w+")
# read

# data=f.read()
# print(data)

# line1 =f.readline()
# print(line1)

# line1 =f.readline()
# print(line1)

# print(type(data))

#write

#f.write("abc")
#print(f.read())
#f.write("abc")
#f.close()


with open("practice.txt", "r") as f:
    data=f.read()
    print(data)
    
with open("practice.txt", "w") as f:
    f.write("New Data")
    
import os
os.remove("practice.txt")    