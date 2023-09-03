import pygame


def draw_text(screen: pygame.surface.Surface, text: str | int, color: str, x: float, y: float, size: int = 10):
    """Draw text on screen where directed (x, y) coordinates.

        screen  -- surface where to place text on
        text    -- string to be placed on screen
        color   -- change the appearance of the text
        x       -- x-coordinate where text will be placed
        y       -- y-coordinate where text will be placed
        size    -- (default=10) set the size of the font
    """
    f = pygame.font.Font("font/ThaleahFat.ttf", size)
    screen.blit(f.render(str(text), True, color), (x, y))
