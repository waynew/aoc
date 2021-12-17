sample_data = [
    '00100',
    '11110',
    '10110',
    '10111',
    '10101',
    '01111',
    '00111',
    '11100',
    '10000',
    '11001',
    '00010',
    '01010',
]

def one(data):
    _0_counts = [0]*len(data[0])
    _1_counts = [0]*len(data[0])
    for line in data:
        for i, val in enumerate(line.strip()):
            if val == '1':
                _1_counts[i] += 1
            elif val == '0':
                _0_counts[i] += 1

    nums = []
    #print(_0_counts)
    #print(_1_counts)
    for _0, _1 in zip(_0_counts, _1_counts):
        if _0 > _1:
            nums.append('0')
        elif _0 < _1:
            nums.append('1')
        else:
            print(_0, _1)
            raise Exception('Oops!')
    gamma_rate = int(''.join(nums), 2)
    #print(bin(gamma_rate))
    epsilon_rate = gamma_rate ^ int('1'*len(data[0]), 2)
    #print(bin(epsilon_rate))
    power_consumption = gamma_rate * epsilon_rate
    return power_consumption


def two(data):
    i = 0
    ones = []
    zeroes = []

    for line in data:
        if line[i] == '1':
            ones.append(line)
        else:
            zeroes.append(line)

    if actual_o2 is None and len(ones) == 1:
        actual_o2 = int(ones[0], 2)
    elif len(zeroes) > len(ones):
        possible_o2 = zeroes
    else:
        possible_o2 = ones

    if actual_co2 is None and len(zeroes) == 1:
        actual_o2 = int(zeroes[0], 2)
    elif len(zeroes) > len(ones):
        possible_co2 = ones
    else:
        possible_co2 = zeroes


    print(possible_o2)
    print(possible_co2)


def largest(data, i=0):
    ones = []
    zeroes = []
    for line in data:
        if line[i] == '1':
            ones.append(line)
        else:
            zeroes.append(line)

    if len(ones) == 1:
        return int(ones[0], 2)
    elif len(zeroes) > len(ones):
        return largest(zeroes, i+1)
    else:
        return largest(ones, i+1)

def smallest(data, i=0):
    ones = []
    zeroes = []
    for line in data:
        if line[i] == '1':
            ones.append(line)
        else:
            zeroes.append(line)

    if len(zeroes) == 1:
        return int(zeroes[0], 2)
    elif len(zeroes) > len(ones):
        return smallest(ones, i+1)
    else:
        return smallest(zeroes, i+1)



def two(data):
    o2_rating = largest(data)
    co2_rating = smallest(data)
    print('o2:', o2_rating)
    print('co2:', co2_rating)
    return o2_rating*co2_rating



if __name__ == '__main__':
    #print(one(sample_data)); exit()
    #print(two(sample_data)); exit()
    with open('input.txt') as f:
        data = [line.strip() for line in f]

    print(one(data))
    print(two(data))
