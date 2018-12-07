import io
import re
from ast import literal_eval
from collections import *
from itertools import *

DAY=7

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
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
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


class Step:
    def __init__(self, id, requirements=None):
        self.id = id
        self.requirements = []
        if requirements is not None:
            self.requirements.extend(requirements)
    
    def __repr__(self):
        return f'Step(id={self.id!r}, requirements={self.requirements!r})'


Edge = namedtuple('Edge', 'step,needed_by')


class Graph(list):
    def __init__(self):
        super().__init__()

    def ordered(self):
        ordered = []
        


def part_one(lines):
    print('==== Part one ====')
    graph = Graph()
    for line in lines:
        data = line.split()
        step = data[1]
        needed_by = data[-3]
        edge = Edge(step=step, needed_by=needed_by)
        graph.append(edge)

    print(graph)
    print('==== End part one ====')


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY)
part_one(data.split('\n'))
print(f'{" Done ":*^40}')
