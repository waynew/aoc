from aocd import get_data, submit
from collections import Counter

DAY=4

data = get_data(year=2024, day=DAY)
sample_data =  data = '''\
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

def find_xmas(row, col, data):
    count = 0
    # Look right
    if col+3 < len(data[row]) and data[row][col:col+4] == 'XMAS':
        count += 1
    # Look left
    if col > 3 and data[row][col-4:col] == 'XMAS':
        count += 1
    # Look up
    if row > 3 and data[row-1][col] == 'M' and data[row-2][col] == 'A' and data[row-3][col] == 'S':
        count += 1
    # Look down
    if row+3 < len(data) and data[row+1][col] == 'M' and data[row+2][col] == 'A' and data[row+3][col] == 'S':
        count += 1
    # Look up left
    if col > 3 and row > 3 and data[row-1][col-1] == 'M' and data[row-2][col-2] == 'A' and data[row-3][col-3] == 'S':
        count += 1
    # Look up right
    if col+3 < len(data[row]) and row > 3 and data[row-1][col+1] == 'M' and data[row-2][col+2] == 'A' and data[row-3][col+3] == 'S':
        count += 1
    # Look down right
    elif col+3 < len(data[row]) and row+3 < len(data) and data[row+1][col+1] == 'M' and data[row+2][col+2] == 'A' and data[row+3][col+3] == 'S':
        count += 1
    # Look down left
    elif col > 3 and row+3 < len(data):
        for i in range(4):
            s = list(data[row+i])
            char = s[col]
            s[col] = f'[31;m{s[col]}[0m'
            data[row+i] = ''.join(s)
        if data[row+1][col-1] == 'M' and data[row+2][col-2] == 'A' and data[row+3][col-3] == 'S':
            count += 1
    return count

def part_one(data):
    data = [row.split() for row in data]
    count = 0
    for i, row in enumerate(data):
        #print(row)
        for j, letter in enumerate(row):
            if letter == 'X':
                count += find_xmas(row=i, col=j, data=data)
    print()
    print('\n'.join(''.join(d) for d in data))
    print(count)
    #submit(count, part="a", day=DAY, year=2024, reopen=False)

def part_two(data):
    ...
    #submit(..., part="b", day=DAY, year=2024, reopen=False)


part_one(data)
part_two(data)
