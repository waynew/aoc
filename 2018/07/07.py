import io
import re
from ast import literal_eval
from collections import *
from itertools import *

DAY=7

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
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
'''.strip())

sample_1_lines = [line.strip() for line in sample_1]


class Step:
    def __init__(self, id, requirements=None):
        self.id = id
        self.requirements = []
        self.required_by = []

        if requirements is not None:
            self.requirements.extend(requirements)

    def __repr__(self):
        return f'Step(id={self.id!r}, requirements={self.requirements!r})'

    def blocked(self):
        return bool(self.requirements)


Dependency = namedtuple('Dependency', 'step,needed_by')


def step_time(char):
    return ord(char)-ord('A')+60


def part_one(lines):
    print('==== Part one ====')
    steps = {}
    blocked_by = defaultdict(list)
    blocking = defaultdict(list)
    steps_left = set()
    for line in lines:
        data = line.split()
        step = data[1]
        required_by = data[-3]
        steps_left.add(step)
        steps_left.add(required_by)
        steps.setdefault(step, Step(step))
        steps.setdefault(required_by, Step(required_by)).requirements.append(step)
        steps[step].required_by.append(steps[required_by])
        blocked_by[step].append(required_by)
        blocking[required_by].append(step)

    ordered = []
    result = ''
    while steps_left:
        next_step = next(iter(sorted(steps_left.difference(blocking))))
        result += next_step
        steps_left.remove(next_step)
        for blocked_step in blocked_by[next_step]:
            blocking[blocked_step].remove(next_step)
            if not blocking[blocked_step]:
                del blocking[blocked_step]
    return result
    print('==== End part one ====')


print(f'{" Sample ":*^40}')
part_one(sample_1_lines)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY)
result = part_one(data.split('\n'))
#submit1(result)
print(f'{" Done ":*^40}')
