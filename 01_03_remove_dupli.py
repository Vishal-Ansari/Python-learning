#question 3
#vishal ansari
list1=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    list1.append(element)
list2 = set()
unique = []
for x in list1:
    if x not in list2:
        unique.append(x)
        list2.add(x)
print("Non-duplicate items:")
print(unique)
print("vishal ansari  section-N  std-id-200111238")
