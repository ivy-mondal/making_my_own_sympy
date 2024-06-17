import math
from tokenization_func import tokenize
from rev_pol_nota import rev_pol_func
from rpn_eval import evaluate_rpn


if __name__ == "__main__":
    """
    print(evaluate_rpn(rev_pol_func(tokenize("2+2"))))
    print(evaluate_rpn(rev_pol_func(tokenize("5*3"))))
    print(evaluate_rpn(rev_pol_func(tokenize("10/2"))))
    print(evaluate_rpn(rev_pol_func(tokenize("7-3"))))
    print(evaluate_rpn(rev_pol_func(tokenize("2^3"))))
    print(evaluate_rpn(rev_pol_func(tokenize("sin(30)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("cos(60)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("tan(45)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("asin(0.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("acos(0.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("exp(1)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("ln(2.78)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("log(100)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("2*sin(30)+3"))))
    print(evaluate_rpn(rev_pol_func(tokenize("exp(2)*3-1"))))
    print(evaluate_rpn(rev_pol_func(tokenize("10/cos(60)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("acosh(1.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("asinh(0.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("atanh(0.8)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("asech(1.2)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("acoth(0.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("acosh(1.5)*2+3"))))
    print(evaluate_rpn(rev_pol_func(tokenize("asinh(0.5)+atanh(0.8)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("asech(1.2)+acoth(0.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("acosh(1.5)+asinh(0.5)*2"))))
    print(evaluate_rpn(rev_pol_func(tokenize("atanh(0.8)-asech(1.2)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("(-3 - 2 * (-5 - (-7 + 3))) - (-2 - 3 * (-4 - (-5 - 2))) + (-1 - 2 * (-3 - (-4 - 1)))"))))
    print(evaluate_rpn(rev_pol_func(tokenize("tanh(2)+coth(2)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("sinh(2)+cosh(2)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("2^3+log(10)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("5-3*cosh(2)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("asec(2)+acsc(2)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("atan(1)+acot(1)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("acos(0.5)+asin(0.5)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("exp(2)*ln(3)-4"))))
    print(evaluate_rpn(rev_pol_func(tokenize("5+2*sin(3)"))))
    print(evaluate_rpn(rev_pol_func(tokenize("-5+(-3)*(5-6)*-87"))))
    print(evaluate_rpn(rev_pol_func(tokenize("sin(30)+exp(2/(3+2.3/ln(7))-1)"))))

    print(evaluate_rpn(rev_pol_func(tokenize("((exp(2) * asin(0.5) + 2 * log(100) / log(10)) / tan(2) - 1)"))))

   # print(evaluate_rpn(rev_pol_func(tokenize("(2 ^ 3 - 5) * tan(45) + 4 * (1 / 2) ^ (1 / 2) - 3 * asin(2 / 3)"))))

   # print(evaluate_rpn(rev_pol_func(tokenize("(log(1024) / log(2)) * (5 - 2 * cos(60)) + 7 * (1 / 3) ^ (1 / 2) + 2 * sinh(1)"))))

   # print(evaluate_rpn(rev_pol_func(tokenize("((3 + 2) * (1 - 2)) / (sin(5) + 2) + 4 * atan(1 / 2) - 3 * cosh(1)"))))


  #  print(evaluate_rpn(rev_pol_func(tokenize("(sinh(2) * (3 ^ 2 - 2 ^ 3) + 5 * (log(27) / log(3))) / (2 ^ 2 - 3)"))))

 #   print(evaluate_rpn(rev_pol_func(tokenize("(2 ^ (-1 / 2) + 3 ^ (-1 / 2)) / (tan(60) - cot(45)) + 2 * 2 ^ (1 / 2) - 3 * atan(1 / 3)"))))

  #  print(evaluate_rpn(rev_pol_func(tokenize("((5 - 2) * (3 + 1)) / (log(100) / log(10)) + 3 * asin(3 / 5) - 2 * sinh(1 / 2)"))))

   # print(evaluate_rpn(rev_pol_func(tokenize("(2 * sin(45) + 3 * cos(30)) / (2 ^ 2 - 3) + 4 * log(16) / log(2) - 3 * cosh(1 / 2)"))))

  #  print(evaluate_rpn(rev_pol_func(tokenize("(3 ^ 2 + 2 ^ 3) * (1 - 1 / 2) + 5 * atan(1) - 2 * sinh(1 / 2) + 3 * asin(2 / 3)"))))

   # print(evaluate_rpn(rev_pol_func(tokenize("(log(256) / log(4)) * (2 - 3 * sin(30)) + 7 * (1 / 4) ^ (1 / 2) + 2 * 2 ^ (-1) - 3 * cos(45)"))))


print(eval(f"((math.exp(2) * math.asin(0.5) + 2 * math.log(100) / math.log(10)) / (math.tan(2) - 1))"))
print(eval(f"math.exp(2)*math.asin(0.5)"))
print(eval(f"2*math.log(100)"))
print(eval(f"3.8689007262272317+9.210340371976184"))
"""
"""
print(eval(f"((2**3 - 5) * math.tan(45) + 4 * (1/2)**(1/2) - 3 * math.asin(2/3))"))

print(eval(f"((math.log(1024) / math.log(2)) * (5 - 2 * math.cos(60)) + 7 * (1/3)**(1/2) + 2 * math.sinh(1))"))

print(eval(f"(((3 + 2) * (1 - 2)) / (math.sin(5) + 2) + 4 * math.atan(1/2) - 3 * math.cosh(1))"))

print(eval(f"((math.sinh(2) * (3**2 - 2**3) + 5 * (math.log(27) / math.log(3))) / (2**2 - 3))"))

print(eval(f"((2**(-1/2) + 3**(-1/2)) / (math.tan(60) - 1/math.tan(45)) + 2 * 2**(1/2) - 3 * math.atan(1/3))"))

print(eval(f"(((5 - 2) * (3 + 1)) / (math.log(100) / math.log(10)) + 3 * math.asin(3/5) - 2 * math.sinh(1/2))"))

print(eval(f"((2 * math.sin(45) + 3 * math.cos(30)) / (2**2 - 3) + 4 * math.log(16) / math.log(2) - 3 * math.cosh(1/2))"))

print(eval(f"((3**2 + 2**3) * (1 - 1/2) + 5 * math.atan(1) - 2 * math.sinh(1/2) + 3 * math.asin(2/3))"))

print(eval(f"((math.log(256) / math.log(4)) * (2 - 3 * math.sin(30)) + 7 * (1/4)**(1/2) + 2 * 2**(-1) - 3 * math.cos(45))"))
"""
"""
print(evaluate_rpn(rev_pol_func(tokenize("(sin(45) + cos(30) * tan(60) - ln((const_e)^2))"))))
print(eval(f"(math.sin(45) + math.cos(30) * math.tan(60) - math.log(math.e**2,math.e))"))
print(evaluate_rpn(rev_pol_func(tokenize("((sec(30) + csc(45)) * (sinh(1) - cosh(2)) + log(100))"))))
print(eval(f"((1/math.cos(30) + 1/math.sin(45)) * (math.sinh(1) - math.cosh(2)) + math.log(100, 10))"))
print(evaluate_rpn(rev_pol_func(tokenize("asin(0.5) + acos(0.8) - atan(1.2) + asec(0.5)"))))
print(eval(f"(math.asin(0.5) + math.acos(0.8) - math.atan(1.2) + 1/math.cos(0.5))"))
print(evaluate_rpn(rev_pol_func(tokenize("(exp(2) * (sin(30) + cos(45)) - tanh(1.5) + coth(2.8))"))))
print(eval(f"(math.exp(2) * (math.sin(30) + math.cos(45)) - math.tanh(1.5) + 1/math.tanh(2.8))"))
print(evaluate_rpn(rev_pol_func(tokenize("acsc(0.999) + acot(2.2) - asech(2) + acsch(1.9)"))))
print(eval(f"(1/math.asin(0.999) + 1/math.atan(2.2) - 1/math.acosh(2) + 1/math.asinh(1.9))"))
print(evaluate_rpn(rev_pol_func(tokenize("(sin(60) + cos(45)) * (tan(30) - cot(60)) + ln(2.5)"))))
print(eval(f"(math.sin(60) + math.cos(45)) * (math.tan(30) - 1/math.tan(60)) + math.log(2.5,math.e)"))
print(evaluate_rpn(rev_pol_func(tokenize("cosh(2) + sinh(1) - tanh(3) + coth(4)"))))
print(eval(f"math.cosh(2) + math.sinh(1) - math.tanh(3) + 1/math.tanh(4)"))
print(evaluate_rpn(rev_pol_func(tokenize("asin(0.3) + acos(0.9) - atan(1.1) + asec(0.99)"))))
print(eval(f"math.asin(0.3) + math.acos(0.9) - math.atan(1.1) + 1/math.acos(0.99)"))
print(evaluate_rpn(rev_pol_func(tokenize("exp(1.5) * (sin(45) - cos(30)) + log(50)"))))
print(eval(f"math.exp(1.5) * (math.sin(45) - math.cos(30)) + math.log(50,10)"))
print(evaluate_rpn(rev_pol_func(tokenize("(sec(45) - csc(30)) * (sinh(2) + cosh(1)) - acsch(0.9)"))))
print(eval(f"(1/math.cos(45) - 1/math.sin(30)) * (math.sinh(2) + math.cosh(1)) - 1/math.asinh(0.9)"))
"""