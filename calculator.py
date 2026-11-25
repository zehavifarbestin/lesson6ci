import sys


# ארבע הפונקציות הקיימות
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# כאן מוסיפים את main
def main():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <a> <b>")
        return

    operation = sys.argv[1]
    a = float(sys.argv[2])
    b = float(sys.argv[3])

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        print("Unknown operation")
        return

    print(result)



if __name__ == "__main__":
    main()