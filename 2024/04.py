import copy
from aocd import get_data, submit
from collections import Counter

DAY=4

data = get_data(year=2024, day=DAY)
sample_data = '''\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX\
'''
data = data.split()

def find_xmas(row, col, data, other_data):
    count = 0
    # Look right
    if col+3 < len(data[row]) and data[row][col+1] == 'M' and data[row][col+2] == 'A' and data[row][col+3] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row][col+1] = red('M')
        other_data[row][col+2] = red('A')
        other_data[row][col+3] = red('S')
    # Look left
    if col-3 >= 0 and data[row][col-1] == 'M' and data[row][col-2] == 'A' and data[row][col-3] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row][col-1] = red('M')
        other_data[row][col-2] = red('A')
        other_data[row][col-3] = red('S')
    # Look up
    if row-3 >= 0 and data[row-1][col] == 'M' and data[row-2][col] == 'A' and data[row-3][col] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row-1][col] = red('M')
        other_data[row-2][col] = red('A')
        other_data[row-3][col] = red('S')
    # Look down
    if row+3 < len(data) and data[row+1][col] == 'M' and data[row+2][col] == 'A' and data[row+3][col] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row+1][col] = red('M')
        other_data[row+2][col] = red('A')
        other_data[row+3][col] = red('S')
    # Look up left
    if col-3 >= 0 and row-3 >= 0 and data[row-1][col-1] == 'M' and data[row-2][col-2] == 'A' and data[row-3][col-3] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row-1][col-1] = red('M')
        other_data[row-2][col-2] = red('A')
        other_data[row-3][col-3] = red('S')
    # Look up right
    if col+3 < len(data[row]) and row-3 >= 0 and data[row-1][col+1] == 'M' and data[row-2][col+2] == 'A' and data[row-3][col+3] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row-1][col+1] = red('M')
        other_data[row-2][col+2] = red('A')
        other_data[row-3][col+3] = red('S')
    # Look down right
    if col+3 < len(data[row]) and row+3 < len(data) and data[row+1][col+1] == 'M' and data[row+2][col+2] == 'A' and data[row+3][col+3] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row+1][col+1] = red('M')
        other_data[row+2][col+2] = red('A')
        other_data[row+3][col+3] = red('S')
    # Look down left
    if col-3 >= 0  and row+3 < len(data) and data[row+1][col-1] == 'M' and data[row+2][col-2] == 'A' and data[row+3][col-3] == 'S':
        count += 1
        other_data[row][col] = red('X')
        other_data[row+1][col-1] = red('M')
        other_data[row+2][col-2] = red('A')
        other_data[row+3][col-3] = red('S')
    return count


def red(letter):
    return letter
    return f'[31;m{letter}[0m'

def part_one(data):
    data = [list(row.strip()) for row in data]
    other_data = copy.deepcopy(data)
    other_data = [['.']*len(row) for row in data]
    count = 0
    for i, row in enumerate(data):
        #print(row)
        for j, letter in enumerate(row):
            if letter == 'X':
                #other_data[i][j] = red('X')
                count += find_xmas(row=i, col=j, data=data, other_data=other_data)
    #print()
    #print('\n'.join(''.join(d) for d in data))
    #print('*'*20)
    #print('\n'.join(''.join(d) for d in other_data))
    #print(count)
    submit(count, part="a", day=DAY, year=2024, reopen=False)

def find_x_mas(row, col, data):
    front_slash = False
    back_slash = False
    if row-1 >= 0 and col+1 < len(data[row]) and row+1 < len(data) and col-1 >= 0:
    #if row+1 < len(data) and col+1 < len(data[row]):
        #   S        M
        #  A   or   A
        # M        S
        if (data[row+1][col-1] + data[row-1][col+1]) in ('MS', 'SM'):
            front_slash = True

        # M      S
        #  A  or  A
        #   S      M
        if (data[row-1][col-1] + data[row+1][col+1]) in ('MS', 'SM'):
            back_slash = True
    return front_slash and back_slash


def part_two(data):
    data = [list(row.strip()) for row in data]
    count = 0
    for i, row in enumerate(data):
        for j, letter in enumerate(row):
            if letter == 'A':
                count += find_x_mas(row=i, col=j, data=data)

    print(count)
    submit(count, part="b", day=DAY, year=2024, reopen=False)


#part_one(data)
part_two(data)
