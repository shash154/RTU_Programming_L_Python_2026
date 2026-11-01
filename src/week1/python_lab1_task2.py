def greet_user(name):
    """Clean up a name and return a greeting.

    >>> greet_user("  alice  ")
    'Hello, Alice!'
    >>> greet_user("jOHN   smith")
    'Hello, John Smith!'
    """
    cleaned = " ".join(name.split()).title()
    return f"Hello, {cleaned}!"


if __name__ == "__main__":
    print(greet_user(input("Your name: ")))