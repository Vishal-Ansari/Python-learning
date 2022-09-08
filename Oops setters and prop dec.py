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


shahrukh=Employee("Rahul"," Anjali")
salman=Employee("Raj"," Anjali")

print(shahrukh.explain())
print(shahrukh.gmail)

shahrukh.fname="bazigar"  # name will not change because it isnt a fucntion
print(shahrukh.gmail)

shahrukh.fname="bazigar"
# print(shahrukh.email())  # now the name will change to badshah bcoz it is in function
print(shahrukh.email)  # now the name will change due to property ..direct access to email

# ab setter ko use krne k lie print statement chlaege.
shahrukh.email="vishal.ansari@gmail.com"  #this wont work untill setter is used to do so
print(shahrukh.fname)    #setter k lie
print(shahrukh.lname)    #setter k lie
print(shahrukh.email)    #setter k lie

del shahrukh.email
print(shahrukh.email)  #del setter attribute k baa