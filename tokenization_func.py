#  Aim is to make a Tokenization function

function_replacements = {"acosech": "ᾳ", "asinh": "α", "acosh": "Ά", "atanh": "ᾶ", "asech": "ἀ",
                         "acoth": "ᾴ", "sinh": "Ψ", "cosh": "Φ", "tanh": "Ω", "cosech": "ξ", "sech": "ζ",
                         "coth": "Θ", "asin": "丂", "acosec": "万", "acos": "七", "atan": "丄", "asec": "丈",
                         "acot": "下", "sin": "$", "cosec": "Π", "cos": "€",
                         "tan": "Δ", "sec": "ω", "cot": "Λ",
                         "exp": "Ξ", "ln": "λ", "log": "β"}

backwards_replacement = {value: key for key, value in function_replacements.items()}


def tokenize(user_input):
    user_input = user_input.replace(" ", "")
    user_input = user_input.lower()
    for func, rep in function_replacements.items():
        user_input = user_input.replace(func, str(rep))
    tokens = []
    current_token = ""

    for char in user_input:
        if char in "+-*/()^%,ᾳαΆᾶἀᾴΨΦΩζξΘ丂七丄万丈下$€ΔΠωΛΞλβ":
            if char == "-":
                if not current_token and tokens and tokens[-1] in ["(", ",", "+", "-", "*", "/", "^"]:
                    current_token += char
                elif not current_token and user_input[0] == char:
                    current_token += char
                else:
                    if current_token:
                       tokens.append(current_token)
                    tokens.append(char)
                    current_token = ""

            else:
                if current_token:
                    tokens.append(current_token)
                tokens.append(char)
                current_token = ""
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)

    for i, char in enumerate(tokens):
        if char in backwards_replacement.keys():
            char = backwards_replacement[char]
            tokens[i] = char
    return tokens


"""
print(tokenize("(sin(x))*(cos(x))+(tanh(x))^2"))
print(tokenize("exp(2*x) + ln(x) - sin(x)"))
print(tokenize("sin(x) ^ 2 + cos(x) ^ 2"))
print(tokenize("arcsin(x) + arccos(x)"))
print(tokenize("log(x) + log(10,x)"))
print(tokenize(""))
print(tokenize("      "))
print(tokenize("sin(x"))
print(tokenize(
    "sinh(x) + cosh(x) + tanh(x) + sech(x) + cosech(x) + coth(x) + arcsin(x) + arccos(x) + arctan(x) + arccosec(x) + "
    "arcsec(x) + arccot(x) + exp(x) + ln(x) + log(x) + sin(x) + cos(x) + tan(x) + cosec(x) + sec(x) + cot(x)"))

print(tokenize("(-5)+x"))
print(tokenize("(+)"))
"""
# print(tokenize(
#   "sinh(x) + cosh(x) + tanh(x) + sech(x) + cosech(x) + coth(x) + asin(x) + acos(x) + atan(x) + acosec(x) + "
#  "asec(x) + acot(x) + exp(x) + ln(x) + log(x) + sin(x) + cos(x) + tan(x) + cosec(x) + sec(x) + cot(x)"))
"""
print(tokenize("-5+(-3)*(5-6)*-87"))
print(tokenize("5+2*sin(3)"))
print(tokenize("exp(2)*ln(3)-4"))
print(tokenize("acos(0.5)+asin(0.5)"))
print(tokenize("atan(1)+acot(1)"))
print(tokenize("asec(2)+acsc(2)"))
print(tokenize("5-3*cosh(2)"))
print(tokenize("2^3+log(10)"))
print(tokenize("sinh(2)+cosh(2)"))
print(tokenize("tanh(2)+coth(2)"))
print(tokenize("5*asech(2)-3*acoth(2)"))
"""
#print(tokenize("(-3 - 2 * (-5 - (-7 + 3))) - (-2 - 3 * (-4 - (-5 - 2))) + (-1 - 2 * (-3 - (-4 - 1)))"))