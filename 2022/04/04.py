import io


sample = io.StringIO('''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''.strip())


def contains(a, b):
    if a[0] <= b[0] and b[1] <= a[1]:
        return True
    return False


def has_overlap(a, b):
    if a[0] <= b[0] <= a[1]:
        return True
    return False


def to_ranges(line):
    return [
        [int(x) for x in parts.split('-')]
        for parts in line.strip().split(',')
    ]


def part_one(file):
    overlap_count = 0
    for ranges in (to_ranges(line) for line in file):
        if contains(ranges[0], ranges[1]) or contains(ranges[1], ranges[0]):
            overlap_count += 1
            #print(ranges)
    return overlap_count


def part_two(file):
    overlap_count = 0
    for ranges in (to_ranges(line) for line in file):
        if has_overlap(ranges[0], ranges[1]) or has_overlap(ranges[1], ranges[0]):
            overlap_count += 1
            #print(ranges)
    return overlap_count


print(part_one(sample)); sample.seek(0)
print(part_two(sample)); sample.seek(0)
with open('input.txt') as f:
    print(part_one(f)); f.seek(0)
    print(part_two(f)); f.seek(0)
