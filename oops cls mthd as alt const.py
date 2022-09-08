class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"

    @classmethod
    def from_str(cls,string):
        # jack=string.split("-")
        # print(jack)
        # return cls(jack[0],jack[1],jack[2])
        return cls(*string.split("-"))


vishal=Employee("Vishal","420","anokha")
jumboo=Employee("jumboo","440","busy")
karan=Employee.from_dash("karan-400-bccha")

print(karan.salary )

