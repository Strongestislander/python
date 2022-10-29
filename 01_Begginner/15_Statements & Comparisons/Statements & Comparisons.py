


def max_num(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
print("Welcome to the max number calculator")
print("------------------------------------")
num1 = input("please input the First Number: ")
num2 = input("please input the Second Number: ")
num3 = input("please input the Third Number: ")
print("------------------------------------")
print("The max number is: ", max_num(num1, num2, num3))