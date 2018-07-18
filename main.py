#!/usr/bin/env python
import re

r = re.compile('(.*)\s\[(\d*)\sx\s(\d*)\sfrom\s\((\d*),\s(\d*)\)\]\n')

with open('./example.txt', 'r') as fid:
    lines = fid.readlines()

data = [[]]
for line in lines:
    if line == '\n':
        data.append([])
        continue
    m = r.match(line)
    data[-1].append([float(m.group(i)) for i in xrange(1, 6)])

data = filter(lambda x: bool(x), data)

y_thre = 300
gap_thre = 100
beat = []
for d in data:
    t = d[0][0]
    if beat and t - beat[-1] < gap_thre:
        continue
    down = False
    for hand in d:
        y = hand[2] / 2 + hand[4]
        if y > 300:
            down = True
            continue
    if down:
        beat.append(t)

print(beat)
