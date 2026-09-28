print("WELCOME!")
command = ""
while command != "exit":
    command = input(": ")
    if command == "exit":
            break        
    first = float(input("Enter first number: "))
    operator = input("Enter operator: ")
    second = float(input("Enter second numbder: "))
    if operator == "+":
        result = first + second
        print(result)
    elif operator == "-":
        result = first - second
        print(result)
    elif operator == "*":
        result = first * second
        print(result)
    elif operator == "/":
        if second != 0:
            result = first / second
            print(result)
        if second == 0:        
            print("0 is invilid divisor")
    else:
        print("Invalid operator")

    