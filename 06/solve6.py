with open('input.txt', 'r') as file:
    data = file.read().splitlines()

for i in range(len(data)):
    if '^' in data[i]:
        x = i
        y = data[i].index('^')
        start = (x, y)
        break

visited = set()
visited.add((x, y)) 

direction = (-1, 0)
map = [list(row) for row in data]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # hoch (^), rechts (>), runter (v), links (<)
direction_char = ['^', '>', 'v', '<']

while True:
    if map[x + direction[0]][y + direction[1]] == '#':
        direction = directions[(directions.index(direction) + 1) % 4]
        map[x][y] = direction_char[directions.index(direction)]
    else:
        x += direction[0]
        y += direction[1]
        visited.add((x, y))
        map[x][y] = 'X'
    if x == 0 or x == len(data) - 1 or y == 0 or y == len(data[0]) - 1:
        break

#print(visited)
print('Part 1:')
print(len(visited))

#Part 2:
possible_positions = 0
visited_obstructions_and_guard_position = set()
direction = (-1, 0)
map = [list(row) for row in data]
#print(map)

for position in visited:
    x, y = position
    if x != start[0] or y != start[1]:
        map[x][y] = 'O'
        O_pos = (x, y)

        stuck = False
        x,y = start
        while True:
            if map[x + direction[0]][y + direction[1]] == '#' or map[x + direction[0]][y + direction[1]] == 'O':
                direction = directions[(directions.index(direction) + 1) % 4]
                map[x][y] = direction_char[directions.index(direction)]
                if ((x,y), direction) in visited_obstructions_and_guard_position:
                    possible_positions += 1
                    break
                visited_obstructions_and_guard_position.add(((x,y), direction))
                #print(map)
            else:
                x += direction[0]
                y += direction[1]
            if x == 0 or x == len(data) - 1 or y == 0 or y == len(data[0]) - 1:
                break
            
        direction = (-1, 0)
        map[O_pos[0]][O_pos[1]] = 'X'
        visited_obstructions_and_guard_position.clear()

print('Part 2:')
print(possible_positions)

