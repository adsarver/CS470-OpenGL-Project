import pygame
from OpenGL.raw.GLUT import glutSolidSphere, glutSolidCube
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

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
    glColor3f(1, 1, 1)  
    glPushMatrix()
    glTranslatef(0, 0, -0.5)

    glBegin(GL_QUADS)
    glVertex3f(-0.4, 0.3, 0)
    glVertex3f(0.4, 0.3, 0)
    glVertex3f(0.4, 0.3, -0.2)
    glVertex3f(-0.4, 0.3, -0.2)
    
    glColor3f(1, 1, 1)
    glVertex3f(-0.4, 0, 0)
    glVertex3f(-0.4, 0.3, 0)
    glVertex3f(-0.3, 0.3, 0)
    glVertex3f(-0.3, 0, 0)

    glVertex3f(0.3, 0, 0)
    glVertex3f(0.3, 0.3, 0)
    glVertex3f(0.4, 0.3, 0)
    glVertex3f(0.4, 0, 0)

    glVertex3f(-0.4, 0, -0.2)
    glVertex3f(-0.4, 0.3, -0.2)
    glVertex3f(-0.3, 0.3, -0.2)
    glVertex3f(-0.3, 0, -0.2)

    glVertex3f(0.3, 0, -0.2)
    glVertex3f(0.3, 0.3, -0.2)
    glVertex3f(0.4, 0.3, -0.2)
    glVertex3f(0.4, 0, -0.2)
    glEnd()

    glPopMatrix()


def draw_front_wall(color):
    glColor3f(*color)
    glBegin(GL_QUADS)

    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 0.3, 1)
    glVertex3f(-1, 0.3, 1)

    glVertex3f(-1, 0.3, 1)
    glVertex3f(-0.6, 0.3, 1)
    glVertex3f(-0.6, 0.7, 1)
    glVertex3f(-1, 0.7, 1)

    glVertex3f(-0.3, 0.3, 1)
    glVertex3f(0.6, 0.3, 1)
    glVertex3f(0.6, 0.7, 1)
    glVertex3f(-0.3, 0.7, 1)

    glVertex3f(-1, 0.7, 1)
    glVertex3f(1, 0.7, 1)
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
    draw_furniture()
    draw_front_door(front_door_open)
    draw_back_door(back_door_open)

    if garage:
        draw_garage(garage_open)

    glPopMatrix()

def draw_cylinder(radius, height, slices):
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(slices + 1):
        angle = 2 * np.pi * i / slices
        x = radius * np.cos(angle)
        z = radius * np.sin(angle)
        glVertex3f(x, 0, z)
        glVertex3f(x, height, z)
    glEnd()
    
    for y in (0, height):
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(0,y,0)
        for i in range(slices + 1):
            angle = 2 * np.pi * i/slices
            x = radius * np.cos(angle)
            z = radius * np.sin(angle)
            glVertex3f(x,y,z)
        glEnd()

