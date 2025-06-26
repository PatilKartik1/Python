#with open("practice.txt","r") as f:
  #f.write("Hii everyone\nwe are learning File I/O\n")
  #f.write("using Java.\nI like programming in Java.")
  #data=f.read()
  
  #new_data=data.replace("Java", "Python")
  #print(new_data)
  
#with open("practice.txt","w") as f:
   # f.write(new_data)
    
# def word_check():
#  word ="learning"
#  with open("practice.txt","r") as f:
#     data=f.read()
#     if(word in data):
#         print("Found word")
#     else:
#             print("No word found")
            
            
# def check_for_line():
#     word="programmingx"
#     data =True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while True:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no +=1
            
#     return -1

# check_for_line()


count =0
with open("practice.txt","r") as f:
    data=f.read()
    # print(data)
    
    # num =""
    # for i in range(len(data)):
    #     if(data[i]==","):
    #         print(int(num))
    #         num=""
    #     else:
    #         num=num+data[i]
    
    nums =data.split(",")
    for val in nums:
        if(int(val)%2==0):
            count +=1
            
print(count)