'''Function definitions
def sum(a,b):  #Function parameters
    return a+b

sum = sum(2,81)  #Function call(argument1,argument2)
print(sum)'''


'''def print1():
    print("Hello world")
    
    
print1()
print1()
print1()'''


'''#Built in functions

print("Kartik",end="$")
print("Patil")'''


'''def prod(a=5,b=5):
    prod=a*b
    return prod

prod = prod(9,2) 
print(prod)'''


#RECURSION

'''def show(n):
    if(n == 11):
        return
    print(n)
    show(n+1)
    print("End")
    
show(1)'''

#Factorial of numbers  by recursion

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return fact(n-1) *  n
    
n=int(input("Enter n: ")) 
fact = fact(n)
print("factorial of",n,": ",fact)
