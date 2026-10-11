"""Try to access a local variable out its function."""

def show_name():
    """Try and print a local variable"""
    name = "Ivan"
    print(name)

show_name()
# print(name)


# Read and change a global variable inside a function.

score = 10

def update_score():
    """Print and update the global score."""
    global score 
    print("Inside the function:", score)
    score = 20

print("Before:", score)
update_score()
print("after:", score)
