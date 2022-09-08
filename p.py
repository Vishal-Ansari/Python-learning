list=[]
n=int(input())

for i in range (0,n):
    ele=int(input())
    list.append(ele)

list.sort()
list.reverse()
print(list)