# Aim is to make a function which will take tokens in Reverse polish notation and evaluate the value
import math
from rev_pol_nota import is_numeric


def evaluate_rpn(rpn_tokens):
    operands = []
    for token in rpn_tokens:
        if is_numeric(token):
            operands.append(token)
        elif token in "+-*/^%":
            num_2 = operands.pop()
            num_1 = operands.pop()
            if token == "+":
                result = float(num_1) + float(num_2)
            elif token == "-":
                result = float(num_1) - float(num_2)
            elif token == "*":
                result = float(num_1) * float(num_2)
            elif token == "/":
                result = float(num_1) / float(num_2)
            elif token == "^":
                result = float(num_1) ** float(num_2)
            elif token == "%":
                result = float(num_1) % float(num_2)
            operands.append(result)
        else:
            num = float(operands.pop())
            if token == "sinh":  # sinh
                result = math.sinh(num)
            elif token == "cosh":  # cosh
                result = math.cosh(num)
            elif token == "tanh":  # tanh
                result = math.tanh(num)
            elif token == "csch":  # cosech
                result = 1 / math.sinh(num)
            elif token == "sech":  # sech
                result = 1 / math.cosh(num)
            elif token == "coth":  # coth
                result = 1 / math.tanh(num)
            elif token == "asin":  # arcsin
                result = math.asin(num)
            elif token == "acsc":  # arccosec
                result = 1 / math.asin(num)
            elif token == "acos":  # arccos
                result = math.acos(num)
            elif token == "atan":  # arctan
                result = math.atan(num)
            elif token == "asec":  # arcsec
                result = 1 / math.acos(num)
            elif token == "acot":  # arccot
                result = 1 / math.atan(num)
            elif token == "sin":  # sin
                result = math.sin(num)
            elif token == "csc":  # cosec
                result = 1 / math.sin(num)
            elif token == "cos":  # cos
                result = math.cos(num)
            elif token == "tan":  # tan
                result = math.tan(num)
            elif token == "sec":  # sec
                result = 1 / math.cos(num)
            elif token == "cot":  # cot
                result = 1 / math.tan(num)
            elif token == "exp":  # exp
                result = math.exp(num)
            elif token == "ln":  # ln
                result = math.log(num)
            elif token == "log":  # log10
                result = math.log(num, 10)
            elif token == "acoth":  # acoth
                result = 1 / math.atanh(num)
            elif token == "acsch":  # acosech
                result = 1 / math.asinh(num)
            elif token == "asinh":  # asinh
                result = math.asinh(num)
            elif token == "acosh":  # acosh
                result = math.acosh(num)
            elif token == "atanh":  # atanh
                result = math.atanh(num)
            elif token == "asech":  # asech
                result = 1 / math.acosh(num)
            operands.append(result)

    return operands[0]


"""
rpn_tokens1 = ["3", "4", "+"]
rpn_tokens2 = ["10", "2", "/"]
rpn_tokens3 = ["5", "2", "^"]
rpn_tokens4 = ["10", "2", "%"]
rpn_tokens5 = ["1", "2", "3", "+", "+"]
rpn_tokens6 = ["1", "2", "3", "*", "+"]
rpn_tokens7 = ["1", "2", "+", "3", "*"]
rpn_tokens8 = ["1", "丂"]  # arcsin
rpn_tokens9 = ["1", "Π"]  # cosec
rpn_tokens10 = ["1", "Ξ"]  # exp
rpn_tokens11 = ["1", "λ"]  # ln
rpn_tokens12 = ["1", "β"]  # log
print(evaluate_rpn(rpn_tokens1))  # Should print 7
print(evaluate_rpn(rpn_tokens2))  # Should print 5
print(evaluate_rpn(rpn_tokens3))  # Should print 25
print(evaluate_rpn(rpn_tokens4))  # Should print 0
print(evaluate_rpn(rpn_tokens5))  # Should print 6
print(evaluate_rpn(rpn_tokens6))  # Should print 7
print(evaluate_rpn(rpn_tokens7))  # Should print 9
print(evaluate_rpn(rpn_tokens8))  # Should print the arcsin of 1
print(evaluate_rpn(rpn_tokens9))  # Should print the cosec of 1
print(evaluate_rpn(rpn_tokens10))  # Should print e^1
print(evaluate_rpn(rpn_tokens11))  # Should print the natural logarithm of 1
print(evaluate_rpn(rpn_tokens12))  # Should print the base-10 logarithm of 1
"""
#    print(evaluate_rpn(['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'ln', '+', 'x', 'log', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'cot', '+', 'sec', '+', 'cosec', '+', 'tan', '+', 'cos', '+', 'sin', '+', 'exp', '+', 'acot', '+', 'asec', '+', 'acosec', '+', 'atan', '+', 'acos', '+', 'asin', '+', 'coth', '+', 'cosech', '+', 'sech', '+', 'tanh', '+', 'cosh', '+', 'sinh']))
#print(evaluate_rpn(['-5', '-3', '5', '6', '-', '*', '-87', '*', '+']))
#print(evaluate_rpn(['5', '2', '3', 'sin', '*', '+']))
#print(evaluate_rpn(['2', 'exp', '3', 'ln', '*', '4', '-']))
#print(evaluate_rpn(['0.5', 'acos', '0.5', 'asin', '+']))
#print(evaluate_rpn(['1', 'atan', '1', 'acot', '+']))
#print(evaluate_rpn(['2', 'asec', '2', 'acsc', '+']))
#print(evaluate_rpn(['5', '3', '2', 'cosh', '*', '-']))
#print(evaluate_rpn(['2', '3', '^', '10', 'log', '+']))
#print(evaluate_rpn(['2', 'sinh', '2', 'cosh', '+']))
#print(evaluate_rpn(['2', 'tanh', '2', 'coth', '+']))

#print(evaluate_rpn(['-3', '2', '-5', '-7', '3', '+', '-', '*', '-', '-2', '3', '-4', '-5', '2', '-', '-', '*', '-', '-', '-1', '2', '-3', '-4', '1', '-', '-', '*', '-', '+']))
"""
#print(eval(f"-5+(-3)*(5-6)*-87"))
#print(eval(f"5+2*math.sin(math.radians(3))"))
"""


#print(eval(f"(-3 - 2 * (-5 - (-7 + 3))) - (-2 - 3 * (-4 - (-5 - 2))) + (-1 - 2 * (-3 - (-4 - 1)))"))
