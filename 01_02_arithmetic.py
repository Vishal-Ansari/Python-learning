#question 2
#vishal ansari
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

arith = input("Enter any operation +,-,*,/: ")

result = 0
if arith == '+':
    result = num1 + num2
elif arith == '-':
    result = num1 - num2
elif arith == '*':
    result = num1 * num2
elif arith == '/':
    result = num1 / num2
else:
    print("Invalid input!")

print(num1, arith , num2, "=", result)
print("vishal ansari  section-N  std-id-200111238")
