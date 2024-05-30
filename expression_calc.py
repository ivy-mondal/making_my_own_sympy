import math
from tokenization_func import tokenize
from rev_pol_nota import rev_pol_func
from rpn_eval import evaluate_rpn

if __name__ == "__main__":
    print(evaluate_rpn(rev_pol_func(tokenize("sin(30)"))))  # should be approximately0.5)
    print(evaluate_rpn(rev_pol_func(tokenize("cos(60)"))))  # should be approximately 0.5)
    print(evaluate_rpn(rev_pol_func(tokenize("tan(45)"))))  # should  be approximately 1)
    print(evaluate_rpn(rev_pol_func(tokenize("asin(0.5)"))))  # should be approximately 30)
    print(evaluate_rpn(rev_pol_func(tokenize("acos(0.5)"))))  # should be approximately 60)
if __name__ == "__main__":
    print(tokenize("sin(30)"))
    print(tokenize("cos(60)"))
    print(tokenize("tan(45)"))
    print(tokenize("asin(0.5)"))
    print(tokenize("acos(0.5)"))
if __name__ == "__main__":
    print(rev_pol_func(['sin', '(', '30', ')']))
    print(rev_pol_func(['cos', '(', '60', ')']))
    print(rev_pol_func(['tan', '(', '45', ')']))
    print(rev_pol_func(['asin', '(', '0.5', ')']))
    print(rev_pol_func(['acos', '(', '0.5', ')']))
if __name__ == "__main__":
    print(evaluate_rpn(['30', 'sin']))
    print(evaluate_rpn(['60', 'cos']))
    print(evaluate_rpn(['45', 'tan']))
    print(evaluate_rpn(['0.5', 'asin']))
    print(evaluate_rpn(['0.5', 'acos']))
