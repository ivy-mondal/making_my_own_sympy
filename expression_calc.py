import math
from tokenization_func import tokenize
from rev_pol_nota import rev_pol_func
from rpn_eval import evaluate_rpn


if __name__ == "__main__":
    print(evaluate_rpn(rev_pol_func(tokenize("2+2"))))  # 4
    print(evaluate_rpn(rev_pol_func(tokenize("5*3")))) # 15
    print(evaluate_rpn(rev_pol_func(tokenize("10/2"))))  # 5.0
    print(evaluate_rpn(rev_pol_func(tokenize("7-3"))))# 4
    print(evaluate_rpn(rev_pol_func(tokenize("2^3"))))  # 8
    print(evaluate_rpn(rev_pol_func(tokenize("sin(30)"))))  # 0.5 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("cos(60)"))))  # 0.5 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("tan(45)"))))  # 1.0 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("asin(0.5)"))))  # 30.0 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("acos(0.5)"))))  # 60.0 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("exp(1)"))))  # 2.71828 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("ln(e)"))))  # 1.0 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("log(100)"))))  # 2.0 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("2*sin(30)+3"))))  # 5.0 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("exp(2)*3-1"))))  # 21.0855 (approximately)
    print(evaluate_rpn(rev_pol_func(tokenize("10/cos(60)"))))  # 20.0 (approximately)