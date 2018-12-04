import re
import io
from collections import Counter, defaultdict
from datetime import datetime, timedelta

DATE_PATTERN = '%Y-%m-%d %H:%M'

sample_1 = io.StringIO('''
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
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

with open('input.txt') as real_input:
    lines = [line.strip() for line in real_input]

sample_1_lines = [line.strip() for line in sample_1]
sample_2_lines = [line.strip() for line in sample_2]


def parse_line(line):
    timestamp = line[1:17]
    return timestamp, line[19:]


def shifts(lines):
    shift = []
    guard_id = None
    for line in lines:
        timestamp, rest = parse_line(line)
        if rest.startswith('Guard'):
            if guard_id is not None:
                yield shift
                shift = []
            guard_id = rest.split(None, 2)[1]
        shift.append((timestamp, rest))
    yield shift

def part_one(lines):
    print('==== Part one ====')
    lines.sort()
    sleepy_times = Counter()
    current_guard = None
    asleeps_on = defaultdict(Counter)
    for shift in shifts(lines):
        guard_id = shift[0][1].split(None, maxsplit=2)[1]
        total_sleep = timedelta(minutes=0)
        for sleep, wake in zip(*[iter(shift[1:])]*2):
            sleep_time = datetime.strptime(sleep[0], DATE_PATTERN)
            wake_time = datetime.strptime(wake[0], DATE_PATTERN)
            time_asleep = wake_time-sleep_time
            total_sleep += time_asleep
            try:
                sleepy_times[guard_id] += time_asleep
            except TypeError:
                sleepy_times[guard_id] = time_asleep
            minutes = int(time_asleep.total_seconds() / 60)
            for minute in range(minutes):
                asleeps_on[guard_id][(sleep_time+timedelta(minutes=minute)).time()] += 1
    most_common_sleep_time = (None, None, -1)
    for guard_id in sleepy_times:
        guards_most_common_sleep_time = asleeps_on[guard_id].most_common(1)[0]
        if most_common_sleep_time[2] < guards_most_common_sleep_time[1]:
            most_common_sleep_time = (guard_id, *guards_most_common_sleep_time)
    print('Most common sleep time', most_common_sleep_time)
    guard_id = int(most_common_sleep_time[0][1:])
    sleep_minute = most_common_sleep_time[1].minute
    print('Result:', guard_id * sleep_minute)

    most_sleepy_guard = sleepy_times.most_common(1)
    print('Sleepiest guard:', most_sleepy_guard)
    guard_id = most_sleepy_guard[0][0]
    print('Guard ID:', guard_id[0])
    print('Sleepiest guard most common sleep time:', asleeps_on[guard_id].most_common(1))
    print('Result:', int(guard_id[1:])*asleeps_on[guard_id].most_common(1)[0][0].minute)
    print('==== End part one ====')


def part_two(lines):
    print('==== Part two ====')
    print(lines)
    print('==== End part two ====')


print('***** Sample ******')
part_one(sample_1_lines)
part_two(sample_2_lines)
print('***** End Sample ******')

print()
print()

part_one(lines)
#part_two(lines)
