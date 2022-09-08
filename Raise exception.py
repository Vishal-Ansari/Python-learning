# a=input("what is your name?\n")
# b=int(input("what is your salary.\n"))

# if b==0:
#     raise ZeroDivisionError("b 0 h yaar berojgaaar.... kuchni hoga ab age .")
# if a.isnumeric():
#     raise Exception("number is not allowed")

# print(f"hello {a} apki salary {b} rupees h")    

c = input("Enter your name\n")
try:
    print(a)

except Exception as e:

    if c =="vishal":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")