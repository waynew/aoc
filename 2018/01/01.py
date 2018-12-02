from ast import literal_eval

with open('input.txt') as f:
    print(sum(literal_eval(freq_change.strip()) for freq_change in f))
