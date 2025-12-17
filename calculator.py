import math

print("Welcome to Smart Calculator")

while True:
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Power")
    print("8. Exit")

    choice = input("Enter choice (1-8): ")

    if choice == '8':
        print("Bye Bye 👋")
        break

    try:
        if choice in ['1', '2', '3', '4', '7']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        else:
            num1 = float(input("Enter number: "))
    except:
        print("Please enter numbers only!")
        continue

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", num1 / num2)
    elif choice == '5':
        print("Result:", num1 * num1)
    elif choice == '6':
        if num1 < 0:
            print("Cannot take square root of negative number")
        else:
            print("Result:", math.sqrt(num1))
    elif choice == '7':
        print("Result:", math.pow(num1, num2))
    else:
        print("Wrong choice! Try again.")
