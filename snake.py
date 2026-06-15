import pygame
from collections import deque
from constants import CELL_SIZE, NUMBER_OF_CELLS


class Snake:
    def __init__(self, surface, pos_x, pos_y, direction):
        self.surface = surface
        self.body = deque()
        self.body.append(pygame.Vector2(x=pos_x / 2, y=pos_y / 2))
        self.direction = direction

    def move(self, direction):
        head = self.body[0] + direction
        # body_iter = iter(self.body)
        self.body.appendleft(head)
        self.body.pop()

    def eat_fruit(self, fruit):
        head = self.body[0]
        if head.x == fruit.x and head.y == fruit.y:
            return True
        return False

    def grow(self):
        new_tail = self.body[-1]
        self.body.append(new_tail)
        return self.body

    def draw(self):
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(self.surface, (255, 255, 255), block_rect)
