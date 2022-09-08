# num=["3","56","65"]

# num=list(map(int,num))
# # for i in range(len(num)):
# #     num[i]=int(num[i])

# num[2]+=1
# print(num[2])    

# def sq(a):
#     return a*a
# ls=[1,2,3,4,5,6,7,8,9,10]    
# square=list(map(sq,ls))
# print(square)

# or

# ls=[1,2,3,4,5,6,7,8,9,10]    
# square=list(map(lambda x:x*x,ls))
# print(square)

# now do multiple function at a time.....

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func=[square,cube]
# n=[1,2,3,4,5,6,7,8,9,10]

# for i in range(5):
#     val=list(map(lambda x:x(i),func))
#     print(val)



# ----------------------FILTER FILTER FILTER FILTER FILTER----------------------------

# numb=[1,2,3,4,5,6,7,8,9,10]
# def is_greater(numb):
#     return numb>5
# gr_than=list(filter(is_greater,numb))    
# print(gr_than)


# ------------------------REDUCE--------------------

from functools import reduce

lst=[1,2,3,4]
num=reduce(lambda x,y:x+y,lst)
print(num)    
# num=0
# for i in lst:
#     num=num+i
# print(num)    

