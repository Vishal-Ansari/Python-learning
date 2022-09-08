class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    
    def __add__(self,other):   # operator are overloadibg here.. add,divv,multi.,,,
        return self.salary+other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"
       

emp1=Employee("vishal", 400, "programmer")
emp2=Employee("rohan", 100, "burger seller")

print(emp1)  # str vala chalta h agr specified n ho ki repr chlana y str..
print(repr(emp1))
print(emp1+emp2)