from aocd import lines, submit

grid = [[int(num) for num in line] for line in lines]
x_width = len(grid)
y_width = len(grid[0])


def ray_cast(x: int, y: int, direction, limit: int):
    score = 0
    if not (x == 0 or x == x_width - 1 or y == 0 or y == y_width - 1):
        x_move = 1 if direction == "down" else -1 if direction == "up" else 0
        y_move = -1 if direction == "left" else 1 if direction == "right" else 0

        while 0 < x < x_width - 1 and 0 < y < y_width - 1:
            x += x_move
            y += y_move
            score += 1
            if grid[x][y] >= limit:
                break
    return score


highest_score = 0
for x, row in enumerate(grid):
    for y, col in enumerate(row):
        results = [
            ray_cast(x, y, "up", col),
            ray_cast(x, y, "down", col),
            ray_cast(x, y, "left", col),
            ray_cast(x, y, "right", col),
        ]
        scenic_score = results[0] * results[1] * results[2] * results[3]
        if scenic_score > highest_score:
            highest_score = scenic_score

print(highest_score)
