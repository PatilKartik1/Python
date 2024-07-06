'''#Q1
def sum(n):
    if(n <= 1):
        return n
    else:
        return  sum(n-1) + n
    

n =int(input("Enter N: "))
sum = sum(n)
print(sum)'''

#Q2

def prin(list,idx=0):
    if(idx == len(list)):
         return
    else:
        print(list[idx])
        prin(list,idx+1)
    
    

 
cities=["delhi", "gurgaon", "noidal", "pune", "mumbai", "chennai"]
prin(cities)