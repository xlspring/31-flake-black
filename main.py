from utils import validate_input, format_name


def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def main():
    name = input("Enter your name: ")
    
    if not validate_input(name):
        print("Name cannot be empty.")
        return
    
    formatted_name = format_name(name)
    greeting = greet(formatted_name)
    print(greeting)


if __name__ == "__main__":
    main() 