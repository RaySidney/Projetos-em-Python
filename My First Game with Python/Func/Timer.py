import pygame, sys
from pygame.locals import *

cont = 1
while True:
    Tempo = pygame.time.get_ticks()/1000
    if cont == Tempo:
        cont += 1
        print(Tempo)