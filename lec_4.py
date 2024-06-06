'''#Dictionary

info={
    "name": "Kartik",
    "Subjects": ["Python","C","java"],
    "Topics": ("Dictionaries","Sets"),
    "age" : 20,
    "is_adult" : True,
    "Marks" : 94.4
}

print(info)  
print(info["name"])
print(info["Subjects"])

info["name"] ="Priyanka"
info["surname"] ="Ganguly"
print(info["name"])

print(info)'''


'''#Null Dictionary

Null_dict = {}
Null_dict["Name"] = "Kartik"
print(Null_dict)

#Nested dictionary
student= {
    "name": "kartik",
    "subject": {
        "phy":97,
        "chem" :98,
        "Maths" : 95
    }
 }

print(student)
print(student["subject"])
print(student["subject"]["chem"])


#Dictionary Methods

print(len(student))
print(list(student.keys()))


print(student.values())


print(student.items())

pairs= list(student.items())
print(pairs[0])

#print(student["name2"]) //error message
print(student.get("name2"))
print("hii")    
print("Welcome to")
print("Apna cklg")

new_dict={"name":"Priyanka","age":16}
student.update(new_dict)
print(student)'''


#SETS

'''collection ={1,2,2,2,4,"hello","world","world"}

print(collection)
print(type(collection))
print(len(collection))'''


'''#Empty set

collection = set()
 
# print(collection)
# print(type(collection))

#Set Methods
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hello")
collection.add((1,2,3))
#collection.add([1,2,3]) #error


print(collection.pop())

collection.remove(2)

collection.clear()
print(collection)
print(len(collection))'''

#union

set1 ={1,2,3}
set2=(2,3,4)

print(set1.union(set2))
print(set1)
print(set2)


print(set1.intersection(set2))


