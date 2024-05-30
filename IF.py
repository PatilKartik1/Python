'''a=int(input("enter a: "))
b=int(input("enter b: "))

if(a>=b):
    print("True")
else:
    print("False")'''
    
# marks=int(input("enter marks: "))

# if(marks >=90):
#     grade ="A"

# elif(marks >= 80 and marks < 90):
#     grade ="B"
    
# elif(marks >= 70 and marks <80):
#     grade ="C"
# else:
#     grade ="D"
    
# print("grade: ",grade)

#nested if else
age=int(input("enter age: "))

if(age>=18):
    if(age>=80):
        print("Cannot drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")