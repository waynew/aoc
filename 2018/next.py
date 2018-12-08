#!/usr/bin/env python3
import sys
import os
from pathlib import Path

try:
    day = Path(sys.argv[1]).absolute()
except IndexError:
    sys.exit('Usage: next.py DAY')

print(day)
os.makedirs(day, exist_ok=True)
with open('template.py') as f:
    with open(day / f'{day.name}.py', 'w') as outf:
        outf.write(f.read().replace('DAY=0', f'DAY={day.name.strip("0")}'))
    with open(day / 'one.txt', 'w'):
        pass
    with open(day / 'two.txt', 'w'):
        pass

    input_txt = day / 'input.txt'
    if input_txt.exists():
        input_txt.unlink()
    os.symlink(day / 'one.txt', input_txt)
