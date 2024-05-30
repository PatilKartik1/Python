a=int(input("A is: "))
b=int(input("B is: "))
c=int(input("C is: "))
d=int(input("D is: "))

if(a>b and a>c and a>d):
    print("A is big")
elif(b>a and b>c and b>d):
    print("B is big")
elif(c>a and c>b and c>d):
    print("C is big")
else:
    print("D is big")