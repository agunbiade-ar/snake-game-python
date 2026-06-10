import pygame
from constants import NUMBER_OF_CELLS, CELL_SIZE, SNAKE_MOVE_EVENT
from game import Game
import sys

WIDTH = NUMBER_OF_CELLS * CELL_SIZE
HEIGHT = NUMBER_OF_CELLS * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game = Game(screen=screen)
pygame.time.set_timer(SNAKE_MOVE_EVENT, 100)
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SNAKE_MOVE_EVENT:
            game.snake.move(game.snake.direction)
            if game.check_collision():
                game.snake = Game.respawn_snake(screen=screen, pos_x= screen.get_width() / CELL_SIZE, pos_y=screen.get_height() / CELL_SIZE, direction=pygame.Vector2(1, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.opposite_direction_check(current_direction=game.snake.direction, new_direction=pygame.Vector2(0, -1)):
                game.snake.direction = pygame.Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.opposite_direction_check(current_direction=game.snake.direction, new_direction=pygame.Vector2(0, 1)):
                game.snake.direction = pygame.Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.opposite_direction_check(current_direction=game.snake.direction, new_direction=pygame.Vector2(-1, 0)):
                game.snake.direction = pygame.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.opposite_direction_check(current_direction=game.snake.direction, new_direction=pygame.Vector2(1,0)):
                game.snake.direction = pygame.Vector2(1, 0)
    game.update()

pygame.quit()
