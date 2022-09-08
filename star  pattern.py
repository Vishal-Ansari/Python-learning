row=int(input("how many row u wnt to print:--"))
n=int(input("Type 1 or 0:--"))
boolean=bool(n)

if boolean==True:
    for i in range(0,row+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

elif boolean==False:
    for i in range(row,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
