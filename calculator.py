from arithmetic import *

#math_dictionary = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
#equation_list = equation.split(' ')
#equation = raw_input("> ")

def tokenize_equation(equation):
    #equation = raw_input("> ")
    equation_list = equation.split(' ')
    math_dictionary = {'+': add, '-': subtract, '*': multiply, '/': divide, 
                        'square': square, 'cube': cube, 'pow': power, 'mod': mod}
    if equation == "q" or equation == "Q":
        quit()
    else:
        if 2 > len(equation_list) > 3:
            print "I don't understand"
        elif equation_list[0] not in math_dictionary:
            print "I don't understand"
        elif equation_list[0] in math_dictionary.keys():
            num1 = int(equation_list[1])
            if len(equation_list) == 2:
                return math_dictionary[equation_list[0]](num1)
            else:
                num2 = int(equation_list[2])
                return math_dictionary[equation_list[0]](num1, num2)

            
while True:
    print tokenize_equation(raw_input("> "))


    
'''
def calc(equation):
    if tokenize_equation(equation)'''