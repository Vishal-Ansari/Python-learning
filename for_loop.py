# # list1=["vishal","arman","raghav","vaibhav","college"]
# # for items in list1:
# #     print(items)

# list2=[ ["vishal",1],["armaan",2],["raghav",3],["vaibhav",4],["college",0] ]# list of list
# # for item,no in list2:
# #     print(item,no)    

# d=dict(list2)
# print(d)
# for item,no in d.items():
#     print(item,no)

list3=[int,float,"insan","janwar",1,3,5,77,34,5,51235,55,6]
for item in list3:
    if str(item).isnumeric() and item>6:
        print(item)