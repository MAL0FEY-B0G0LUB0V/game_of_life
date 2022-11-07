import pygame
import field

WIDTH = 1920
HEIGHT = 1080
FPS = 60

SOMECOLOR = (120, 168, 150)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

scale = 30
offset = 1

field0 = field.Field(WIDTH, HEIGHT, scale, offset)
field0.randField()

running = True
pause = False

while running:
    clock.tick(FPS)
    screen.fill('WHITE')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_ESCAPE:
                running = False

    field0.gameOfLife(SOMECOLOR, 'BLACK', screen, pause)

    if pygame.mouse.get_pressed()[0]:
        mouseX, mouseY = pygame.mouse.get_pos()
        field0.mouse(mouseX, mouseY)

    if field0.isEnd():
        field0.randField()

    pygame.display.flip()
    pygame.display.update()
pygame.quit()

