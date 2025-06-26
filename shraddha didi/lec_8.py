class Student:
    college_name="BJS"  #Class attribute
    def __init__(self,name,marks):
        self.name=name #obj attribute
        self.marks=marks
        #print("adding new student to database")
        
    def welcome(self):
        print("Welcome student",self.name)
        
    def get_marks(self):
        return self.marks
    
    
s1=Student("Karan",97)
s1.welcome()
print(s1.get_marks())
# print(s1.name,s1.marks)
 
# s2=Student("Arjun",88)
# print(s2.name,s2.marks)
# print(s2.college_name)

# s2=Student()
# print(s2.name) 

# class Car:
#     color="red"
#     brand ="mercedes"
    
# Car1 =Car()
# print(Car.color)
# print(Car.brand)