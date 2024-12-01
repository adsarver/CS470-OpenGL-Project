import camera, landscape, lighting, structures
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

DISPLAY_RES = (1200, 800)


def main():
    pygame.init()
    pygame.display.set_mode(DISPLAY_RES, DOUBLEBUF | OPENGL)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Get input keys
        keys = pygame.key.get_pressed()
        
        pygame.display.flip()
        pygame.time.wait(10)
        
main()