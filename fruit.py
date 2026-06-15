import pygame
from constants import CELL_SIZE


class Fruit:
    def __init__(self, surface, x, y):
        self.surface = surface
        self.x = x
        self.y = y

    def draw(self):
        block_rect = pygame.Rect(
            (self.x * CELL_SIZE, self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        )
        pygame.draw.rect(self.surface, (87, 135, 90), block_rect)
