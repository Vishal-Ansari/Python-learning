# f=open("m.txt","r")
# content=f.read()
# print(content)

# count=0
# for i in f:
#     if i==" " or i=="\n":
#         count=count+1
# print(count)

# f.close


#question 2
#vishal ansari
file = open("m.txt", "r")  
count=0
      
#Gets each line till end of file is reached  
for line in file:  
     
    words = line.split(" ");  
    
    count = count + len(words);  
   
print("Number of words present in given file: " + str(count-1));  
print("vishal ansari section N 200111238")
file.close();  