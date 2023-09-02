#!/usr/bin/env python3

"""Idle clicker game using pygame."""

import pygame
from sprite import Sprite_Sheet

def drawText(text, color, x, y, size):
    f = pygame.font.Font("font/ThaleahFat.ttf", size)
    screen.blit(f.render(str(text), True, color), (x, y))


pygame.init()
screen = pygame.display.set_mode((640, 480))
bg = pygame.image.load('images/woodsBackground.png')
hero_sheet = Sprite_Sheet(pygame.image.load('images/HeroKnight.png'))
hero = hero_sheet.get_sprite(0, 0, 100, 55, 3, 3)

running = True

while running:
    # poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close window
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')
    screen.blit(bg, (0, 0))  # Background
    screen.blit(hero, (0,0))  # Hero
    pygame.display.flip()  # display changes to screen
