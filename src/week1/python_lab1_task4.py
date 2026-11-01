OPERATORS = "+-*/"


def is_number(token):
    """Return True if token can be read as a number.

    >>> is_number("3.5")
    True
    >>> is_number("+")
    False
    """
    try:
        float(token)
        return True
    except ValueError:
        return False


def extract_numbers(text):
    """Return all numbers in the text as floats.

    >>> extract_numbers("3 + 4 * 2")
    [3.0, 4.0, 2.0]
    """
    return [float(t) for t in text.split() if is_number(t)]


def extract_operators(text):
    """Return all operators in the text.

    >>> extract_operators("3 + 4 * 2")
    ['+', '*']
    """
    return [t for t in text.split() if len(t) == 1 and t in OPERATORS]


def apply_operator(a, op, b):
    """Apply one operator. Division by zero returns None.

    >>> apply_operator(6, "/", 3)
    2.0
    >>> apply_operator(1, "/", 0) is None
    True
    """
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else None
    raise ValueError(f"Unknown operator: {op}")


def analyze_text(text):
    """Analyze an arithmetic text, evaluating left to right.

    >>> analyze_text("3 + 4 * 2")
    {'numbers': [3.0, 4.0, 2.0], 'operators': ['+', '*'], 'result': 14.0}
    >>> analyze_text("")
    {'numbers': [], 'operators': [], 'result': None}
    """
    numbers = extract_numbers(text)
    operators = extract_operators(text)
    result = numbers[0] if numbers else None
    for op, n in zip(operators, numbers[1:]):
        if result is None:
            break
        result = apply_operator(result, op, n)
    return {"numbers": numbers, "operators": operators, "result": result}


if __name__ == "__main__":
    print(analyze_text(input("Expression (space separated): ")))