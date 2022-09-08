class Employee:
    no_of_leaves=7 # this is class property cannot be change by vishal or jumbo0..
    pass
vishal=Employee()
jumboo=Employee()


vishal.name="vishal ansari"
vishal.salary=360000000000
vishal.role="CEO"
vishal.no_of_leaves=21  # instant variable.. it doesnt change the class variable of no of leaves

jumboo.name="Jumboo"
jumboo.salary=250000000
jumboo.role="CEO coordinater"

print(Employee.no_of_leaves,vishal.no_of_leaves,jumboo.no_of_leaves)
print(jumboo.__dict__)
Employee.no_of_leaves=10
print(Employee.no_of_leaves)
