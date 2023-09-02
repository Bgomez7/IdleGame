import pygame.transform


class Enemy:

    def __init__(self, screen, enemy_sprite):
        self.sprite = pygame.transform.scale(
            enemy_sprite, (enemy_sprite.get_width() * .75, enemy_sprite.get_height() * .75)
        )
        self.sprite_rect = self.sprite.get_rect(midbottom=(screen.get_width()/2 + 100, screen.get_height() - 70))
        self.health_total = 10
        self.health_current = 10
        self.slain_count = 0
        self.souls_count = 0
