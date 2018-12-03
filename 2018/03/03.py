import re
import io
from collections import namedtuple

Coord = namedtuple('Coord', 'id, x_start, y_start, width, height')

sample_1 = io.StringIO('''
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
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

with open('input.txt') as real_input:
    lines = [line.strip() for line in real_input]

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


def gen_fabric(w, h):
    return [['.' for _ in range(w)] for y in range(h)]

def fabric_to_text(fabric):
    return '\n'.join(''.join(line) for line in fabric)


def part_one(lines):
    print('==== Part one ====')
    coords = []
    max_width = max_height = 0
    for line in lines:
        id_, x_start, y_start, w, h = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line).groups()
        coords.append(Coord(
            id=id_,
            x_start=int(x_start),
            y_start=int(y_start),
            width=int(w),
            height=int(h),
        ))
        total_width = coords[-1].x_start + coords[-1].width + 1
        total_height = coords[-1].y_start + coords[-1].height + 1
        max_width = max(total_width, max_width)
        max_height = max(total_height, max_height)

    fabric = gen_fabric(max_width, max_height)
    for coord in coords:
        for y in range(coord.y_start, coord.y_start+coord.height):
            for x in range(coord.x_start, coord.x_start+coord.width):
                if fabric[y][x] != '.':
                    fabric[y][x] = 'X'
                else:
                    fabric[y][x] = coord.id if len(coord.id) == 1 else '?'
    with open('debug.txt', 'w') as f:
        print(fabric_to_text(fabric), file=f)
    overlaps = 0
    for row in fabric:
        for col in row:
            if col == 'X':
                overlaps += 1
    print('Overlapped claims:', overlaps)

    for coord in coords:
        conflicts = False
        for y in range(coord.y_start, coord.y_start+coord.height):
            for x in range(coord.x_start, coord.x_start+coord.width):
                if fabric[y][x] == 'X':
                    conflicts = True
        if not conflicts:
            print('Non-overlapping claim:', coord.id)
    print('==== End part one ====')


def part_two(lines):
    print('==== Part two ====')
    print(lines)
    print('==== End part two ====')


print('***** Sample ******')
part_one(sample_1_lines)
part_two(sample_2_lines)
print('***** End Sample ******')

print()
print()

part_one(lines)
#part_two(lines)
