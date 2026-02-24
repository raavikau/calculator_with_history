def calculation(a, b, operator):
    if operator == "+":
        return f"{a} + {b} = {a + b} \n"
    elif operator == "-":
        return f"{a} - {b} = {a - b} \n"
    elif operator == "*":
        return f"{a} * {b} = {a * b} \n"
    elif operator == "/":
        if b == 0:
            print("Error: division by zero")
            return None
        return f"{a} / {b} = {a / b} \n"
    else:
        print("wrong operator")

def save_history():
    try:
        with open("history.txt", "r") as readfile:
            content = readfile.read()
            if content == "":
                print("file is empty")
            print(content)
    except FileNotFoundError:
        print("No history file found")

def calculator(c, d, operation):
    result = calculation(c, d, operation)
    if result is not None:
        with open("history.txt", "a") as file:
            file.write(result)
        print("Successfully added")

def clear_history():
    pass

while True:
    choice = input("Enter +, -, *, / or type history, clear, quit ")
    if choice == "quit":
        print("Good by!")
        break
    elif choice == "clear":
        clear_history()
    elif choice == "history":
        save_history()
    elif choice in ["+", "-", "*", "/"]:
        first = int(input("enter the first value: "))
        second = int(input("enter the second value: "))
        calculator(first, second, choice)
    else:
        print("Invalid command")
