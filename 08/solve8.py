import itertools

with open('input.txt') as f:
    lines = f.readlines()

def split_line(line):
    line = line.strip() # entfernt \n
    return [char for char in line]

antenna_map= [split_line(line) for line in lines]
max_x = len(antenna_map[0])
max_y = len(antenna_map)

def get_antenna_positions(antenna_map):
    antenna_positions = {}
    for y, line in enumerate(antenna_map):
        for x, char in enumerate(line):
            
            if char != '.':
                antenna_positions[(x, y)] = char
    return antenna_positions

antpos = get_antenna_positions(antenna_map)

def get_antenna_pairs(antenna_positions):
    antenna_pairs = {}
    for (x1, y1), antenna1 in antenna_positions.items():
        for (x2, y2), antenna2 in antenna_positions.items():
            if (x1, y1) != (x2, y2) and antenna1 == antenna2:
                antenna_pairs[(x1, y1),(x2, y2)] = antenna1
    antenna_pairs = {tuple(sorted(pair)): antenna for pair, antenna in antenna_pairs.items()} # sortiert Tupel nach Größe, damit keine doppelten Einträge
    return antenna_pairs

antpairs = get_antenna_pairs(antpos)

def get_antinode_positions(antenna_pairs):
    antinode_positions = []
    for (x1, y1), (x2, y2) in antenna_pairs.keys():
        dx = x2 - x1
        dy = y2 - y1
        if(x1-dx < max_x and x1-dx >= 0 and y1-dy < max_y and y1-dy >= 0):
            antinode_positions.append((x1 - dx, y1 - dy))
        if(x2+dx < max_x and x2+dx >= 0 and y2+dy < max_y and y2+dy >= 0):
            antinode_positions.append((x2 + dx, y2 + dy))
    antinode_positions = list(set(antinode_positions))
    return antinode_positions

antinode_positions = get_antinode_positions(antpairs)
print(f'Part 1: {len(antinode_positions)}')

# Part 2
def get_antinode_positions2(antenna_positions):
    antinode_positions = []
    for (x1, y1), antenna1 in antenna_positions.items():
        for (x2, y2), antenna2 in antenna_positions.items():
            if (x1, y1) != (x2, y2) and antenna1 == antenna2:
                dx = x2 - x1
                dy = y2 - y1
                i=0
                while(x1-i*dx < max_x and x1-i*dx >= 0 and y1-i*dy < max_y and y1-i*dy >= 0):
                    antinode_positions.append((x1-i*dx, y1-i*dy))
                    i+=1
                i=0
                while(x2+i*dx < max_x and x2+i*dx >= 0 and y2+i*dy < max_y and y2+i*dy >= 0):
                    antinode_positions.append((x2+i*dx, y2+i*dy))
                    i+=1
    antinode_positions = list(set(antinode_positions))
    return antinode_positions

antinode_positions2 = get_antinode_positions2(antpos)
print(f'Part 2: {len(antinode_positions2)}')