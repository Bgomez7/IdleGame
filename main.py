#!/usr/bin/env python3

"""Idle clicker game using pygame."""

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
bg = pygame.image.load('images/woodsBackground.png')

running = True

while running:
    # poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close window
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')
    screen.blit(bg, (0, 0))
    pygame.display.flip()  # display changes to screen
