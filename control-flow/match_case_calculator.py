# Simple Calculator with Match Case

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))


operation_type = input("Choose the operation (+, -, *, /):")

match operation_type:
    case n if n == "+":
        result = num1 + num2
        
    case n if n == "-":
        result = num1 - num2
        
    case n if n == "*":
        result = num1 * num2
        
    case n if n == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            result = None
        else:
            result = num1 / num2

if result is not None:
    print(f"The result is: {result}")          
