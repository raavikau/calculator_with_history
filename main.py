def calculation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            print("Error: division by zero")
            return None
        return a / b
    else:
        print("wrong operator")

first = int(input("enter the first value: "))
second = int(input("enter the second value: "))
choice = input("please check +, -, *, /")

print(calculation(first, second, choice))
