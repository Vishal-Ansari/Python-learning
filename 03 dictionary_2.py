D={"vishal":"btech",
"mbbs":"ansari",
"preshaan":"carrier ko lekr"}

name=input("enter the name:")
print(name,"means",D[name])
del D["preshaan"]
print(D)
