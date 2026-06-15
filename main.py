import pygame
from constants import CELL_SIZE, NUMBER_OF_CELLS, SNAKE_MOVE_EVENT
from game import Game

WIDTH = NUMBER_OF_CELLS * CELL_SIZE
HEIGHT = NUMBER_OF_CELLS * CELL_SIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

game = Game(screen=screen)
pygame.time.set_timer(SNAKE_MOVE_EVENT, 100)
running = True
ai_enabled = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SNAKE_MOVE_EVENT:
            if ai_enabled:
                path = game.find_shortest_path_to_fruit(
                    target=pygame.Vector2(game.fruit.x, game.fruit.y)
                )
                if path and len(path) > 1:
                    game.snake.direction = path[1] - path[0]
                else:
                    snake_tail = game.snake.body[-1]
                    path = game.find_shortest_path_to_fruit(target=snake_tail)
                    if path and len(path) > 1:
                        game.snake.direction = path[1] - path[0]

            game.snake.move(game.snake.direction)

            if game.check_collision():
                game.snake = Game.respawn_snake(
                    screen=screen,
                    pos_x=screen.get_width() / CELL_SIZE,
                    pos_y=screen.get_height() / CELL_SIZE,
                    direction=pygame.Vector2(1, 0),
                )

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.opposite_direction_check(
                current_direction=game.snake.direction,
                new_direction=pygame.Vector2(0, -1),
            ):
                game.snake.direction = pygame.Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.opposite_direction_check(
                current_direction=game.snake.direction,
                new_direction=pygame.Vector2(0, 1),
            ):
                game.snake.direction = pygame.Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.opposite_direction_check(
                current_direction=game.snake.direction,
                new_direction=pygame.Vector2(-1, 0),
            ):
                game.snake.direction = pygame.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.opposite_direction_check(
                current_direction=game.snake.direction,
                new_direction=pygame.Vector2(1, 0),
            ):
                game.snake.direction = pygame.Vector2(1, 0)
    game.update()

pygame.quit()
