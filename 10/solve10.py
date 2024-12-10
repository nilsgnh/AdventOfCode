from collections import deque

with open("input.txt") as f:
    input_map = [list(line.strip()) for line in f]

for i in range(len(input_map)):
    for j in range(len(input_map[i])):
        input_map[i][j] = int(input_map[i][j])

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def trailhead_scores(grid):
    rows, cols = len(grid), len(grid[0])
    total_score = 0

    # Breitensuche
    def bfs(trailhead):
        queue = deque([trailhead])
        visited = set()
        visited.add(trailhead)
        reachable_nines = set()

        while queue:
            x, y = queue.popleft()

            if grid[x][y] == 9:
                reachable_nines.add((x, y))

            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    if (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        # print(f"({x}, {y}) -> ({nx}, {ny})")
                        # print(f"visited: {visited}")
        return len(reachable_nines)

    # für jeden Trailhead Score berechnen
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_score += bfs((r, c))
    return total_score

total_score = trailhead_scores(input_map)
print(f"Part 1: {total_score}")

# Part 2:
def trailhead_ratings(grid):
    rows, cols = len(grid), len(grid[0])
    total_rating = 0

    def dfs(x, y, visited):
        if grid[x][y] == 9:
            return 1
        
        paths = 0
        for dx, dy in DIR:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited and grid[nx][ny] == grid[x][y] + 1:
                    visited.add((nx, ny))
                    paths += dfs(nx, ny, visited)
                    # print(f"visited: {visited}")
                    visited.remove((nx, ny))
        return paths

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                total_rating += dfs(r, c, set([(r, c)]))

    return total_rating

total_rating = trailhead_ratings(input_map)
print(f"Part 2: {total_rating}")
