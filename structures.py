import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

front_doors_open = [False, False, False, False]  
back_doors_open = [False, False, False, False]   
garage_open = [False, False, False, False]  

house_colors = [
    (0.6, 0.8, 0.9), 
    (0.9, 0.6, 0.6),  
    (0.6, 0.9, 0.6),  
    (0.8, 0.7, 0.9)  
]

def draw_furniture():
    glColor3f(0.5, 0.3, 0.1) 
    glPushMatrix()
    glTranslatef(0, -0.5, -1.5) 
    glBegin(GL_QUADS)
    glVertex3f(-0.4, 0, -0.6)
    glVertex3f(0.4, 0, -0.6)
    glVertex3f(0.4, 0, -0.8)
    glVertex3f(-0.4, 0, -0.8)
    glEnd()
    glPopMatrix()

def draw_window_cutout(x, y):
    glPushMatrix()
    glColor3f(0, 0, 0)  
    glTranslatef(x, y, 1.01)  
    glBegin(GL_QUADS)
    glVertex3f(-0.3, -0.3, 0.0)
    glVertex3f(0.3, -0.3, 0.0)
    glVertex3f(0.3, 0.3, 0.0)
    glVertex3f(-0.3, 0.3, 0.0)
    glEnd()
    glPopMatrix()

def draw_front_wall(color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(-1, 1, 1)
    glEnd()

def draw_back_wall(color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(-1, 1, -1)
    glEnd()

def draw_side_wall(color, left=True):
    glColor3f(*color)
    glBegin(GL_QUADS)
    if left:
        glVertex3f(-1, 0, -1)
        glVertex3f(-1, 0, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)
    else:
        glVertex3f(1, 0, -1)
        glVertex3f(1, 0, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, -1)
    glEnd()

def draw_roof():
    glColor3f(0.8, 0.2, 0.2)  
    glBegin(GL_TRIANGLES)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 1.5, 0)
    glVertex3f(-1, 1, -1)
    glVertex3f(1, 1, -1)
    glVertex3f(0, 1.5, 0)
    glEnd()

    glBegin(GL_QUADS)
    glVertex3f(-1, 1, -1)
    glVertex3f(-1, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, -1)
    glEnd()

def draw_front_door(open_state):
    glColor3f(0.5, 0.3, 0.1)  
    glBegin(GL_QUADS)
    if open_state:
        glVertex3f(0.3, 0, 1.01)
        glVertex3f(0.3, 0.8, 1.01)
        glVertex3f(0.5, 0.8, 1.01)
        glVertex3f(0.5, 0, 1.01)
    else:
        glVertex3f(-0.3, 0, 1.01)
        glVertex3f(0.3, 0, 1.01)
        glVertex3f(0.3, 0.8, 1.01)
        glVertex3f(-0.3, 0.8, 1.01)
    glEnd()

def draw_back_door(open_state):
    glColor3f(0.5, 0.3, 0.1)  
    glBegin(GL_QUADS)
    if open_state:
        glVertex3f(0.3, 0, -1.01)
        glVertex3f(0.3, 0.8, -1.01)
        glVertex3f(0.5, 0.8, -1.01)
        glVertex3f(0.5, 0, -1.01)
    else:
        glVertex3f(-0.3, 0, -1.01)
        glVertex3f(0.3, 0, -1.01)
        glVertex3f(0.3, 0.8, -1.01)
        glVertex3f(-0.3, 0.8, -1.01)
    glEnd()

def draw_garage(open_state):
    glPushMatrix()
    glTranslatef(1.5, 0, 0)  
    glColor3f(0.7, 0.7, 0.7) 
    glBegin(GL_QUADS)
    glVertex3f(-0.5, 0, 1)
    glVertex3f(0.5, 0, 1)
    glVertex3f(0.5, 1, 1)
    glVertex3f(-0.5, 1, 1)
    glEnd()

    glColor3f(0.4, 0.4, 0.4) 
    glBegin(GL_QUADS)
    if open_state:
        glVertex3f(-0.4, 0.8, 1.01)
        glVertex3f(0.4, 0.8, 1.01)
        glVertex3f(0.4, 1.0, 1.01)
        glVertex3f(-0.4, 1.0, 1.01)
    else:
        glVertex3f(-0.4, 0, 1.01)
        glVertex3f(0.4, 0, 1.01)
        glVertex3f(0.4, 0.8, 1.01)
        glVertex3f(-0.4, 0.8, 1.01)
    glEnd()
    glPopMatrix()

def draw_house(x, y, z, front_door_open, back_door_open, color, garage=False, garage_open=False):
    glPushMatrix()
    glTranslatef(x, y, z)

    draw_front_wall(color)
    draw_back_wall(color)
    draw_side_wall(color, left=True)
    draw_side_wall(color, left=False)
    draw_roof()
    draw_window_cutout(-0.6, 0.6)  
    draw_window_cutout(0.6, 0.6)   
    draw_furniture()
    draw_front_door(front_door_open)
    draw_back_door(back_door_open)

    if garage:
        draw_garage(garage_open)

    glPopMatrix()

def draw_scene():
    draw_house(-6, 0, -10, front_doors_open[0], back_doors_open[0], house_colors[0])
    draw_house(-2, 0, -10, front_doors_open[1], back_doors_open[1], house_colors[1])
    draw_house(2, 0, -10, front_doors_open[2], back_doors_open[2], house_colors[2], garage=True, garage_open=garage_open[2])
    draw_house(6, 0, -10, front_doors_open[3], back_doors_open[3], house_colors[3])

def main():
    global front_doors_open, back_doors_open, garage_open
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, -1.0, -20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                # Toggle doors
                if event.key == K_1:
                    front_doors_open[0] = not front_doors_open[0]
                elif event.key == K_2:
                    back_doors_open[0] = not back_doors_open[0]
                elif event.key == K_3:
                    front_doors_open[1] = not front_doors_open[1]
                elif event.key == K_4:
                    back_doors_open[1] = not back_doors_open[1]
                elif event.key == K_5:
                    front_doors_open[2] = not front_doors_open[2]
                elif event.key == K_6:
                    back_doors_open[2] = not back_doors_open[2]
                elif event.key == K_7:
                    garage_open[2] = not garage_open[2]
                elif event.key == K_8:
                    front_doors_open[3] = not front_doors_open[3]
                elif event.key == K_9:
                    back_doors_open[3] = not back_doors_open[3]
                    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_scene()
        pygame.display.flip()

if __name__ == "__main__":
    main()
