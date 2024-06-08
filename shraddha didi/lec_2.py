
str1="Kartik"
str2='Anil'
str3="""Patil""" 
str4="My name is kartik Patil.\nI study in bjs callege"

con=str1+str2+str3
print(str4) 
print(con)

#INDEXING

len1=len(str1)
len2=len(con) 

print(len1)
print(len2) 

ch =str1[4]

print(ch)

#string cannot be updated/manipulated

#SLICING(ACCESING PART OF STRING)

print(str1[1:4])
print(str1[0:len(str1)])

#rev slicing

print(str1[-3:-1])

#str funtions
str5="i am coder"

print(str5.endswith("r"))
print(str5.capitalize())
print(str5)

print(str5.replace("o","a"))
print(str5.replace("coder","playboy"))

print(str5.find("q"))

print(str5.count("a"))






 