#!/usr/bin/env python3

"""Idle clicker game using pygame."""

import pygame
from sprite import Sprite_Sheet
from enemy import Enemy


pygame.init()
screen = pygame.display.set_mode((640, 480))
bg = pygame.image.load('images/woodsBackground.png')
hero_sheet = Sprite_Sheet(pygame.image.load('images/HeroKnight.png'))
hero = hero_sheet.get_sprite(0, 0, 100, 55, 3, 3)

enemy = Enemy(screen, pygame.image.load("images/BossMechaRattlesnake.png"))


running = True

while running:
    # poll for events
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close window
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')
    screen.blit(bg, (0, 0))  # Display Background
    screen.blit(hero, (0,0))  # Display Hero
    screen.blit(enemy.sprite, enemy.sprite_rect)  # Display Enemy
    enemy.health_display(screen)
    pygame.display.flip()  # display changes to screen
