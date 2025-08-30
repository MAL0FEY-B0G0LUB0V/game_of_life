import pygame
import field
import math

FPS = 60
SOMECOLOR = (120, 168, 150)
offset = 1

TARGET_LINES = 60     # по ширине
TARGET_COLUMNS = 30   # по высоте

pygame.init()
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# вычисляем начальный scale
scale = min(WIDTH // TARGET_LINES, HEIGHT // TARGET_COLUMNS)

field0 = field.Field(WIDTH, HEIGHT, scale, offset)
field0.randField()

prev_size = (WIDTH, HEIGHT)

running = True
pause = False

while running:
    clock.tick(FPS)
    screen.fill('WHITE')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Проверка текущего размера окна
    WIDTH, HEIGHT = screen.get_size()
    if (WIDTH, HEIGHT) != prev_size:
        scale = min(WIDTH // TARGET_LINES, HEIGHT // TARGET_COLUMNS)
        new_field = field.Field(WIDTH, HEIGHT, scale, offset)

        min_lines = min(new_field.lines, field0.lines)
        min_columns = min(new_field.columns, field0.columns)

        new_field.array[:min_lines, :min_columns] = field0.array[:min_lines, :min_columns]
        field0 = new_field
        prev_size = (WIDTH, HEIGHT)

    field0.gameOfLife(SOMECOLOR, 'BLACK', screen, pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        field0.mouse(mouseX, mouseY)

    if field0.isEnd():
        field0.randField()

    pygame.display.flip()

pygame.quit()

