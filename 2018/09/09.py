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


Player = namedtuple('Player', 'id,score')


class Marble:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self


class Game:
    def __init__(self, player_count):
        self.current_marble_point = 0
        self.current_marble = Marble(self.current_marble_point)
        self.starting_marble = self.current_marble
        self.player_count = player_count
        self.current_player = 0
        self.scores = Counter()
        self._marble_count = 1
        for i in range(self.player_count):
            self.scores[i+1] = 0

    def play(self):
        pass

    def show(self):
        circle = []
        marble = self.starting_marble
        for _ in range(self._marble_count):
            circle.append(
                str(marble.value) if marble is not self.current_marble else f'({marble.value})'
            )
            marble = marble.next
        print(f'{self.current_player or "-"}: {" ".join(circle)}')

    def play(self):
        self.current_player = self.current_player % self.player_count + 1
        self.current_marble_point += 1
        if not self.current_marble_point % 23:
            self._marble_count -= 1
            self.scores[self.current_player] += self.current_marble_point
            removed_marble = self.current_marble
            for _ in range(7):
                removed_marble = removed_marble.prev
            self.scores[self.current_player] += removed_marble.value
            removed_marble.prev.next, removed_marble.next.prev = removed_marble.next, removed_marble.prev
            self.current_marble = removed_marble.next
        else:
            self._marble_count += 1
            next_marble = Marble(self.current_marble_point)
            next_marble.prev = self.current_marble.next
            next_marble.next = self.current_marble.next.next
            
            self.current_marble.next.next.prev = next_marble
            self.current_marble.next.next = next_marble
            
            self.current_marble = next_marble

    @property
    def winner(self):
        return Player(*self.scores.most_common(1)[0])


def do_it(player_count=30, last_marble=5807, debug=False, progress=False):
    g = Game(player_count)
    g.show()
    for i in range(last_marble):
        if progress and not i % 1000:
            print(f'Marble {i} played', end='\r')
        g.play()
        if debug:
            g.show()
    return g



print(f'{" Sample ":*^40}')
result = do_it(9, 25, debug=True)
print(result.winner)
things = (
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
)

for player, last_marble, expected_score in things:
    result = do_it(player, last_marble)
    assert result.winner.score == expected_score, f'Score was {result.winner.score} not {expected_score}'
    print('Checked', player, last_marble, expected_score)
print(f'{" End Sample ":*^40}')

print('\n')

print(f'{" Live ":*^40}')
data = get_data(day=DAY).split()
player_count = int(data[0])
last_marble = int(data[-2])
result = do_it(player_count, last_marble, progress=True)
#score = result.most_common(1)[0][1]
#
result = do_it(player_count, last_marble*100, progress=True)
#submit1(score)
submit2(result.winner.score)
print(f'{" Done ":*^40}')
