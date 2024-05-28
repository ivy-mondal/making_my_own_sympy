# Aim is to make a function which will take tokens in Reverse polish notation and evaluate the value
def evaluate_rpn(rpn_tokens):
    operands = []
    for token in rpn_tokens:
        if token in "+-*/^%":
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
            operands.append(token)
    return operands[0]

"""
rpn_tokens = ['3', '4', '+']
print(evaluate_rpn(rpn_tokens))  # Should print 7.0
rpn_tokens = ['10', '2', '-']
print(evaluate_rpn(rpn_tokens))  # Should print 8.0
rpn_tokens = ['5', '3', '*']
print(evaluate_rpn(rpn_tokens))  # Should print 15.0
rpn_tokens = ['12', '3', '/']
print(evaluate_rpn(rpn_tokens))  # Should print 4.0
rpn_tokens = ['2', '3', '+', '4', '*']
print(evaluate_rpn(rpn_tokens))  # Should print 20.0
rpn_tokens = ['17', '5', '%']
print(evaluate_rpn(rpn_tokens))  # Should print 2.0
rpn_tokens = ['2', '3', '^']
print(evaluate_rpn(rpn_tokens))  # Should print 8.0
rpn_tokens = ['10', '2', '^', '3', '*', '4', '+']
print(evaluate_rpn(rpn_tokens))  # Should print 304.0
rpn_tokens = ['5', '2', '%', '3', '*', '4', '-']
print(evaluate_rpn(rpn_tokens))  # Should print -1.0

"""