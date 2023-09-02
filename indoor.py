# Implement a program that prompts the user for input and then outputs that same input in lowercase. 
# Punctuation and whitespace should be outputted unchanged. 
# You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

def main(user_inp):
    print(f'Your word in lowercase is: {user_inp.lower()}')

word = input('Write a word in uppercase: ')
main(word)