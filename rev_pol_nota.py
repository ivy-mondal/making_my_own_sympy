# Aim is to create a func which will convert tokens to postfix notations

precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}
functions = ['sin', 'cos', 'tan', 'sec', 'cosec', 'cot', 'sinh', 'cosh', 'tanh', 'sech', 'cosech', 'coth', 'asin', 'acos', 'atan', 'asec', 'acosec', 'acot', 'asinh', 'acosh', 'atanh', 'acoth', 'asech', 'acosech', 'log', 'ln', 'exp']


def is_numeric(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def rev_pol_func(tokens):
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token in functions:
            operator_stack.append(token)
        elif token.isalpha() or is_numeric(token):
            output_queue.append(token)

        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == "(":
                operator_stack.pop()
        elif token in precedence:
            while operator_stack and operator_stack[-1] != "(" and precedence[token] <= precedence.get(operator_stack[-1], 0):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    while operator_stack:
        output_queue.append(operator_stack.pop())
    return output_queue


"""
tokens1 = ['2', '+', '3', '*', '(', '4', '-', '2', ')']
print(rev_pol_func(tokens1))  # [2.0, 3.0, 4.0, 2.0, '-', '*', '+']

tokens2 = ['10', '-', '5', '+', '(', '3', '*', '2', ')']
print(rev_pol_func(tokens2))  # [10.0, 5.0, '-', 3.0, 2.0, '*', '+']

tokens3 = ['5', '*', '2', '-', '(', '3', '+', '1', ')']
print(rev_pol_func(tokens3))  # [5.0, 2.0, '*', 3.0, 1.0, '+', '-']

tokens4 = ['10', '/', '2', '-', '(', '3', '+', '1', ')']
print(rev_pol_func(tokens4))  # [10.0, 2.0, '/', 3.0, 1.0, '+', '-']

tokens5 = ['10', '^', '2', '*', '(', '3', '-', '1', ')']
print(rev_pol_func(tokens5))  # [10.0, 2.0, '^', 3.0, 1.0, '-', '*']
"""
