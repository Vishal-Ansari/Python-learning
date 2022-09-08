class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    pass

    def print_details(self):
        return f"Name is {self.name} , Salaray is {self.salary}, and the role is {self.role}"


vishal=Employee()
jumboo=Employee()


vishal.name="vishal ansari"
vishal.salary=360000000000
vishal.role="CEO"


jumboo.name="Jumboo"
jumboo.salary=250000000
jumboo.role="CEO coordinater"


print(vishal.print_details())

#-----X-------X CONSTRUCTOR ----- OR---- INIT FUNCTION---------X----------X-----#

class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"

vishal=Employee("Vishal","420","anokha")
# employee(class) doesnt take any argument thats why we used init function CONSTRUCTOR

print(vishal.salary)
