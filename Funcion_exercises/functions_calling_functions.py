"""Demonstrate how one function calls another."""


def second_function():
    """Print the second function's message."""
    print("I am the second function")


def first_function():
    """Print a message and call the second function."""
    print("I am the first function")
    second_function()


first_function()