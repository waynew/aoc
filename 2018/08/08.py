import io
import re
from ast import literal_eval
from collections import *
from itertools import *

DAY=8

try:
    from aocd import get_data
except:
    def get_data(day=None):
        try:
            with open('input.txt') as real_input:
                return real_input.read()
        except FileNotFoundError:
            print('WARNING: no input.txt found, just running with sample data')

sample_1 = io.StringIO('''
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
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


class Node:
    def __init__(self, data=None, children=None, metadata=None):
        if children and metadata:
            self.children = children
            self.metadata = metadata
        else:
            data = data[:]
            self.child_count = data.pop(0)
            self.meta_count = data.pop(0)
            self.leftover_data = data
            self.children = []
            self.metadata = []
            for _ in range(self.child_count):
                child = Node(data)
                data = child.leftover_data
                self.children.append(child)

            for _ in range(self.meta_count):
                self.metadata.append(data.pop(0))

    def __repr__(self):
        return f'Node(children={self.children!r}, metadata={self.metadata!r})'


def part_one(lines):
    print('==== Part one ====')
    result = Node([int(x) for x in lines[0].split()])
    print('==== End part one ====')
    return result


print(f'{" Sample ":*^40}')
print(part_one(sample_1_lines))
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY)
#print(part_one(data.split('\n')))
print(f'{" Done ":*^40}')
