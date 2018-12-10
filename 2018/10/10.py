import sys
import time
import io
import re
from ast import literal_eval
from collections import *
from itertools import *

try:
    from aocd import get_data, submit1, submit2
except:
    def get_data(day=None):
        try:
            with open('input.txt') as real_input:
                return real_input.read()
        except FileNotFoundError:
            print('WARNING: no input.txt found, just running with sample data')

sample_1 = io.StringIO('''
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
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

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


class Point:
    def __init__(self, x, y, dx, dy):
        self._x = x
        self._y = y
        self.dx = dx
        self.dy = dy
        self.offset_x = 0
        self.offset_y = 0
        self.step = 0

    @property
    def x(self):
        return self._x + self.dx * self.step

    @property
    def y(self):
        return self._y + self.dy * self.step

    @property
    def yx(self):
        return (self.y, self.x)

    @property
    def offset_yx(self):
        return (self.y+self.offset_y, self.x+self.offset_x)


def parse(line):
    _, rest = line.split('<', 1)
    pos, vel = rest.split('> velocity=<')
    vel = vel[:-1]
    position = [int(x) for x in pos.split(',')]
    velocity = [int(x) for x in vel.split(',')]
    return Point(*position, *velocity)



def do_it(lines, max_steps=5, grid_x=100, grid_y=20, file=sys.stdout):
    points = []
    for line in lines:
        points.append(parse(line))

    min_diff_x = sys.maxsize
    min_diff_y = sys.maxsize
    min_step_x = None
    min_step_y = None
    for step in range(10000):
        for point in points:
            point.step = step
        min_x = min(p.x for p in points)
        max_x = max(p.x for p in points)
        min_y = min(p.y for p in points)
        max_y = max(p.y for p in points)

        diff_x = max_x-min_x
        diff_y = max_y-min_y
        if diff_x < min_diff_x:
            min_diff_x = diff_x
            min_step_x = step

        if diff_y < min_diff_y:
            min_diff_y = diff_y
            min_step_y = step

    print(min_diff_x, min_diff_y, min_step_x, min_step_y)

    for point in points:
        point.step = min_step_x

    coords = set()
    for point in points:
        coords.add(point.offset_yx)

    grid = [
        [
            '#' if (y,x) in coords else '.'
            for x in range(grid_x)
        ]
        for y in range(grid_y)
    ]
    print('\n'.join(''.join(row) for row in grid), file=file)


print(f'{" Sample ":*^40}')
result = do_it(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data()
with open('output.txt', 'w') as f:
    result = do_it(data.split('\n'), max_steps=100, grid_x=1000, grid_y=1000, file=f)
#part_one(lines)
#submit1(result)
#submit2(result)
print(f'{" Done ":*^40}')
