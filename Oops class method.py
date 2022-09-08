class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


vishal=Employee("Vishal","420","anokha")
jumboo=Employee("jumboo","440","busy")

vishal.change_leaves(45)
print(vishal.no_of_leaves)
# employee(class) doesnt take any argument thats why we used init function CONSTRUCTOR
