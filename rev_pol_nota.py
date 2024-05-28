# Aim is to create a func which will convert tokens to postfix notations

precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}
function_replacements = {"sinh": "Ψ", "cosh": "Φ", "tanh": "Ω", "cosech": "ξ", "sech": "ζ",
                         "coth": "Θ", "arcsin": "丂", "arccosec": "万", "arccos": "七", "arctan": "丄", "arcsec": "丈",
                         "arccot": "下", "sin": "$", "cosec": "Π", "cos": "€",
                         "tan": "Δ", "sec": "ω", "cot": "Λ",
                         "exp": "Ξ", "ln": "λ", "log": "β"}


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
        if token in function_replacements.values() or token.isalpha() or is_numeric(token):
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
