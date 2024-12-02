with open('input.txt') as f:
    lines = f.readlines()

levels = []
for line in lines:
    levels.append([int(x) for x in line.split()])

# Test, ob Zahlenreihe auf- oder absteigend sortiert ist
def is_sorted(level):
    return level == sorted(level) or level == sorted(level, reverse=True)

'''# keine benachbarten Zahlen dürfen gleich sein (nicht nötig, da check_abs abdeckt)
def no_equals(level):
    return len(set(level)) == len(level) # set() entfernt doppelte Einträge'''

# Prüfen, ob Abstand benachbarter Zahlen <= 3 oder == 0
def check_abs(level):
    for i in range(1, len(level)):
        if abs(level[i] - level[i-1]) > 3:
            return False
        if abs(level[i] - level[i-1]) == 0:
            return False
    return True

def is_valid(level):
    return is_sorted(level) and check_abs(level)

valid = 0

for level in levels:
    if is_valid(level):
        valid += 1

print("Part 1: "+ str(valid))

# Part 2
def make_valid(level):
    for i in range(len(level)):
        new_level = level[:i] + level[i+1:]
        if is_valid(new_level):
            return new_level
    return level

valid2 = 0
for level in levels:
    if is_valid(level):
        valid2 += 1
    else:
        if is_valid(make_valid(level)):
            valid2 += 1
        '''else:
            print(level)'''
        
print("Part 2: "+ str(valid2))
        