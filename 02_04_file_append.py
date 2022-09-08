# question 4
# vishal ansari

f=open("apend.txt","w")
print("enter the string ")
a=input()
f.write(a)
f.close()
f1=open("apend.txt","r")
content=f1.read()
print("the content printed in file is:-")
print(content)
print("vishal ansari secction N 200111238")
f1.close()