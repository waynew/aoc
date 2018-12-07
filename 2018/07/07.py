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
    return ord(char)-ord('A')+1+60


def part_one(lines, max_workers=2):
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
    workers = {}
    time = 0
    while steps_left:
        next_steps = [
            step for step in sorted(steps_left.difference(blocking))
            if step not in workers
        ]
        if next_steps and len(workers) < max_workers:
            for i in range(min(len(next_steps), max_workers-len(workers))):
                #print('Adding worker', next_steps[i], 'iter', time)
                workers[next_steps[i]] = step_time(next_steps[i])

        for s in list(workers):
            workers[s] -= 1
            if workers[s] <= 0:
                #print('Worker', s, 'done')
                del workers[s]
                steps_left.remove(s)
                result += s
                for blocked_step in blocked_by[s]:
                    blocking[blocked_step].remove(s)
                    if not blocking[blocked_step]:
                        del blocking[blocked_step]
        time += 1
    return time, result
    print('==== End part one ====')


print(f'{" Sample ":*^40}')
result = part_one(sample_1_lines)
print(result)
for c in result[1]:
    print(step_time(c))
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY)
result = part_one(data.split('\n'), max_workers=5)
print(result)
submit2(result[0])
print(f'{" Done ":*^40}')
