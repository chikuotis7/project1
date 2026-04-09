def add(a: float, b: float):
    return a + b


def addmul(a: float, b: float, c: float):
    return a + b + c


def sub(a: float, b: float):
    return a - b


def mul(a: float, b: float):
    return a * b


def div(a: float, b: float):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

