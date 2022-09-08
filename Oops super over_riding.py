# class A:
#     classvar1="i am a class variable in class A"
#     def __init__(self):
#         self.var="i am inside class A's constructor"
#         self.classvar1="instance var in class A"

# class B(A):
#     classvar1=" i am in class B"

# a=A()
# b=B()


# print(b.classvar1)
        

# ---------X------X--------------x-----------X oover writing--X-----------X-----------------X--------------------#


class A:
    classvar1="i am a class variable in class A"
    def __init__(self):
        self.var="i am inside class A's constructor"
        self.classvar1="instance var in class A"
        self.special="special hu m..overwrigte hokr koi wjaud ni rhjaega mmera"

class B(A):
    classvar1=" i am in class B"

    def __init__(self):
        # super().__init__()     # super use hota h overright krne k bad bhi use krne klie...ab print special hojaega
        self.var="i am inside class B's constructor"
        # self.classvar1="instance var in class B"
        super().__init__()
        print(super().classvar1)

a=A()
b=B()


print(b.classvar1)
# overrited print krunga m ab...or vo hoga ni kuk ab uska koi wajud hi nni bcha..
# print(b.special)



        