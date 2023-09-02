import pygame.transform
from text import draw_text


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

    def health_display(self, screen):
        pygame.draw.rect(screen, 'red', pygame.rect.Rect(screen.get_width() / 2 - 100, 15, 200 * (
                self.health_current / self.health_total), 30)
        )
        pygame.draw.rect(screen, 'gold', pygame.rect.Rect(screen.get_width() / 2 - 100, 15, 200, 30), 2)
        draw_text(screen, self.health_current, 'goldenrod2', screen.get_width() / 2 - 10, 20, 24)
