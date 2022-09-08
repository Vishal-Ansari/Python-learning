
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

#--------x----------x--STATIC METHOD---x--------------x------------------x-----#

    @staticmethod
    def printgood(string):
        print("this is good"+string)
        # return "bhagjaa"  # y bs none n aae isilie vrna to koi use ni bs esi lelia....


#--------x--------------x-------------x-MULTIPLE INHERITENCE--------------------X--------X----------------------X#


class player:
    no_of_games=4
    def __init__(self,name,game):
        self.name= name
        self.game= game

    def print_details(self):
        return f"Name is {self.name} , game is {self.game}"    

class coolprogrammer(Employee,player):
    language="c++"
    def printlanguage(self):
        print(self.language)


vishal=Employee("Vishal","420","anokha")
jumboo=Employee("jumboo","440","busy")

shubham=player("shuham",["cricket"])
karan=coolprogrammer("karan",789,"coolprogrammer")

print(karan.print_details())
print(karan.printlanguage())