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


result1 = add(5, 3)
result2 = subtract(10, 4)

print("Addition Result:", result1)
print("Subtraction Result:", result2)
