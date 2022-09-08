import math

me="vishal"
c=786
# a=" my name is %s"%me
# a=" my name is %s %s"%(me,c)
a=" this is {1} {0}"
# print(a)
b=a.format(me,c)
print(b)



# F strings
d=f"the name given by parents is {me} and lucky no is {7}...i like{c} no also"
e=f"the value of cos0 is {math.cos(0)}"
print(d)
print(e)