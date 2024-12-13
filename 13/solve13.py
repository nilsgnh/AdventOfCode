import re

with open('input.txt') as f:
    lines = f.readlines()

machines = []

pattern = r"X([+-]?\d+), Y([+-]?\d+)"

for i in range(0, len(lines), 4):
    machine = {}
    
    a_match = re.search(pattern, lines[i])
    if a_match:
        a_x, a_y = int(a_match.group(1)), int(a_match.group(2))
        machine['A'] = (a_x, a_y)
    
    b_match = re.search(pattern, lines[i+1])
    if b_match:
        b_x, b_y = int(b_match.group(1)), int(b_match.group(2))
        machine['B'] = (b_x, b_y)
    
    prize_match = re.search(r"X=([+-]?\d+), Y=([+-]?\d+)", lines[i+2])
    if prize_match:
        prize_x, prize_y = int(prize_match.group(1)), int(prize_match.group(2))
        machine['prize'] = (prize_x, prize_y)
    
    machines.append(machine)

#print(machines)

max_prizes = 0
min_ij = 1111
anztokens = 0

for machine in machines:
    a_x, a_y = machine['A']
    b_x, b_y = machine['B']
    prize_x, prize_y = machine['prize']
    
    for i in range(101):
        for j in range(101):
            if i*a_x + j*b_x == prize_x and i*a_y + j*b_y == prize_y:
                if min_ij == 1111:
                    max_prizes += 1
                if i*3 + j < min_ij:
                    min_ij = i*3 + j
                break
    
    if min_ij != 1111:
        anztokens += min_ij
        min_ij = 1111

print(max_prizes)
print(anztokens)