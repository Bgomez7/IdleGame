class Enemy:

    def __init__(self, screen, enemy_sprite):
        self.sprite = enemy_sprite
        self.sprite_rect = enemy_sprite.get_rect(midbottom=(screen.get_width()/2 + 100, 410))
        self.health_total = 10
        self.health_current = 10
        self.slain_count = 0
        self.souls_count = 0
