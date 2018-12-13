import functools
import io
import re
import sys
from ast import literal_eval
from collections import *
from itertools import *

DAY=11

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
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
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


def calc_power(x, y, grid_serial):
    rack_id = x+10
    power_level = y * rack_id
    power_level += grid_serial
    power_level = power_level * rack_id
    power_level = int(str(power_level).zfill(3)[-3])
    power_level -= 5
    return power_level


def smaller_grid_power(x, y, grid):
    real_x = x-1
    real_y = y-1
    total_power = 0
    for y in range(real_y, real_y+3):
        for x in range(real_x, real_x+3):
            #print(f'{grid[y][x]!s:>2}', end='  ')
            total_power += grid[y][x]
        #print()
    return total_power


def do_it(grid_serial, width=300, height=300):
    # 1-based coordinate system
    maximum_grid = {'coord': None, 'power': -sys.maxsize}
    grid = [[0]*width for _ in range(height)]
    for x in range(1, width+1):
        for y in range(1, height+1):
            cell_power = calc_power(x,y, grid_serial)
            grid[y-1][x-1] = cell_power
            if x > 3 and y > 3:
                grid_power = smaller_grid_power(x-3, y-3, grid)
                if grid_power > maximum_grid['power']:
                    maximum_grid['power'] = grid_power
                    maximum_grid['coord'] = (x-3, y-3)

    return grid, maximum_grid


def result_to_xy(result):
    x,y = result[1]['coord']
    return f'{x},{y}'


print(f'{" Sample ":*^40}')
assert calc_power(3,5,8) == 4
assert calc_power(122,79,57) == -5
assert calc_power(217,196,39) == 0
assert calc_power(101,153,71) == 4

assert do_it(8)[0][5-1][3-1] == 4
print('*'*10)
result = do_it(18)
with open('output.txt', 'w') as f:
    printf = functools.partial(print, file=f)
    for row in result[0]:
        for x in row:
            printf(f'{x!s:>3}', end='')
        printf()
print('What', result_to_xy(do_it(42)))
print(f'{" End Sample ":*^40}')
print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY)
result = do_it(int(data))
print(result_to_xy(result))
#submit1(result_to_xy(result))
#submit2(result)
print(f'{" Done ":*^40}')
