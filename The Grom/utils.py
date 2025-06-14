"""
    Name: utils.py
    Author: 
    Created:
    Purpose: A utilty module with commonly used functions
"""

from rich.console import Console
from rich.panel import Panel



def main():
    """ Place code here to test the modules """
    print(title("Test the utils module"))
    int_num = get_int("Please enter a whole number: ")
    print(f"Your whole number is: {int_num}")
    float_num = get_float("Please enter any number: ")
    print(f"Your number is: {float_num}")


def title(statement, color="green", under_text="By Owen Osmera"):
    """Takes in a string argument
        returns a string with ascii decorations
    """
    console = Console()
    # Create the title string
    # Initialize the result string variable
    console.print(
        Panel.fit(
            statement,
            style=color,
            subtitle=under_text
        )
    )


def get_int(prompt):
    """Get an integer from the user with try catch
        The prompt string parameter is used to ask the user
        for the type of input needed
    """
    # Declare local variable
    num = 0

    # Ask the user for an input based on the prompt string parameter
    num = input(prompt)

    # If the input is numeric, convert to int and return value
    try:
        return int(num)

    # If the input is not numeric,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a whole number.")
        print(f"Let' try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_int(prompt)


def get_float(prompt):
    """Get a number from the user with try catch
        The prompt string parameter is used to ask the user
        for the type of input needed
    """
    # Declare local variable
    num = 0

    # Ask the user for an input based on the what parameter
    num = input(prompt)

    # If the input is numeric, convert to float and return value
    try:
        return float(num)

    # If the input is not numeric,
    # Inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a number.")
        print(f"Let's try that again.\n")

        # Call function from the beginning
        # This is a recursive function call
        return get_float(prompt)


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
