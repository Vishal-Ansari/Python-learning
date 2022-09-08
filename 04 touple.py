#tuples are immutable (cannot change)
tp=(1,2,3)
#tp1=(1)  it gives 1 as output
#tp2=(1,)  it gives (1,) as output
print(tp)
#tp[1]=8 its an error because it cant be change
a=8
b=7
print(a,b)
# to swap generlyy we use temp method ......but in pythonn there is direct method
a,b=b,a
#temp=a
#a=b
#b=temp
print(a,b)