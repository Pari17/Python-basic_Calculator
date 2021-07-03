# Basic calculator

# Add function
def add(x, y):
    return x + y

# Subtract function
def subtract(x, y):
    return x - y

# Multiply function
def multiply(x, y):
    return x * y

# Divide function
def divide(x, y):
    return x / y

choice = ""

while choice != "e":
    print("Select operation:")
    print("(1) Add")
    print("(2) Subtract")
    print("(3) Multiply")
    print("(4) Divide")
    print("(e) Exit")
    choice = input("Enter choice:")
    
    print("You chose choice:",choice)

    if choice in ('1', '2', '3', '4'):
    
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                            print(num1, "+", num2, "=", add(num1, num2))
            elif choice == "2":
                            print(num1, "-", num2, "=", subtract(num1, num2))
            elif choice == "3":
                            print(num1, "*", num2, "=", multiply(num1, num2))
            else:
                            print(num1, "/", num2, "=", divide(num1, num2))
        except ValueError:
            print("That was not a valid number.  Try again...")

print("Exiting ....")
     