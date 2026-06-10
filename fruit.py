import pygame
from constants import CELL_SIZE

class Fruit:
    def __init__(self, surface, pos_x, pos_y):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y

    def draw(self):
        block_rect = pygame.Rect((self.pos_x * CELL_SIZE, self.pos_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.surface, (87, 135, 90), block_rect)
