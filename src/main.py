def greet(name: str) -> str:
    """Return a personalized greeting.

    Args:
        name (str): The name to greet

    Returns:
        str: The greeting message
    """
    return f"Hello, {name}!"


def main():
    name = input("What's your name? ")
    print(greet(name))


if __name__ == "__main__":
    main()
