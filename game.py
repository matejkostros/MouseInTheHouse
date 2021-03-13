"""
Simple Game project
"""
import pygame
import os, sys

# Game variables
APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
GAME_NAME = 'My Game'
# ICON = os.path.join(APP_FOLDER, "icon.jpg")
ICON = 'icon.jpg'
SCREEN_RESOLUTION = (640,480)

# Settings
os.chdir(APP_FOLDER)
pygame.display.set_caption(GAME_NAME)
icon = pygame.image.load(ICON)
pygame.display.set_icon(icon)

# Game
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_RESOLUTION)
    screen.fill([220, 220, 220])
    GAME_DONE = False

    while not GAME_DONE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_DONE = True
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(60, 60, 30, 30))
        pygame.display.flip()
