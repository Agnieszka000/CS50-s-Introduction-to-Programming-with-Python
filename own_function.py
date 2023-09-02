# Put the main part of the code at the top but what's IMPORTANT I have to call this fucnction at the end:
def main():
    name = input('What\'s your name? ')
    hello(name) # It's important to define the parameter.
    hello() # I call the function without a parameter, so the default parameter is used/printed.

def hello(name='World'): # I assign a default value to the function just in case the programmer call the function WITHOUT a parameter.
    print(f'Hello, {name}.')

main() # I call the main function from the top.