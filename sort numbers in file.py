# file = open("a.txt","r")
# content=file.read()

# list=content.split(" ")
# list.sort()
# print(content)
# print(list)
# f=open("a.txt","w")
# b=f.write(str(list))
# print(b)

# file.close()

wee_days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("day"+(" "*12)+ "high temperature")
print("_ "*30)
temperature=[]
temp=0
spaces=0
for i,x in enumerate(wee_days):
    temp_input=input("enter the TEMPERATUR FOR" + x + str(":"))
temperature.append(int(temp_input))
spaces=15-len(x)
print(x," "*spaces,temperature)
avg=sum(temperature)//len(wee_days)
print("the average is",avg)