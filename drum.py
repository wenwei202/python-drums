from musical.theory import Note, Scale, Chord
from musical.audio import playback

from timeline import Hit, Timeline

import pygame
BD = pygame.mixer.Sound('music-as-data/samples/BassDrums1/bassdrum1.wav')
SD = pygame.mixer.Sound('music-as-data/samples/SnareDrums1/snaredrum1.wav')
HH = pygame.mixer.Sound('music-as-data/samples/HiHats1/hihat1.wav')
C1 = pygame.mixer.Sound('music-as-data/samples/Cymbals1/cymbal1.wav')
C2 = pygame.mixer.Sound('music-as-data/samples/Cymbals1/cymbal2.wav')
FT = pygame.mixer.Sound('music-as-data/samples/TomTomDrums/tomtomdrum3.wav')

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


def make_sound(type):
  mytimeline = Timeline()
  mytimeline.add(0, Hit(type, 1, sound_string[type]))
  data = mytimeline.render()
  playback.play(data)


# gap = 0.2
# guns = open('21guns.tab').readlines()
#
# for line in guns:
#   if len(line) < 2:
#     time += 64*gap
#     continue
#   if len(line) < 12:
#     time += int(line)*gap
#     continue
#   sound = sound_string[line[0:2]]
#   pos = 0.0
#   for word in line[2:]:
#     if word == "|" or word == "\n":
#       continue
#     if word == "-":
#       pos += gap
#     else:
#       add(time + pos, sound)
#       pos += gap
#
# print "Rendering audio..."
#
# data = timeline.render()
#
# print "Playing audio..."
#
# playback.play(data)
#
# print "Done!"
