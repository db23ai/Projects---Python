try:
    # Prompt the user to enter the first number and convert it to an integer
    a = int(input("Enter the First Number: "))

    # Prompt the user to enter the second number and convert it to an integer
    b = int(input("Enter the Second Number: "))

    # Display the available arithmetic operations to the user
    print("What kind of operation do you want to perform. \nPress + for Addition\nPress - for Subtraction\nPress / for Division\npress * for Multiplication")

    # Take the operation input from the user
    o = input("Enter Operation: ")

    # Use match-case (introduced in Python 3.10) to handle the operation
    match o:
        case "+":  # If user entered '+', perform addition
            print(f"The result is: {a + b}")
        case "-":  # If user entered '-', perform subtraction
            print(f"The result is: {a - b}")
        case "*":  # If user entered '*', perform multiplication
            print(f"The result is: {a * b}")
        case "/":  # If user entered '/', perform division
            print(f"The result is: {a / b}")
        case _:    # Default case for invalid operations (should use `_` instead of `default`)
            print("There was an error")

# Catch any exception (e.g., invalid input, division by zero) and print a user-friendly error message
except Exception as e:
    print("Enter a valid value of a and b")
