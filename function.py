# a=9
# b=8
# c=sum((a,b))  # pre define function oor built in function
# print(c)

def function1():
    print("hello you in my kingdom")
# print(function1())
function1()


# def function2(a,b):
#     average=(a+b)/2
#     print(average)
#
# function2(2,5)
# v=function2(2,5)
# print(v)

def function2(a,b):
    """This is a function to calculate the average of two numbers"""
    average=(a+b)/2
    # print(average)
    return average
print(function2.__doc__)
v=function2(2,5)
print(v)

