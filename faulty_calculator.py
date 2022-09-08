# give fault at values .......... 45*3=555,  56+9=77,  56/6=4...

print("select the operator:-")
op=input()

a=int(input("enter first no:- "))
b=int(input("enter second no:- "))


if a==45 and b==3 and op=="multiply":
    c=555
elif op=="multiply":
    c=a*b

elif a==56 and b==9 and op=="addition":
    c=77
elif op=="addition":
    c=a+b

elif a==56 and b==6 and op=="division":
    c=4
elif op=="division":
    c=a/b    
else:
    c=a-b   
   
print("the result of given operation is = ",c)
