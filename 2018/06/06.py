import io
import re
import string
from ast import literal_eval
from collections import *
from itertools import *

sample_1 = io.StringIO('''
1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
'''.strip())

sample_2 = io.StringIO('''
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
'''.strip())

Point = namedtuple('Point', 'id,x,y')

try:
    with open('input.txt') as real_input:
        lines = [line.strip() for line in real_input]
except FileNotFoundError:
    print('WARNING: no input.txt found, just running samples')

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


def debug(grid):
    with open('output.txt', 'w') as f:
        print('\n'.join(''.join(row) for row in grid), file=f)


def distance(p1, p2):
    return abs(p1.x-p2.x) + abs(p1.y-p2.y)


def closest_to(point, points):
    distances = defaultdict(list)
    for other in points:
        distances[distance(point, other)].append(other)

    closest = min(distances)
    if len(distances[closest]) == 1:
        return distances[closest][0]
    else:
        return None


def part_one(lines):
    print('==== Part one ====')
    points = []
    for id_, line in zip(string.printable, lines):
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        points.append(Point(id=id_, x=x, y=y))

    max_x = max(p.x for p in points)
    max_y = max(p.y for p in points)
    grid = [['.']*(max_x+2) for _ in range(max_y+1)]
    by_ids = {i: v for i,v in zip(string.printable, points)}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            xy = Point(id=None,x=x,y=y)
            closest = closest_to(xy, points)
            if closest:
                grid[y][x] = closest.id


    for id_ in by_ids:
        point = by_ids[id_]
        grid[point.y][point.x] = id_

    bad_ids = set(c for c in chain(grid[0], grid[-1]))
    bad_ids.update(row[0] for row in grid)
    bad_ids.update(row[-1] for row in grid)
    bad_ids.remove('.')
    print('Discounting these:', bad_ids)
    #print(by_ids)
    #print(max_x, max_y)
    #print(len(points))
    debug(grid)
    text = ''.join(''.join(row) for row in grid)
    print('Max:', max(text.count(id_) for id_ in by_ids if id_ not in bad_ids))
    print('==== End part one ====')


def part_two(lines, limit):
    points = []
    for id_, line in zip(string.printable, lines):
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        points.append(Point(id=id_, x=x, y=y))

    max_x = max(p.x for p in points)
    max_y = max(p.y for p in points)
    grid = [['.']*(max_x+2) for _ in range(max_y+1)]
    by_ids = {i: v for i,v in zip(string.printable, points)}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            xy = Point(id=None,x=x,y=y)
            total_distance = sum(distance(xy, point) for point in points)
            if total_distance < limit:
                print(total_distance)
                grid[y][x] = '✓'
            else:
                print(total_distance)
    text = ''.join(''.join(row) for row in grid)
    print('Safe zone:', text.count('✓'))
    debug(grid)


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
part_two(sample_1_lines, limit=32)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
#part_one(lines)
part_two(lines, limit=10_000)
print(f'{" Done ":*^40}')
