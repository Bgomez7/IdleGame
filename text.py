import pygame

def draw_text(screen, text, color, x, y, size):
    f = pygame.font.Font("font/ThaleahFat.ttf", size)
    screen.blit(f.render(str(text), True, color), (x, y))