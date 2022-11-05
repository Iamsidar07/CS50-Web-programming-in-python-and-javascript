#functional programming
def announce(f):
    def wrapper():
        print("Function is going to run.")
        f()
        print("Function ran successfully.")
    return wrapper

@announce
def hello(): # Can't pass argument
    print(f"Hello,sir")

hello()