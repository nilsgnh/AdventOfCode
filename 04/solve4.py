import re

def horizontal(input, xmas):
    count = 0
    for line in input:
        count += len(re.findall(xmas, line))
    return count

def vertical(input, xmas):
    count = 0
    for i in range(len(input[0])):
        line = ''.join([input[j][i] for j in range(len(input))])
        #print(line)
        count += len(re.findall(xmas, line))
    return count

def diagonal(input, xmas):
    count = 0
    for i in range(len(input)):
        line = ''.join([input[j][j+i] for j in range(len(input)-i)])
        #print(line)
        count += len(re.findall(xmas, line))
    for i in range(1, len(input)):
        line = ''.join([input[j+i][j] for j in range(len(input)-i)])
        #print(line)
        count += len(re.findall(xmas, line))

    for i in range(len(input)):
        line = ''.join([input[j][len(input)-1-j-i] for j in range(len(input)-i)])
        #print(line)
        count += len(re.findall(xmas, line))
    for i in range(1, len(input)):
        line = ''.join([input[j+i][len(input)-1-j] for j in range(len(input)-i)])
        #print(line)
        count += len(re.findall(xmas, line))

    return count

def solve(input):
    return horizontal(input, "XMAS") + vertical(input, "XMAS") + diagonal(input, "XMAS") + diagonal(input, "SAMX") + vertical(input, "SAMX") + horizontal(input, "SAMX")

input = []
with open("input.txt") as file:
    for line in file:
        input.append(line.strip())

test = []
with open("test.txt") as file:
    for line in file:
        test.append(line.strip())

print('Part 1: ')
print(solve(test))
print(solve(input))

# Part 2
def find_mas_in_x_shape(input):
    count = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if i+2 < len(input) and j+2 < len(input[0]):
                if input[i][j] == 'M' and input[i+1][j+1] == 'A' and input[i+2][j+2] == 'S':
                    if input[i][j+2] == 'M' and input[i+1][j+1] == 'A' and input[i+2][j] == 'S':
                        count += 1
                    elif input[i][j+2] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j] == 'M':
                        count += 1
                elif input[i][j] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j+2] == 'M':
                    if input[i][j+2] == 'M' and input[i+1][j+1] == 'A' and input[i+2][j] == 'S':
                        count += 1
                    elif input[i][j+2] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j] == 'M':
                        count += 1
    return count
        

print('Part 2: ')
print(find_mas_in_x_shape(test))
print(find_mas_in_x_shape(input))