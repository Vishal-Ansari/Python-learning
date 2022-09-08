x=10 # Global

# def function(n):
#     # x=5  #Local
#     m=8 # local
#     global x
#     x=x+5
#     print(x,m)
#     print(n,"i have printed")
# function("this is no")

def vi():
    x=20
    def an():
        global x
        x=88
        print("before calling function an",x)
        an()
        print("after calling function an",x)

vi()        
print(x)