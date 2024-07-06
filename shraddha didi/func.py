'''def avg(a,b,c):
    avg =(a+b+c)/3
    return avg


avg = avg(91,34,77)
print(avg)'''

'''#Q1 & Q2

cities=["delhi", "gurgaon", "noidal", "pune", "mumbai", "chennai"]
heros = ["thor", "ironman", "captain america", "shakiman"]

# def len1(list):
#     print(len(list))
    
def print1(list):
    for i in list:
        print(i,end=" ")
        
print1(cities)'''

'''#Q3

n=int(input("Number: "))

def factorial(n):
    fact =1
    for i in range(1,n+1):
        fact = fact*i
    return fact

facto = factorial(n)
print(facto)'''

'''n = int(input("Number: "))

def calc(n):
    inr = n*83
    return inr

inr = calc(n)
print(n,"USD = ",inr,"INR")'''


#Q4
n = int(input("Number: "))

def oddeven(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd") 
        
oddeven(n)