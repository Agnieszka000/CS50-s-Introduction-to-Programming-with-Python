#  Implement a program that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).

def dots(user_inp):
    print(f'{user_inp.replace(" ", "...")}')

sentence = input('Write a sentence: ')
dots(sentence)