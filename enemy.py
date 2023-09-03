import pygame.transform
from text import draw_text


class Enemy:
    def __init__(self, screen: pygame.surface.Surface, enemy_sprite: pygame.Surface):
        """Initiate enemy variables to start of game

            screen       -- surface where enemy will be placed
            enemy_sprite -- image of enemy
        """
        # resize sprite to fit on screen better
        self.sprite = pygame.transform.scale(
            enemy_sprite, (enemy_sprite.get_width() * .75, enemy_sprite.get_height() * .75)
        )
        # get rect of sprite for easier placement on screen
        self.sprite_rect = self.sprite.get_rect(midbottom=(screen.get_width()/2 + 100, screen.get_height() - 70))
        self.health_total = 10
        self.health_current = 10
        self.slain_count = 0  # Used to calculate health of enemy
        self.souls_count = 0  # Currency for T2 upgrades

    def health_display(self, screen: pygame.surface.Surface):
        """Create HUD for enemy health on screen.

            screen -- surface where hud will be placed
        """
        # Progress bar of current health of enemy
        pygame.draw.rect(screen, 'red', pygame.rect.Rect(screen.get_width() / 2 - 100, 15, 200 * (
                self.health_current / self.health_total), 30)
        )
        # Border of bar
        pygame.draw.rect(screen, 'gold', pygame.rect.Rect(screen.get_width() / 2 - 100, 15, 200, 30), 2)
        # Text, amount of health enemy has
        draw_text(screen, self.health_current, 'goldenrod2', screen.get_width() / 2 - 10, 20, 24)

    def new_enemy(self):
        """Increase health of enemy based on enemies slain"""
        self.slain_count += 1  # used to increase health of new enemy
        self.souls_count += 1  # increase currency for slain enemy
        # quicker early game
        if self.slain_count > 10:
            self.health_total = self.health_total + self.slain_count + int(self.slain_count ** 1.5)
        else:
            self.health_total = self.health_total + 5 + self.slain_count ** 2
        # reset health to max
        self.health_current = self.health_total
