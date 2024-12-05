with open('input.txt') as f:
    lines = f.readlines()

rules = []
updates = []
for line in lines:
    if '|' in line:
        rule = line.strip().split('|')
        rules.append(rule)
    else:
        update = line.strip().split(',')
        updates.append(update)

# Part 1
def check_order(update):
    for i in range(len(update)):
        for j in range(i, len(update)):
            if i == j:
                continue
            if [update[i], update[j]] in rules:
                continue
            if [update[j], update[i]] in rules:
                return False
    return True

def find_middle(updates):
    res = 0
    for update in updates:
        if check_order(update):
            middle = len(update) // 2
            #print("Current update:", update)
            if middle >= len(update):
                continue
            if update[middle] == '':
                continue
            res += int(update[middle])
    return res

print("Part 1")
print(find_middle(updates))
        
# Part 2
def correct_order(update):
    for i in range(len(update)):
        for j in range(i, len(update)):
            if i == j:
                continue
            if [update[i], update[j]] in rules:
                continue
            if [update[j], update[i]] in rules:
                update[i], update[j] = update[j], update[i]
    return update

#testupdates = []
def find_middle(updates):
    res = 0
    for update in updates:
        if not check_order(update):
            update = correct_order(update)
            #testupdates.append(update)
            middle = len(update) // 2
            #print("Current update:", update)
            if middle >= len(update):
                continue
            if update[middle] == '':
                continue
            res += int(update[middle])
    return res

print("Part 2")
print(find_middle(updates))
'''for update in testupdates:
    if(not check_order(update)):
        print("Not in order:", update)'''