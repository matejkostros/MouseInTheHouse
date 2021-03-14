"""
Simple Game project
"""
import pygame
import os, sys
from webcolors import name_to_rgb
#from PIL import Image
from GIFImage import GIFImage

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
    screen.fill(name_to_rgb('gray'))
    step = 5
    position = {"x":60, "y":60}
    dimension = {'height':30, 'width':50}
    GAME_DONE = False
    mouse_image = GIFImage("MouseSprite.gif")

    while not GAME_DONE:
        pygame.time.delay(25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GAME_DONE = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and position["x"] >= 0:
            position["x"] -= step
        if keys[pygame.K_RIGHT] and position["x"] <= SCREEN_RESOLUTION[0]:
            position["x"] += step
        if keys[pygame.K_UP] and position["y"] >= 0:
            position["y"] -= step
        if keys[pygame.K_DOWN] and position["y"] <= SCREEN_RESOLUTION[1]:
            position["y"] += step

    
        screen.fill(name_to_rgb('gray'))
        #pygame.draw.rect(screen, name_to_rgb('firebrick'), pygame.Rect(position["x"], position["y"], dimension['width'], dimension['height']), 10)
        #pygame.draw.circle(screen, name_to_rgb('firebrick'), (position["x"], position["y"]), 10)
        mouse_image.render(screen, (position["x"], position["y"]))
        pygame.display.flip()
