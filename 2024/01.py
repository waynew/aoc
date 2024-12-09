from aocd import get_data, submit
from collections import Counter

left, right = [], []
for row in get_data(year=2024, day=1).split('\n'):
    l, r = row.split()
    left.append(int(l))
    right.append(int(r))


def part_one(left, right):
    left = sorted(left)
    right = sorted


    total = 0
    for l, r in zip(left, right):
        distance = abs(l-r)
        total += distance

    #submit(total, part="a", day=1, year=2024)


def part_two(left, right):
    right = Counter(right)
    total_score = 0
    for number in left:
        score = number * right.get(number, 0)
        total_score += score
    print(total_score)
    submit(total_score, part="b", day=1, year=2024)


#part_one(left, right)
part_two(left, right)
