from pathlib import Path

inp = (Path(__file__).parent / "input.txt").read_text()

# Part 1

n = 0
dial = 50
for rot in [
    (-1 if line[:1] == "L" else 1) * int(line[1:]) for line in inp.splitlines()
]:
    dial += rot
    dial = dial % 100
    if dial == 0:
        n += 1

print(n)

# Part 2

n = 0
dial = 50
for rot in [
    i
    for line in inp.splitlines()
    for i in [(-1 if line[:1] == "L" else 1)] * int(line[1:])
]:
    dial += rot
    dial = dial % 100
    if dial == 0:
        n += 1

print(n)
