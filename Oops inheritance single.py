class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def print_details(self):
        return f"Name is {self.name} , Salary is {self.salary}, and the role is {self.role}"

    @classmethod
    def from_dash(cls,string):
        # jack=string.split("-")
        # print(jack)
        # return cls(jack[0],jack[1],jack[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("this is good"+string)
        # return "bhagjaa"  # y bs none n aae isilie vrna to koi use ni bs esi lelia....


#-----------x------------x--------------x---INHERITANCE------x-----------x------------------x----------x-#


class programmer(Employee):  # inheritance....
    def __init__(self, aname, asalary, arole,language):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=language
    
    def printprog(self):
         return f"Programmer Name is {self.name} , Salary is {self.salary}, and the role is {self.role} and languages are{self.language}"

        
vishal=Employee("Vishal","420","anokha")
jumboo=Employee("jumboo","440","busy")
karan=Employee.from_dash("karan-400-bccha")

hari =programmer("hari",800,"programmer",["python","c"])
shri =programmer("shri","90","CID",["c++","jaava"])

print(hari.printprog())
print(hari.print_details())


