s=set()
l=[1,2,3,4]
s_from_list=set(l)
#or
#s_from_list=set([1,2,3,4])
print(s_from_list)
# set only contain the unique values
s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.remove(3)
s1=s.union({1,2,3,4})
s2=s.intersection({1,2,3,4,5,6,7,8})
print(s,s1,s2)
print(s1.isdisjoint(s2))

