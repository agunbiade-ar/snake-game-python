from fruit import Fruit
from snake import Snake
import pygame
from constants import CELL_SIZE, NUMBER_OF_CELLS
import random
import itertools

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake_pos_x = screen.get_width() / CELL_SIZE
        self.snake_pos_y = screen.get_height() / CELL_SIZE
        self.snake = Snake(
            surface=screen, pos_x=self.snake_pos_x, pos_y=self.snake_pos_y, direction=pygame.Vector2(1, 0)
        )
        self.fruit = self.spawn_fruit()

    def opposite_direction_check(self, current_direction, new_direction):
        if current_direction + new_direction != pygame.Vector2(0,0):
            return True
        return False

    @staticmethod
    def respawn_snake(screen, pos_x, pos_y, direction):
        return Snake(screen, pos_x, pos_y, direction)

    def draw(self):
        self.snake.draw()
        self.fruit.draw()

    def set_fruit_position(self):
        positions = self.build_fruit_positions()
        choice = random.choice(positions)
        return choice

    def build_fruit_positions(self):
        possible_positions = []
        for i in range(NUMBER_OF_CELLS):
            for j in range(NUMBER_OF_CELLS):
                if pygame.Vector2(i, j) not in self.snake.body:
                    possible_positions.append(pygame.Vector2(i, j))
        return possible_positions

    def spawn_fruit(self):
        fruit_position = self.set_fruit_position()
        fruit = Fruit(surface=self.screen, pos_x=fruit_position.x, pos_y=fruit_position.y)
        return fruit

    def check_snake_self_collision(self):
        head = self.snake.body[0]
        body = itertools.islice(self.snake.body, 1, len(self.snake.body))
        
        for body_segment in body:
            if head.x == body_segment.x and head.y == body_segment.y:
                return True
        return False

    def check_snake_wall_collision(self):
        snake_head = self.snake.body[0]
        if 0 <= snake_head.x < 40 and 0 <= snake_head.y < 40:
            return False
        return True

    def check_collision(self):
        return self.check_snake_self_collision() or self.check_snake_wall_collision()

    def update(self):
        self.screen.fill((0,0,0))
        snake_ate_fruit = self.snake.eat_fruit(self.fruit)

        if snake_ate_fruit:
            self.snake.body = self.snake.grow()
            self.fruit = self.spawn_fruit()

        self.draw()
        pygame.display.flip()