def draw_cone(radius, height, slices):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, height, 0)
    for i in range(slices + 1):
        angle = 2 * np.pi * i / slices
        x = radius * np.cos(angle)
        z = radius * np.sin(angle)
        glVertex3f(x, 0, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(slices + 1):
        angle = 2 * np.pi * i / slices
        x = radius * np.cos(angle)
        z = radius * np.sin(angle)
        glVertex3f(x, 0, z)
    glEnd()


def draw_tower(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glColor3f(0.367, 0.367, 0.367)
    draw_cylinder(radius=1.5, height=5.0, slices=32)
    glTranslatef(0, 5, 0)
    glColor3f(0.6, 0.0, 0.0)
    draw_cone(radius=1.5, height=2.0, slices=12)
    glPopMatrix()


def draw_scene():
    draw_tower(-15, 0, -20)
    draw_house(-6, 0, -10, front_doors_open[0], back_doors_open[0], house_colors[0])
    draw_house(-2, 0, -10, front_doors_open[1], back_doors_open[1], house_colors[1])
    draw_house(2, 0, -10, front_doors_open[2], back_doors_open[2], house_colors[2], garage=True, garage_open=garage_open[2])
    draw_house(6, 0, -10, front_doors_open[3], back_doors_open[3], house_colors[3])
    draw_tower(15, 0, -20)


def draw_street_lamp(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)

    # Pole
    glColor3f(0.5, 0.5, 0.5)  # Gray
    glBegin(GL_QUADS)
    glVertex3f(-0.1, 0, 0.1)
    glVertex3f(0.1, 0, 0.1)
    glVertex3f(0.1, 3, 0.1)
    glVertex3f(-0.1, 3, 0.1)

    glVertex3f(-0.1, 0, -0.1)
    glVertex3f(0.1, 0, -0.1)
    glVertex3f(0.1, 3, -0.1)
    glVertex3f(-0.1, 3, -0.1)
    glEnd()

    # Lamp head
    glTranslatef(0, 3, 0)
    glColor3f(1.0, 1.0, 0.8)  # Light yellow for the lamp head
    draw_sphere(0.3, 20, 20)
    glPopMatrix()



def draw_stoplight(x, y, z):
    """
    Draws a stoplight at the specified position (x, y, z).
    """
    glPushMatrix()
    glTranslatef(x, y, z)

    # Pole
    glColor3f(0.5, 0.5, 0.5)  # Gray
    glBegin(GL_QUADS)
    glVertex3f(-0.1, 0, 0.1)
    glVertex3f(0.1, 0, 0.1)
    glVertex3f(0.1, 3, 0.1)
    glVertex3f(-0.1, 3, 0.1)

    glVertex3f(-0.1, 0, -0.1)
    glVertex3f(0.1, 0, -0.1)
    glVertex3f(0.1, 3, -0.1)
    glVertex3f(-0.1, 3, -0.1)
    glEnd()

    # Light Box
    glTranslatef(0, 2.5, 0)
    glColor3f(0.2, 0.2, 0.2)  # Dark gray
    draw_cube(0.5)  # Replace glutSolidCube(0.5) with draw_cube(0.5)

    # Lights
    glTranslatef(0, 0, 0.3)
    glColor3f(1, 0, 0)  # Red light
    draw_sphere(0.1, 20, 20)  # Replace glutSolidSphere with draw_sphere
    glTranslatef(0, -0.2, 0)
    glColor3f(1, 1, 0)  # Yellow light
    draw_sphere(0.1, 20, 20)
    glTranslatef(0, -0.2, 0)
    glColor3f(0, 1, 0)  # Green light
    draw_sphere(0.1, 20, 20)

    glPopMatrix()
def draw_sphere(radius, slices, stacks):
    """
    Draws a sphere using GLU (as a replacement for glutSolidSphere).
    :param radius: Radius of the sphere.
    :param slices: Number of slices (longitude divisions).
    :param stacks: Number of stacks (latitude divisions).
    """
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, slices, stacks)
    gluDeleteQuadric(quadric)

def draw_cube(size):
    """
    Draws a solid cube using OpenGL primitives.
    :param size: The length of each side of the cube.
    """
    half_size = size / 2.0

    glBegin(GL_QUADS)

    # Front face
    glVertex3f(-half_size, -half_size, half_size)
    glVertex3f(half_size, -half_size, half_size)
    glVertex3f(half_size, half_size, half_size)
    glVertex3f(-half_size, half_size, half_size)

    # Back face
    glVertex3f(-half_size, -half_size, -half_size)
    glVertex3f(-half_size, half_size, -half_size)
    glVertex3f(half_size, half_size, -half_size)
    glVertex3f(half_size, -half_size, -half_size)

    # Left face
    glVertex3f(-half_size, -half_size, -half_size)
    glVertex3f(-half_size, -half_size, half_size)
    glVertex3f(-half_size, half_size, half_size)
    glVertex3f(-half_size, half_size, -half_size)

    # Right face
    glVertex3f(half_size, -half_size, -half_size)
    glVertex3f(half_size, half_size, -half_size)
    glVertex3f(half_size, half_size, half_size)
    glVertex3f(half_size, -half_size, half_size)

    # Top face
    glVertex3f(-half_size, half_size, -half_size)
    glVertex3f(-half_size, half_size, half_size)
    glVertex3f(half_size, half_size, half_size)
    glVertex3f(half_size, half_size, -half_size)

    # Bottom face
    glVertex3f(-half_size, -half_size, -half_size)
    glVertex3f(half_size, -half_size, -half_size)
    glVertex3f(half_size, -half_size, half_size)
    glVertex3f(-half_size, -half_size, half_size)

    glEnd()

def main():
    global front_doors_open, back_doors_open, garage_open
    pygame.init()
    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
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
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,1,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-1,0)
                if event.key == pygame.K_i:
                    glTranslatef(0, 0 , 1)
                if event.key == pygame.K_k:
                    glTranslatef(0, 0 , -1)
                if event.key == pygame.K_a:
                    glRotatef(5, 1, 0, 0)
                if event.key == pygame.K_d:
                    glRotatef(5, -1, 0, 0)
                if event.key == pygame.K_w:
                    glRotatef(5, 0, 1, 0)
                if event.key == pygame.K_s:
                    glRotatef(5, 0, -1, 0)
                if event.key == pygame.K_q:
                    glRotatef(5, 0, 0, 1)
                if event.key == pygame.K_e:
                    glRotatef(5, 0, 0, -1)    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_scene()
        pygame.display.flip()
        pygame.time.wait(30)

if __name__ == "__main__":
    main()
