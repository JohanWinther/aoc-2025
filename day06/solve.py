from pathlib import Path

inp = "\n".join(
    [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]
)
inp = (Path(__file__).parent / "input.txt").read_text()

print(" Part 1 ".center(100, "-"))
n = sum(
    map(
        lambda column: eval(column[-1].join(column[:-1])),
        zip(*[row.strip().split() for row in inp.splitlines()]),
    )
)
print(n)
print()

print(" Part 2 ".center(100, "-"))
n = 0
problem = []
for digits in zip(*[row[::-1] for row in inp.splitlines()]):
    number = "".join(digits).strip()
    if number:
        if number[-1] not in "*+":
            problem.append(number)
        else:
            problem.append(number[:-1])
            n += eval(number[-1].join(problem))
            problem = []
print(n)
