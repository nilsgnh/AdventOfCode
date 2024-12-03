import re

def read_input():
    with open('input.txt') as f:
        return f.read()

def mult(input):
    all_muls = re.findall(r'mul\((\d+),(\d+)\)', input)
    return sum([int(x)*int(y) for x,y in all_muls])

#print(solve3('xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'), '= 161')
input_string=read_input()
print('Part 1:')
print(mult(input_string))

def split_input(input):
    return re.split(r'(do\(\)|don\'t\(\))', input)

def do_dont_mult(input):
    do = True
    result = 0
    for string in split_input(input):
        if string == 'do()':
            do = True
            #print('do')
        elif string == 'don\'t()':
            do = False
            #print('don\'t')
        else:
            if do:
                result += mult(string)

    return result

print('Part 2:')
#print(split_input('xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'))
print(do_dont_mult(input_string))