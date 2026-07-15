import pygame

import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL = 20
FPS = 6

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 50, 50)
GREEN = (50, 200, 50)
GRAY = (40, 40, 40)

import os
font_path = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", "simhei.ttf")
font = pygame.font.Font(font_path, 36)
small_font = pygame.font.Font(font_path, 24)


def draw_grid():
    for x in range(0, WIDTH, CELL):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def show_score(score):
    text = small_font.render(f"得分: {score}", True, WHITE)
    screen.blit(text, (10, 5))


def show_game_over(score):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, 0))

    text = font.render("游戏结束!", True, RED)
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    screen.blit(text, rect)

    score_text = small_font.render(f"最终得分: {score}", True, WHITE)
    rect2 = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 10))
    screen.blit(score_text, rect2)

    hint = small_font.render("按 R 重新开始 / 按 ESC 退出", True, WHITE)
    rect3 = hint.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 45))
    screen.blit(hint, rect3)

    pygame.display.flip()


def random_food(snake):
    while True:
        pos = (random.randint(0, WIDTH // CELL - 1) * CELL,
               random.randint(0, HEIGHT // CELL - 1) * CELL)
        if pos not in snake:
            return pos


def main():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = (CELL, 0)
    food = random_food(snake)
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        snake = [(WIDTH // 2, HEIGHT // 2)]
                        direction = (CELL, 0)
                        food = random_food(snake)
                        score = 0
                        game_over = False
                        pygame.event.clear()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_UP and direction != (0, CELL):
                        direction = (0, -CELL)
                    elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                        direction = (0, CELL)
                    elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                        direction = (-CELL, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                        direction = (CELL, 0)
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        if game_over:
            continue

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (head[0] < 0 or head[0] >= WIDTH or
                head[1] < 0 or head[1] >= HEIGHT or
                head in snake):
            game_over = True
            show_game_over(score)
            continue

        snake.insert(0, head)

        if head == food:
            score += 10
            food = random_food(snake)
        else:
            snake.pop()

        screen.fill(BLACK)
        draw_grid()

        for i, segment in enumerate(snake):
            color = GREEN if i == 0 else (30, 160, 30)
            pygame.draw.rect(screen, color, (*segment, CELL - 1, CELL - 1))

        pygame.draw.rect(screen, RED, (*food, CELL - 1, CELL - 1))

        show_score(score)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()






