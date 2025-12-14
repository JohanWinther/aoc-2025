from pathlib import Path

inp = (Path(__file__).parent / "input.txt").read_text()
# inp = """
# 987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """[1:]

# Part 1


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

# Part 2
