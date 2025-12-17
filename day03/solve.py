from pathlib import Path

inp = (Path(__file__).parent / "input.txt").read_text()
# inp = """
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """[1:]

print(" Part 1 ".center(100, "-"))


def maximum_joltage(bank: tuple[int]) -> int:
    m = len(bank) - 1
    f, s = 0, 1
    fm, sm = bank[f], bank[s]
    while f < m - 1:
        while (s < m and fm >= bank[s]) or s == m:
            sm = max(sm, bank[s])
            s += 1
        if s > m:
            break
        f = s
        fm = max(fm, bank[f])
        s = s + 1
        sm = bank[s]
    n = 10 * fm + sm
    return n


banks = [tuple(int(b) for b in bank) for bank in inp.splitlines()]
n = sum(map(maximum_joltage, banks))
print(n)
print()


print(" Part 2 ".center(100, "-"))


def print_joltage(bank: list[int], selected: list[int], joltage: str, *, hide=False):
    print("".join(str(b) for b in bank))
    print("".join("^" if i in selected else " " for i in range(len(bank))))
    if not hide:
        print(f"= {joltage}")
    print()


def maximum_joltage(bank: list[int]) -> int:
    n = 12
    descending = list(sorted(enumerate(bank), key=lambda t: t[1], reverse=True))
    joltage = ""
    selected = []
    while len(joltage) < n:
        i, j = next(
            filter(
                lambda t: t[0] not in selected
                and (not selected or selected[-1] < t[0])
                and t[0] + (n - len(joltage)) <= len(bank),
                descending,
            )
        )
        joltage += str(j)
        selected.append(i)
    print_joltage(bank, selected, joltage)
    return int(joltage)


banks = [list(int(b) for b in bank) for bank in inp.splitlines()]
n = sum(map(maximum_joltage, banks))
print(n)
