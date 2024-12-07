from itertools import product

with open('input.txt') as f:
    lines = f.readlines()

def split_line(line):
    parts = line.split(':')
    return int(parts[0]), list(map(int, parts[1].split()))

equations = [split_line(line) for line in lines]


def evaluate(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def check_equation(target, numbers, p1):
    if p1:
        operator_combinations = product(['+', '*'], repeat=len(numbers) - 1)
    else:
        operator_combinations = product(['+', '*', '||'], repeat=len(numbers) - 1)
    
    for operators in operator_combinations:
        if evaluate(numbers, operators) == target:
            return True
    return False

# Part 1:
total = 0
for equation in equations:
    #print(equation)
    if check_equation(equation[0], equation[1], True):
        total += equation[0]
print(total)
    
# Part 2:
total = 0
for equation in equations:
    if check_equation(equation[0], equation[1], False):
        total += equation[0]
print(total)