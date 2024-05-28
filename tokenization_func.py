#  Aim is to make a Tokenization function

function_replacements = {"sinh": "Ψ", "cosh": "Φ", "tanh": "Ω", "cosech": "ξ", "sech": "ζ",
                         "coth": "Θ", "arcsin": "丂", "arccosec": "万", "arccos": "七", "arctan": "丄", "arcsec": "丈",
                         "arccot": "下", "sin": "$", "cosec": "Π", "cos": "€",
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
        if char in "+-*/()^%,ΨΦΩζξΘ丂七丄万丈下$€ΔΠωΛΞλβ":
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
"""