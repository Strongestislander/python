
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter Second number: "))

if op == "+":
    print(num1, op, num2, "=", num1 + num2)
elif op == "-":
    print(num1, op, num2, "=", num1 - num2)
elif op == "/":
    print(num1, op, num2, "=", num1 / num2)
elif op == "*":
    print(num1, op, num2, "=", num1 * num2)
else:
    print("Invalid operator, program is closing")

