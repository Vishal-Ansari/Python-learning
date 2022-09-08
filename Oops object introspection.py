class Employee:
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        self.gmail=f"{fname}@gmail.com"

    def explain(self):
        return f"this employee is {self.fname} loves {self.lname}"

    @property  # i am using this to change name without using function to access email directly
    def email(self):
        if self.fname ==None or self.lname ==None:
            return "email is not set now....pleasse set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        print("setting now")
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]

    @email.deleter     # to delete the attritubute we use the deleter decorator
    def email(self):
        self.fname=None
        self.lname=None

skillf=Employee("skill","learning")
print(skillf.email)
# now we are inspecting object through diferent methods..
print(type("this is "))
print(id("this is "))
print(dir(skillf))

# now using inpection method

import inspect
print(inspect.getmembers(skillf))