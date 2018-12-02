from ast import literal_eval

seen_frequencies = set()
found = False

with open('input.txt') as f:
    frequency = 0
    for freq_change in f:
        amount = literal_eval(freq_change)
        frequency += amount
        if not found and frequency in seen_frequencies:
            found = True
            print('Second time seen:', frequency)
        seen_frequencies.add(frequency)
    print('Final frequency:', frequency)

    while not found:
        f.seek(0)
        for freq_change in f:
            amount = literal_eval(freq_change)
            frequency += amount
            if not found and frequency in seen_frequencies:
                found = True
                print('Second time seen:', frequency)
