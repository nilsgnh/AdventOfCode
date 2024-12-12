with open('input.txt') as f:
    plantmap = f.read().splitlines()

def get_neighbors(x, y):
    return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

def explore_region(x, y, visited):
    plant_type = plantmap[y][x]
    stack = [(x, y)]
    visited.add((x, y))
    area = 0
    sides = []

    while stack:
        cx, cy = stack.pop()
        area += 1

        for nx, ny in get_neighbors(cx, cy):
            if 0 <= ny < len(plantmap) and 0 <= nx < len(plantmap[0]):
                if plantmap[ny][nx] == plant_type:
                    if (nx, ny) not in visited:
                        stack.append((nx, ny))
                        visited.add((nx, ny))
                else:
                    sides.append((nx, ny, cx - nx, cy - ny))
            else:
                sides.append((nx, ny, cx - nx, cy - ny))

    return area, sides

def count_unique_sides(sides):
    unique_sides = 0

    while sides:
        unique_sides += 1
        x, y, dx, dy = sides.pop(0)
        queue = [(x, y, dx, dy)]

        while queue:
            cx, cy, cdx, cdy = queue.pop(0)
            for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
                if (nx, ny, cdx, cdy) in sides:
                    sides.remove((nx, ny, cdx, cdy))
                    queue.append((nx, ny, cdx, cdy))

    return unique_sides

visited = set()
part1_price = 0
part2_price = 0

for y in range(len(plantmap)):
    for x in range(len(plantmap[0])):
        if (x, y) not in visited:
            area, sides = explore_region(x, y, visited)

            part1_price += area * len(sides)
            
            unique_sides = count_unique_sides(sides)
            part2_price += area * unique_sides

print(f'Part 1: {part1_price}')
print(f'Part 2: {part2_price}')
