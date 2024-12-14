# example.py
def greet(name):
    """
    A simple function to greet the user.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
