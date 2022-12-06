import io

sample = io.StringIO('''
A Y
B X
C Z
'''.strip())

maps = {
  'A': 'rock',
  'B': 'paper',
  'C': 'scissors',
  'X': 'rock',
  'Y': 'paper',
  'Z': 'scissors',
}

beats = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper',
}

beaten_by = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors',
}

# alt: X - Rock, Y - Paper, Z - Scissors

points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}


def win_loss(f):
    for line in f:
        them, us = line.strip().split()
        them = maps[them]
        us = maps[us]
        if us == them:
            # draw
            bonus = 3
        elif beats[them] == us:
            bonus = 0
        elif beats[us] == them:
            bonus = 6
        yield points[us] + bonus


def part_two(f):
    for line in f:
        them, us = line.strip().split()
        them = maps[them]
        if us == 'X':
            # lose
            bonus = 0
            us = beats[them]
        elif us == 'Y':
            # draw
            bonus = 3
            us = them
        elif us == 'Z':
            bonus = 6
            us = beaten_by[them]
        yield points[us] + bonus

print(sum(win_loss(sample)))
sample.seek(0)
print(sum(part_two(sample)))
with open('input.txt') as f:
    print(sum(win_loss(f)))
    f.seek(0)
    print(sum(part_two(f)))
