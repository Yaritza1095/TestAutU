def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number"))
    print(a+b)
def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a-b)
def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a*b)
def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(a/b)

operation = input("Please type +, -, * or /")
if operation == "+":
    addition()
elif operation == "-":
    subtraction()
elif operation == "*":
    multiplication()
elif operation == "/":
    division()
else:
    print("You entered an invalid choice")