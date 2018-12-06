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
            closest = min(points, key=lambda point: distance(xy, point))
            grid[y][x] = closest.id


    for id_ in by_ids:
        point = by_ids[id_]
        grid[point.y][point.x] = id_
    #print(by_ids)
    #print(max_x, max_y)
    #print(len(points))
    debug(grid)
    print('==== End part one ====')


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
#part_one(lines)
print(f'{" Done ":*^40}')
