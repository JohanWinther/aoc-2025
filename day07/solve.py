from pathlib import Path

inp = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""[1:]
inp = (Path(__file__).parent / "input.txt").read_text()

print(" Part 1 ".center(100, "-"))

lines = inp.splitlines()[::2]
rows = [[x for x, column in enumerate(line) if column == "^"] for line in lines[1:]]
beams = {lines[0].find("S")}
n = 0
for splitters in rows:
    # Can't mutate beams while iterating it
    beams_new = beams.copy()
    for beam in beams:
        if beam in splitters:
            n += 1
            beams_new.remove(beam)
            beams_new.add(beam - 1)
            beams_new.add(beam + 1)
    beams = beams_new
print(n)

print("")

print(" Part 2 ".center(100, "-"))
beam = lines[0].find("S")
timelines = {
    (y, x): 0
    for y, line in enumerate(lines[1:])
    for x, column in enumerate(line)
    if column == "^"
}
m = max(timelines)[0]


def timelines_below(y, x):
    return next(
        (timelines[(y_, x)] for y_ in range(y + 1, m + 1) if (y_, x) in timelines),
        1,
    )


for y, x in reversed(timelines):
    timelines[(y, x)] = timelines_below(y, x - 1) + timelines_below(y, x + 1)
n = timelines[(0, beam)]
print(n)
