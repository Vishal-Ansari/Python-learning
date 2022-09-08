print("enter the num 1")
n1=input()
print("enter the num 2")
n2=input()

try:
    print("the sum of two numbers is",
      int(n1)+int(n2))
except Exception as e:
    print(e)

print("this line is important")