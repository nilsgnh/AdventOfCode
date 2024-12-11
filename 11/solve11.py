def transform_stone(stone, count):
    result = {}
    if stone == 0:
        result[1] = count
    else:
        stone_str = str(stone)
        if len(stone_str) % 2 == 0:
            mid = len(stone_str) // 2
            left = int(stone_str[:mid])
            right = int(stone_str[mid:])
            if left not in result:
                result[left] = 0
            if right not in result:
                result[right] = 0
            result[left] += count
            result[right] += count
        else:
            new_stone = stone * 2024
            result[new_stone] = count
    return result

def simulate_blinks(init_stones, blink_count):
    stone_counts = {}
    for stone in init_stones:
        if stone not in stone_counts:
            stone_counts[stone] = 0
        stone_counts[stone] += 1

    for blink in range(blink_count):
        next_counts = {}
        for stone, count in stone_counts.items():
            transformed = transform_stone(stone, count)
            for new_stone, new_count in transformed.items():
                if new_stone not in next_counts:
                    next_counts[new_stone] = 0
                next_counts[new_stone] += new_count
        stone_counts = next_counts
        print(f'{blink + 1}. blink: {sum(stone_counts.values())} Steine')
    return sum(stone_counts.values())

with open('input.txt') as f:
    init_stones = list(map(int, f.read().split()))

# Part 1:
part1_result = simulate_blinks(init_stones, 25)
print(f'Part 1: {part1_result}')

# Part 2:
part2_result = simulate_blinks(init_stones, 75)
print(f'Part 2: {part2_result}')