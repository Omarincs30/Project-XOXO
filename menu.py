# Omar Abdullat
# Computer Science 30
# January 25, 2021
# FINAL Project (Menu File)

# Here I imported Pygame.
import pygame, sys

mainClock = pygame. time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Omar's XO Game")
screen = pygame.display.set_mode((600, 600), 0, 100)

font = pygame. font. SysFont(None, 30)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 2, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        draw_text('MAIN MENU', font, (255, 255, 255), screen, 235, 25)
        draw_text('To start playing, click the purple rectrangle below.', font, (255, 255, 255), screen, 50, 70)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(150, 150, 300, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()

        pygame.draw.rect(screen, (22, 49, 184), button_1)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

# Here is the button function and were the game is imported.
def game():
    running = True
    while running:
        screen.fill((22, 49, 184))

        import game
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()
        mainClock.tick(60)

main_menu()
