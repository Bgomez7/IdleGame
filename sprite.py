import pygame


class SpriteSheet:
    def __init__(self, sheet: pygame.surface.Surface):
        """Initialize an object with a sprite sheet

            sheet -- sprite sheet used to get the sprites
        """
        self.sheet = sheet

    def get_sprite(self, position_x: int, position_y: int, width: float, height: float,
                   scale_x: float, scale_y: float, set_position: int = False):
        """Return a sprite from a sprite sheet. Either by getting the exact location with setPosition = True,
            or getting the position of the sprite in relativity of the other sprites with setPosition = False.

            """
        # create surface for sprites to be placed on
        sprite = pygame.Surface((width, height))
        # if sheet is not spaced evenly per image.
        if set_position:
            # Set position where sprite is at in the sheet. Place on surface to save it.
            sprite.blit(self.sheet, (0, 0), (position_x, position_y, width, height))
        else:
            # Search through sheet and get appropriate image and size. Place on created surface to save it.
            sprite.blit(self.sheet, (0, 0), ((position_x * width), (position_y * height), width, height))
        # Rescale the size of the image.
        sprite = pygame.transform.scale(sprite, (width * scale_x, height * scale_y))
        # Removes default black color of background.
        sprite.set_colorkey('black')

        return sprite
