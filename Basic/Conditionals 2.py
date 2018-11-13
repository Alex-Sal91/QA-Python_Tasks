def conditionals2(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        return num1 + num2

print(conditionals2(2, 3))