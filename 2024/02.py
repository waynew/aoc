from aocd import get_data, submit
from collections import Counter

DAY=2

reports = get_data(year=2024, day=DAY).split('\n')


def part_one(reports):
    print(len(reports))
    safe_reports = 0
    for report in reports:
        levels = [int(l) for l in report.strip().split()]
        #levels = [7,6,4,2,1]  # safe
        #levels = [1,2,7,8,9]
        #levels = [1,3,6,7,9]  # safe
        if levels[0] == levels[1]:
            # not increasing *or* decreasing
            continue
        elif levels[0] < levels[1]:
            increasing = True
        elif levels[0] > levels[1]:
            increasing = False

        #print(levels)
        for i, level in enumerate(levels[:-1]):
            next_level = levels[i+1]
            diff = abs(level - next_level)
            #print(i, level, next_level, diff)
            if 1 < diff > 3:
                break

            if increasing:
                if level >= next_level:
                    break
            else:
                if level <= next_level:
                    break
        else:
            #print('Safe')
            safe_reports += 1

    print("Safe reports:", safe_reports)
    submit(safe_reports, part="a", day=2, year=2024, reopen=False)


def is_safe(levels):
    if levels[0] == levels[1]:
        # not increasing *or* decreasing
        return False
    elif levels[0] < levels[1]:
        increasing = True
    elif levels[0] > levels[1]:
        increasing = False

    for i, level in enumerate(levels[:-1]):
        next_level = levels[i+1]
        diff = abs(level - next_level)
        #print(i, level, next_level, diff)
        if 1 < diff > 3:
            break

        if increasing:
            if level >= next_level:
                break
        else:
            if level <= next_level:
                break
    else:
        return True

    return False


def part_two(reports):
    print(len(reports))
    safe_reports = 0
    reports_ = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    for report in reports:
        levels = [int(l) for l in report.strip().split()]
        #levels = [7,6,4,2,1]  # safe
        #levels = [1,2,7,8,9]
        #levels = [1,3,6,7,9]  # safe

        #print(levels)
        if is_safe(levels):
            safe_reports += 1
        else:
            for i in range(len(levels)):
                new_levels = levels.copy()
                new_levels.pop(i)
                if is_safe(new_levels):
                    safe_reports += 1
                    break

    print("Safe reports:", safe_reports)
    submit(safe_reports, part="b", day=2, year=2024, reopen=False)


#part_one(reports)
part_two(reports)
