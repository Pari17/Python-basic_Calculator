
# Basic calculator

class calculator:
    # Add function
    def add(self, x, y):
        return x + y

    # Subtract function
    def subtract(self, x, y):
        return x - y

    # Multiply function
    def multiply(self, x, y):
        return x * y

    # Divide function
    def divide(self, x, y):
        return x / y

    def start_calculator(self):
        choice = ""
        while choice != "e":
            print("Select operation:")
            print("(1) Add")
            print("(2) Subtract")
            print("(3) Multiply")
            print("(4) Divide")
            print("(e) Exit")
            
            choice = input("Enter choice:")
            print("You chose choice:", choice)

            if choice in ('1', '2', '3', '4'):
                try:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == "1":
                                    print(num1, "+", num2, "=", self.add(num1, num2))
                    elif choice == "2":
                                    print(num1, "-", num2, "=", self.subtract(num1, num2))
                    elif choice == "3":
                                    print(num1, "*", num2, "=", self.multiply(num1, num2))
                    else:
                                    print(num1, "/", num2, "=", self.divide(num1, num2))
                except ValueError:
                    print("That was not a valid number.  Try again...")
                except ZeroDivisionError:
                    print("Zero division error; you can not divide by zero")
        print("Exiting ....")

        


     
