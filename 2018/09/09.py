import io
import re
from ast import literal_eval
from collections import *
from itertools import *

DAY=9

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


def do_it(player_count=30, last_marble=5807, debug=False):
    scores = Counter()
    for i in range(player_count):
        scores[i+1] = 0
    circle = deque()
    circle.append(0)
    high_marble = current_marble = 0
    current_player = 1
    current_rotation = 0
    while high_marble < last_marble:
        high_marble += 1
        if not high_marble % 23:
            scores[current_player] += high_marble
            circle.rotate(7)
            current_rotation += 7
            scores[current_player] += circle.pop()
            current_marble = circle[0]
        else:
            circle.rotate(-1)
            current_rotation -= 1
            circle.append(high_marble)
            current_marble = high_marble

        offset = 0
        while circle[0] != 0:
            circle.rotate(1)
            offset += 1
        if debug:
            print(current_player, '-', ' '.join(str(x) if x != current_marble else f'({current_marble})' for x in circle))
        circle.rotate(-offset)
        current_player = (current_player % player_count) + 1
    return scores



print(f'{" Sample ":*^40}')
result = do_it(9, 25, debug=False)
print(result.most_common())
#assert result.most_common(1)[0][1] == 37305, result.most_common(1)[0][1]
things = (
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
)

for player, last_marble, expected_score in things:
    result = do_it(player, last_marble)
    print(result.most_common())
    score = result.most_common(1)[0][1] 
    assert score == expected_score, f'Score was {score} not {expected_score}'
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
#data = get_data(day=DAY).split()
#player_count = int(data[0])
#last_marble = int(data[-2])
#result = do_it(player_count, last_marble)
#print(result.most_common(1))
#score = result.most_common(1)[0][1]
#
#result = do_it(player_count, last_marble*100)
#print(result.most_common(1))
#score = result.most_common(1)[0][1]
#submit1(score)
#submit2(result)
print(f'{" Done ":*^40}')
