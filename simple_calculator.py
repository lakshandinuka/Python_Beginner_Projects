# Define functions for mathematical operations
def add(a, b):
    return a+b


def substract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero"
    return a/b


# USer input for the operation
print("---- Simple Calculator ----")
print("1-Add \n2-Substract \n3-Multiply \n4-Divide")
operation = input("Choose an Operation (1, 2, 3, 4): ")

number1 = float(input("Enter Number 1: "))
number2 = float(input("Enter Number 2: "))

# Mathematical operations
if operation == "1":
    print(f"{"Answer: "} {add(number1, number2)}")
elif operation == "2":
    print(f"{"Answer: "} {substract(number1, number2)}")
elif operation == "3":
    print(f"{"Answer: "} {multiply(number1, number2)}")
elif operation == "4":
    print(f"{"Answer: "} {divide(number1, number2)}")
else:
    print("Invalid Operation")
