from pathlib import Path
from itertools import batched

inp = (Path(__file__).parent / "input.txt").read_text()
# inp = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

# Part 1


def invalid(n: int) -> bool:
    digits = str(n)
    half = len(digits) // 2
    if digits[:half] == digits[half:]:
        return True
    return False


ranges = [
    range(x, y + 1) for (x, y) in [map(int, r.split("-")) for r in inp.split(",")]
]
n = sum(filter(invalid, [id_ for r in ranges for id_ in r]))
print(n)

# Part 2


def invalid(n: int) -> bool:
    digits = str(n)
    half = len(digits) // 2
    for size in range(1, half + 1):
        if len(set(batched(digits, size))) == 1:
            return True
    return False


n = sum(filter(invalid, [id_ for r in ranges for id_ in r]))
print(n)
