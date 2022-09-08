

# def function():
#     print("go to hell")

# fun2=function
# del function
# fun2()


# ------x--------------x--------------------x---------------------x----------------------x---------------------------#


# def executr(func):
#     func("this is it.")

# executr(print) # function  fucntion ko dala print ek function h agr funct m integers hote to sum bhi lelete print ki jgh

#--x---x---x----x-------x---------x--------x----------x---------x--------x---------x--------x-------x-------x-------x-----------------#


# ---------X---X--------X---------DECORATOR--------X---------X-----------X
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec

# def anything():
#     print("no one is nothing ")

# anything=dec1(anything)       # y krne se func1 replace hogya anything s.....
# anything()

#  now by @dec1 method
@dec1
def anything():
    print("no one is nothing ")
anything()