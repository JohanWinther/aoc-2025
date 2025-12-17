from pathlib import Path

inp = (Path(__file__).parent / "input.txt").read_text()
# inp = """
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """[1:]

print(" Part 1 ".center(100, "-"))

grid = {
    (x, y): symbol
    for y, row in enumerate(inp.splitlines())
    for x, symbol in enumerate(row)
}


def accessible(position: tuple[int, int], limit: int = 4) -> bool:
    if grid[position] != "@":
        return False
    x, y = position
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    return (
        len(
            [
                None
                for dx, dy in offsets
                if (x + dx, y + dy) in grid and grid[(x + dx, y + dy)] == "@"
            ]
        )
        < limit
    )


n = len(list(filter(accessible, grid)))
print(n)
print()


print(" Part 2 ".center(100, "-"))
n = 0
while remove := list(filter(accessible, grid)):
    for p in remove:
        grid[p] = "."
        n += 1
print(n)
