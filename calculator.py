equation = raw_input("> ")

operands = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']

def tokenize_equation(equation):
    equation_list = equation.split(" ")
    if equation == "q" or equation == "Q":
        quit()
    else:
        if equation[0] not in operands:
            print "I don't understand"



    
'''
def calc(equation):
    if tokenize_equation(equation)'''