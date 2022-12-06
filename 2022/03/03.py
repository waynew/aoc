import io

sample = io.StringIO("""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip())

def split_sacks(sacks):
    for i in range(len(sacks)):
        mid = len(sacks[i]) // 2
        sacks[i] = sacks[i][:mid], sacks[i][mid:]
    return sacks


def items_in_both(a, b):
    return set(a).intersection(b)

def values(item):
    if 'a' <= item <= 'z':
        return ord(item) - 96
    elif 'A' <= item <= 'Z':
        return ord(item) - 38
    else:
        assert 'whooops'

def part_one(f):
    sacks = [line.strip() for line in f]
    sacks = split_sacks(sacks)
    items = [items_in_both(*sack) for sack in sacks]
    points = [[values(p) for p in stuff] for stuff in items]
    answer = sum(sum(s) for s in points)
    return answer


def group_sacks(sacks):
    for i in range(0, len(sacks), 3):
        yield sacks[i:i+3]


def badge_in_sacks(sacks):
    sets = [set(sack) for sack in sacks]
    ab = sets[0].intersection(sets[1])
    bc = sets[1].intersection(sets[2])
    stuff = sets[0].intersection(sets[1]).intersection(sets[2])
    assert ab.intersection(bc) == stuff
    return stuff


def part_two(f):
    sacks = [line.strip() for line in f]
    sacks = group_sacks(sacks)
    badges = [badge_in_sacks(group) for group in sacks]
    badge_values = [values(x) for b in badges for x in b]
    #points = [[values(p) for p in stuff] for stuff in items]
    #answer = sum(sum(s) for s in points)
    #    [values(p) for p in stuff] for stuff in badges]
    return sum(badge_values)
    points = [[values(p) for p in stuff] for stuff in items]


print(part_one(sample))
sample.seek(0)
print(part_two(sample))
with open('input.txt') as f:
    print(part_one(f))
    f.seek(0)
    print(part_two(f))
