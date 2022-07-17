import pygame
from pygame.locals import *

pygame.init()

screen_width = 500
screen_height = 400

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in python')

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
        pygame.time.wait(100)
pygame.quit()


