import collections
from pprint import pprint

Line = collections.namedtuple('Line', 'x1, y1, x2, y2')
sample_data = [
    "0,9 -> 5,9",
    "8,0 -> 0,8",
    "9,4 -> 3,4",
    "2,2 -> 2,1",
    "7,0 -> 7,4",
    "6,4 -> 2,0",
    "0,9 -> 2,9",
    "3,4 -> 1,4",
    "0,0 -> 8,8",
    "5,5 -> 8,2",
]

def parse_input(data):
    for line in data:
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)
        #print(x1, y1, x2, y2)
        yield Line(x1, y1, x2, y2)

def print_grid(grid):
    for line in grid:
        print(' '.join('.' if not x else str(x) for x in line))

def walk(grid, coordinates, consider_diagonal=True):
    '''
    Walk provided coordinates a the provided X-Y grid. incrementing each
    point in the grid where the lines touch. Coordinates are inclusive
    endpoints. If consider_diagonal is False, ignore any line where
    x1 != x2 or y1 != y2.

     0123456789
    0..........
    1..........
    2..........
    3..........
    4..........
    5..........
    6..........
    7..........
    8..........
    9..........

    '''

    for coord in coordinates:
        if coord.x1 != coord.x2 and coord.y1 != coord.y2:
            if not consider_diagonal:
                continue

            if coord.x1 < coord.x2:
                x_dir = 1
            elif coord.x1 > coord.x2:
                x_dir = -1

            if coord.y1 < coord.y2:
                y_dir = 1
            else:
                y_dir = -1

            #print(coord)
            for mod in range(abs(coord.x1 - coord.x2)+1):
                x = coord.x1+(x_dir*mod)
                y = coord.y1+(y_dir*mod)
                #print('diag', x, y)
                grid[y][x] += 1
        else:
            x_points = sorted((coord.x1, coord.x2))
            x_points[-1] += 1
            for x in range(*x_points):
                y_points = sorted((coord.y1, coord.y2))
                y_points[-1] += 1
                for y in range(*y_points):
                    grid[y][x] += 1
        #print('*'*40)
        #print_grid(grid)
    return grid


def most_dangerous(grid, threshold=2):
    count = 0
    for row in grid:
        for col in row:
            if col >= threshold:
                count +=1
    return count


def one(data):
    coordinates = list(parse_input(data))
    max_x = 0
    max_y = 0
    for coord in coordinates:
        max_x = max(max_x, coord.x1, coord.x2)
        max_y = max(max_y, coord.y1, coord.y2)

    #print(max_x, max_y)
    grid = []
    for _ in range(max_y+1):
        grid.append([0]*(max_x+1))

    #pprint(grid)
    grid = walk(grid, coordinates)

    return most_dangerous(grid)


def two(data):
    ...


if __name__ == '__main__':
    #print(one(sample_data)); exit()
    with open('input.txt') as f:
        print(one(f))
