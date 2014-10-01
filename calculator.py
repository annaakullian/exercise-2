from arithmetic import *


equation = raw_input("> ")

#math_dictionary = ['+', '-', '*', '/', 'square', 'cube', 'pow', 'mod']
equation_list = equation.split(' ')


math_dictionary = {'+': add}


def tokenize_equation(equation):
    #equation_list = equation.split(' ')
    print equation_list
    if equation == "q" or equation == "Q":
        quit()
    else:
        if 2 > len(equation_list) > 3:
            print "I don't understand" 
        elif equation_list[0] not in math_dictionary:
            print "I don't understand"
        elif equation_list[0] in math_dictionary.keys():
            num1 = equation_list[1]
            num2 = equation_list[2]
            num1 = int(num1)
            num2 = int(num2)
            return math_dictionary[equation_list[0]](num1, num2)
        



print tokenize_equation(equation)


    
'''
def calc(equation):
    if tokenize_equation(equation)'''