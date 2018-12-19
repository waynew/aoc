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


def smaller_grid_power(x, y, grid, size=4):
    #print(x, y, size)
    real_x = x-1
    real_y = y-1
    total_power = 0
#    if real_x == 32 and real_y == 44:
#        for col in range(real_y, real_y+size):
#            for row in range(real_x, real_x+size):
#                print(f'{grid[col][row]!s:>2}', end='  ')
#            print()
    if size < 1:
        return 0
    elif size == 1:
        #print('power:', grid[real_y][real_x])
        return grid[real_y][real_x]
    else:
        top = sum(grid[real_y][real_x:real_x+size])
        #print(x,y)
        #print(real_y+size-1)
        bottom = sum(grid[real_y+size-1][real_x:real_x+size])
        left = 0
        right = 0
        for col in range(real_y+1, real_y+size-1):
            left += grid[col][real_x]
            right += grid[col][real_x+size-1]
        #print('----')
        #print(grid[real_y][real_x:real_x+size])
        #print(grid[real_y+size-1][real_x:real_x+size])
        #print(left, right)
        #print('====')

        return top+bottom+left+right+smaller_grid_power(x+1, y+1, grid, size-2)


def do_it(grid_serial, width=300, height=300):
    # 1-based coordinate system
    maximum_grid = {'coord': None, 'power': -sys.maxsize, 'size': None}
    grid = [[0]*width for _ in range(height)]
    for x in range(1, width+1):
        for y in range(1, height+1):
            cell_power = calc_power(x,y, grid_serial)
            grid[y-1][x-1] = cell_power
            if x > 3 and y > 3:
                grid_power = smaller_grid_power(x-3, y-3, grid, size=3)
                if grid_power > maximum_grid['power']:
                    maximum_grid['power'] = grid_power
                    maximum_grid['coord'] = (x-3, y-3)
    return grid, maximum_grid


def do_it_two(grid_serial, width=300, height=300):
    maximum_grid = {'coord': None, 'power': -sys.maxsize, 'size': None}
    grid = [[0]*width for _ in range(height)]
    # 1-based coord system
    for x in range(1, width+1):
        for y in range(1, height+1):
            cell_power = calc_power(x,y, grid_serial)
            grid[y-1][x-1] = cell_power


    size = 300
    max_xy = (0,0)
    for size in range(300, 0, -1):
    #for size in range(12, 17):
        for y in range(height-size):
            for x in range(width-size):
                max_xy = (x, y)
                grid_power = smaller_grid_power(x, y, grid, size=size)
                if grid_power > maximum_grid['power']:
                    maximum_grid['power'] = grid_power
                    maximum_grid['coord'] = (x,y)
                    maximum_grid['size'] = size
        print('Processed size:', size, end='    \r')
    print()
    return grid, maximum_grid


def result_to_xy(result):
    x,y = result[1]['coord']
    return f'{x},{y}'


def result_to_xysize(result):
    x,y = result['coord']
    return f'{x},{y},{result["size"]}'


def grid_to_output(grid):
    with open('output.txt', 'w') as f:
        printf = functools.partial(print, file=f)
        for row in grid:
            for x in row:
                printf(f'{x if x > 0 else ""!s:>3}', end='')
            printf()

def main():
    result = do_it(18)
    print(result_to_xy(result))
    print(f'{" Sample ":*^40}')
    assert calc_power(3,5,8) == 4
    assert calc_power(122,79,57) == -5
    assert calc_power(217,196,39) == 0
    assert calc_power(101,153,71) == 4

    assert do_it(8)[0][5-1][3-1] == 4
    print('*'*10)
    result = do_it(18)
    print('What', result_to_xy(do_it(42)))
    print(f'{" End Sample ":*^40}')
    print('\n')

    print(f'{" Live ":*^40}')
    data = get_data(day=DAY)
    grid_serial = int(data)
    result = do_it(grid_serial)
    grid_to_output(result[0])
    print(result_to_xy(result))
    #submit1(result_to_xy(result))
    grid, result = do_it_two(grid_serial)
    print(result_to_xysize(result))
    #submit2(result_to_xysize(result))
    print(f'{" Done ":*^40}')

    #print('sample again')
    #grid, result = do_it_two(42)
    #print('Answer:', result_to_xysize(result))
    #print(smaller_grid_power(90,269, grid, size=16))

main()
