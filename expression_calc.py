

from tokenization_func import tokenize
from rev_pol_nota import rev_pol_func
from rpn_eval import evaluate_rpn


if __name__ == "__main__":
    print(evaluate_rpn(rev_pol_func(tokenize("((35+9)*2.5)/(3-1)"))))  # Should print 73.75
    print(evaluate_rpn(rev_pol_func(tokenize("(10.5*(2+3.2))-(4.8/2)"))))  # Should print 51.32
    print(evaluate_rpn(rev_pol_func(tokenize("((10-2.8)*3.5)/(2.2+1.8)"))))  # Should print 10.34
    print(evaluate_rpn(rev_pol_func(tokenize("(10.2/(2.5+1.2))^2"))))  # Should print 4.11
    print(evaluate_rpn(rev_pol_func(tokenize("(10.5+2.8)^2-(3.2*2.1)"))))  # Should print 83.11
    print(evaluate_rpn(rev_pol_func(tokenize("10.2%((2.5+1.8)*3.2)"))))  # Should print 0.83

print(eval(f"((35+9)*2.5)/(3-1)"))
print(eval(f"(10.5*(2+3.2))-(4.8/2)"))
print(eval(f"((10-2.8)*3.5)/(2.2+1.8)"))
print(eval(f"(10.2/(2.5+1.2))**2"))
print(eval(f"(10.5+2.8)**2-(3.2*2.1)"))
print(eval(f"10.2%((2.5+1.8)*3.2)"))