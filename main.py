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

def save_history():
    pass

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
        result = calculation(first, second, choice)
        print(result)
    else:
        print("Invalid command")
