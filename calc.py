print("Welcome to the Simple Python Calculator!")
print("Enter your calculation in the format: number operation number")
print("Example: 1 + 1")
print("Type 'q' to quit.")

while True:
    user_input = input("Enter calculation: ")

    if user_input.lower() == 'q':
        print("Goodye :)")
        break

    try:
        # Split the input into components
        num1, operation, num2 = user_input.split()
        num1 = float(num1)
        num2 = float(num2)

        # selected operation
        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} = {result}")

        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} = {result}")

        elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} = {result}")

        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} = {result}")
            else:
                print("Error! Division by zero.")

        else:
            print("Invalid operation. Please use +, -, *, or /.")

    except ValueError:
        print("Invalid input. Please enter in the format: number operation number.")
    except Exception as e:
        print("An error occurred: {e}")