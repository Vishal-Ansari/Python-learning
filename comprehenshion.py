# ls=[]
# for i in range (100):
#     if i%3==0:
#         ls.append(i)

# print(ls)        

# now comprehensive method will be..

ls=[i for i in range(100) if i%3==0]
print(ls)

# now dictionary comprehenshion
dict={i: f"item{i}"  for i in range(1,10)}
print(dict)

# reversiong of dictionary key to value or value to key
dict1={value:key for key,value in dict.items()}
print(dict1)

# ek acha method copied items ek baar lene k lie..
dresses={dress for dress in ["dress1","dress2","dress2","dress1","dress2","dress1"]}
print(dresses)

### list k lie []  , dictionary k lie {},,  generators k lie () use hote h...
# now comprehenesion in genereators

even=(i for i in range(20) if i%2==0)
print(type(even))

for item in even:
    print(item)