sample_data = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

def one(data):
    # Straightforward approach
    prev = None
    increasing = 0
    for current in data:
        if prev is not None and current > prev:
            increasing += 1
        prev = current
    return increasing


def one(data):
    # Clever approach
    return sum(data[i-1] < data[i] for i in range(1, len(data)))

def two(data):
    prev = None
    increasing = 0
    for i in range(len(data)-2):
        cur = sum(data[i:i+3])
        if prev is not None and cur > prev:
            increasing += 1
        prev = cur
    return increasing


if __name__ == '__main__':
    #print(one(sample_data));exit()
    #print(two(sample_data)); exit()
    with open('input.txt') as f:
        actual_data = [int(line) for line in f]
    print(one(actual_data))
    print(two(actual_data))
