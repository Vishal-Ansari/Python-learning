class A:
    def met(self):
        print("this is a method from class A")

class B:
    def met(self):
        print("this is a method from class B")
    
class C:
    def met(self):
        print("this is a method from class C")
    

class D(B,C):
    def met(self):
        print("this is a method from class D")
    


a=A()
b=B()
c=C()
d=D()

d.met()