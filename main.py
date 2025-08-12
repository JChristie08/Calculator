

def main():
    print("Please enter two numbers and a function to perform the calculation.")
    num1 = float(input("Enter the first number for calculation: "))
    num2 = float(input("Enter the second number for calculation: "))
    print("Functions:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter the operation you want to perform: ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Division by zero is not allowed, try again."
    else:
        result = "Error: Invalid operation."

    print("The result of the calculation is :" , result)
    AnotherCalc = input("Do you want to perform another calculation? (y/n)")
    if AnotherCalc == 'y':
        main()
    elif AnotherCalc == 'n':
        print("Thank you for using the calculator. Goodbye!")
    else:
        print('invalid input, exiting the calculator.')

print("Welcome to the Calculator! Made by Jude Christie")
print("This program will perform calculations based on user input.")
main()
