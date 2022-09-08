def factorial(n):
    
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

    pass
number=int(input("enter the number"))
print(factorial(number))       
print("this is factorial using iterative method")


def fact_recursive(n):
    if n==1:
        return 1
    else:
        return n*fact_recursive(n-1)    

number=int(input("enter the number"))
print(factorial(number))       
print("this is factorial using recursive method")