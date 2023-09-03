# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value 
# formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, 
# wherein:
#    x is an integer
#    y is +, -, *, or /
#    z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

def main():
    expr = input("Expression: ")
    x, y, z = expr.split(" ")
    evaluate(x,y,z)

def evaluate(x,y,z):
    match y:
        case "+":
            eval_exp = float(x) + float(z)
            print(f"{eval_exp:.1f}") # The formatting ":.1f" makes the float print 1 decimal digit after "."
        case "-":
            eval_exp = float(x) - float(z)
            print(f"{eval_exp:.1f}")
        case "*":
            eval_exp = float(x) * float(z)
            print(f"{eval_exp:.1f}")
        case "/":
            if float(z) == 0:
                print ("Division impossible!")
            else:
                eval_exp = float(x) / float(z)
                print(f"{eval_exp:.1f}")

main()