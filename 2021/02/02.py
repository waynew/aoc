sample = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2',
]


def one(data):
    pos = {'horiz': 0, 'depth': 0}
    for thing in data:
        direction, velocity = thing.strip().split()
        velocity = int(velocity)
        if direction == 'forward':
            h = 1
            pos['horiz'] += velocity * h
        elif direction == 'down':
            v = 1
            pos['depth'] += velocity * v
        elif direction == 'up':
            v = -1
            pos['depth'] += velocity * v
        #print(f"{direction:<8}, {velocity}, {pos}")
    #print(pos)
    result = pos['depth'] * pos['horiz']
    return result


def two(data):
    pos = {'horiz': 0, 'depth': 0}
    aim = 0
    for thing in data:
        direction, velocity = thing.strip().split()
        velocity = int(velocity)
        if direction == 'forward':
            pos['horiz'] += velocity
            pos['depth'] += aim * velocity
        elif direction == 'down':
            aim += velocity
        elif direction == 'up':
            aim -= velocity
        #print(f"{direction:<8}, {velocity}, {pos}")
    #print(pos)
    result = pos['depth'] * pos['horiz']
    return result



if __name__ == '__main__':
    #print(one(sample)); exit()
    #print(two(sample)); exit()
    with open('input.txt') as f:
        print(one(f))
        f.seek(0)
        print(two(f))
