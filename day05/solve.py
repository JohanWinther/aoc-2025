from pathlib import Path

inp = (Path(__file__).parent / "input.txt").read_text()
# inp = """
# 3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """[1:]


class Range:
    def __init__(self, start, stop=None):
        if stop is None:
            if isinstance(start, str):
                start, stop = map(int, start.split("-"))
            else:
                raise ValueError("start must be str if stop is None")
        if start > stop:
            raise ValueError(f"start must be less than stop: {start} > {stop}")
        self.start, self.stop = start, stop

    def __contains__(self, n):
        return self.start <= n <= self.stop

    def __add__(self, other):
        if not isinstance(other, Range):
            raise TypeError(
                f'can only concatenate range (not "{type(other).__name__}") to range'
            )
        if self.stop + 1 < other.start:
            return None
        if other.stop + 1 < self.start:
            return None
        return Range(min(self.start, other.start), max(self.stop, other.stop))

    def __eq__(self, other):
        return self.start == other.start and self.stop == other.stop

    def __lt__(self, other):
        return self.start < other.start

    def __le__(self, other):
        return self.start <= other.start

    def __gt__(self, other):
        return other.start < self.start

    def __ge__(self, other):
        return other.start <= self.start

    def __repr__(self):
        return f"{self.start}-{self.stop}"

    def __len__(self):
        return self.stop - self.start + 1


print(" Part 1 ".center(100, "-"))

fresh, ingredients = inp.split("\n\n")
ingredients = [int(i) for i in ingredients.splitlines()]
fresh = sorted([Range(r) for r in fresh.splitlines()])
fs = []
current = fresh[0]
for r in fresh[1:]:
    if (merged := current + r) is not None:
        current = merged
    else:
        fs.append(current)
        current = r
fs.append(current)

n = len(list(filter(lambda i: any(i in r for r in fs), ingredients)))
print(n)
print()


print(" Part 2 ".center(100, "-"))
n = sum(len(r) for r in fs)
print(n)
