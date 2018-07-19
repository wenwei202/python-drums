#!/usr/bin/env python
import re
from musical.theory import Note, Scale, Chord
from musical.audio import playback

from timeline import Hit, Timeline

import pygame
BD = pygame.mixer.Sound('samples/BassDrums1/bassdrum1.wav')
SD = pygame.mixer.Sound('samples/SnareDrums1/snaredrum1.wav')
HH = pygame.mixer.Sound('samples/HiHats1/hihat1.wav')
C1 = pygame.mixer.Sound('samples/Cymbals1/cymbal1.wav')
C2 = pygame.mixer.Sound('samples/Cymbals1/cymbal2.wav')
FT = pygame.mixer.Sound('samples/TomTomDrums/tomtomdrum3.wav')

time = 0.0
timeline = Timeline()

sound_string = {}
sound_string[BD] = "BD"
sound_string[SD] = "SD"
sound_string[HH] = "HH"
sound_string[C1] = "C1"
sound_string[C2] = "C2"
sound_string[FT] = "FT"
sound_string["BD"] = BD
sound_string["SD"] = SD
sound_string["HH"] = HH
sound_string["C1"] = C1
sound_string["C2"] = C2
sound_string["FT"] = FT

def add(t, sound):
  timeline.add(t, Hit(sound_string[sound], 1, sound))

r = re.compile('(.*)\s\[(\d*)\sx\s(\d*)\sfrom\s\((\d*),\s(\d*)\)\]\n')

BD = pygame.mixer.Sound('samples/BassDrums1/bassdrum1.wav')


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

y_thre = 400
gap_thre = 200
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

sound = sound_string["BD"]
for b in beat:
    add(b/1000, sound)

print "Rendering audio..."

data = timeline.render()

print "Playing audio..."

playback.play(data)

print "Done!"