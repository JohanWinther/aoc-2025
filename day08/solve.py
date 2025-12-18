from functools import reduce
from itertools import combinations, islice
from math import sqrt
from operator import mul
from pathlib import Path

inp = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""[1:]
p = 10
inp, p = (Path(__file__).parent / "input.txt").read_text(), 1000


def dist(p1, p2):
    (x1, y1, z1), (x2, y2, z2) = p1, p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


print(" Part 1 ".center(100, "-"))

box2circ = {
    tuple(map(int, row.split(","))): c for c, row in enumerate(inp.splitlines())
}
circ2boxes = {c: {b} for b, c in box2circ.items()}
pairs = sorted(combinations(box2circ, 2), key=lambda t: dist(*t))
for i, (b1, b2) in zip(range(p), pairs):
    c1, c2 = box2circ[b1], box2circ[b2]
    if c1 == c2:
        continue
    for b in circ2boxes[c2]:
        box2circ[b] = c1
    circ2boxes[c1].update(circ2boxes[c2])
    del circ2boxes[c2]

n = reduce(
    mul,
    islice(
        sorted(map(len, circ2boxes.values()), reverse=True),
        3,
    ),
    1,
)
print(n)

print("")

print(" Part 2 ".center(100, "-"))

box2circ = {
    tuple(map(int, row.split(","))): c for c, row in enumerate(inp.splitlines())
}
circ2boxes = {c: {b} for b, c in box2circ.items()}
pairs = sorted(combinations(box2circ, 2), key=lambda t: dist(*t))
for i, (b1, b2) in enumerate(pairs):
    c1, c2 = box2circ[b1], box2circ[b2]
    if c1 == c2:
        continue
    for b in circ2boxes[c2]:
        box2circ[b] = c1
    circ2boxes[c1].update(circ2boxes[c2])
    del circ2boxes[c2]
    if len(circ2boxes) == 1:
        break

n = b1[0] * b2[0]
print(n)
