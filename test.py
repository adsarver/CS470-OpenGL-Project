'''import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from camera import *
from landscape import *
from lighting import *
from structures import *
from characters import *
import landscape
import structures


def main():
    global open_trunk

    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    sky_texture = load_texture("Textures/clouds.jpg")
    walls_texture = load_texture("Textures/snowymountains.jpg")
    grass_texture = load_texture("Textures/grasstexture.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
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
                    if event.key == pygame.K_t:
                        open_trunk = not open_trunk
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        landscape.draw_scene(walls_texture, grass_texture, sky_texture)
        draw_lake()
        draw_road1()
        draw_road2()
        Car()
        Trunk()
        #structures.draw_scene()
        pygame.display.flip()
        pygame.time.wait(10)

main()'''
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import structures
import landscape
from landscape import *
from characters import *
from structures import *
from lighting import *

open_trunk = False
def Trunk():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glColor3f(0.58, 0.5332, 0.5332)
    if open_trunk:
        glRotatef(75, 0, 0, 1)
        glTranslatef(0.3, -0.7, 0)
        for mesh in Trunk_scene.mesh_list:
            glBegin(GL_QUADS)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*Trunk_scene.vertices[vertex_i])
            glEnd()
    else:
        for mesh in Trunk_scene.mesh_list:
            glBegin(GL_QUADS)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*Trunk_scene.vertices[vertex_i])
            glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()
    
def main():
    #variables
    global open_trunk

    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, -8, -15)
    glEnable(GL_DEPTH_TEST)

    # Set background color
    glClearColor(1.0, 0.7, 1.0, 1.0)

    # Lighting setup
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [10, 10, 10, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    # Material properties
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMateriali(GL_FRONT_AND_BACK, GL_SHININESS, 50)

    # Load textures
    sky_texture = load_texture("Textures/clouds.jpg")
    walls_texture = load_texture("Textures/snowymountains.jpg")
    grass_texture = load_texture("Textures/grasstexture.jpg")

    # Scene loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Camera movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5, 0, 0)  # Move left
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5, 0, 0)   # Move right
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)    # Move up
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)   # Move down
                if event.key == pygame.K_i:
                    glTranslatef(0, 0, 1)    # Move forward
                if event.key == pygame.K_k:
                    glTranslatef(0, 0, -1)   # Move backward
                if event.key == pygame.K_a:
                    glRotatef(5, 1, 0, 0)    # Rotate around X-axis positive
                if event.key == pygame.K_d:
                    glRotatef(5, -1, 0, 0)   # Rotate around X-axis negative
                if event.key == pygame.K_w:
                    glRotatef(5, 0, 1, 0)    # Rotate around Y-axis positive
                if event.key == pygame.K_s:
                    glRotatef(5, 0, -1, 0)   # Rotate around Y-axis negative
                if event.key == pygame.K_q:
                    glRotatef(5, 0, 0, 1)    # Rotate around Z-axis positive
                if event.key == pygame.K_e:
                    glRotatef(5, 0, 0, -1)   # Rotate around Z-axis negative
                if event.key == pygame.K_t:
                    open_trunk = not open_trunk

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glTranslatef(0, 8, -8)
        glRotatef(90, 0, 1, 0)
        landscape.draw_scene(walls_texture, grass_texture, sky_texture) # Landscape
        glPopMatrix()
        #structures.draw_scene()

        glPushMatrix()
        glTranslatef(0, 8, -8)
        glRotatef(-90, 0, 1, 0)
        glScalef(4, 4, 4)
        draw_lake()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 8, -8)
        glRotatef(-90, 0, 1, 0)
        glScalef(4, 4, 4)
        draw_road1()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(0, 8, -8)
        glRotatef(-90, 0, 1, 0)
        glScalef(4, 4, 4)
        draw_road2()
        glPopMatrix()

        # Add structures
        #draw_house(-5, 0, -15, False, False, (0.8, 0.7, 0.6), garage=True, garage_open=True)
        #draw_house(5, 0, -15, False, False, (0.9, 0.6, 0.6))
        #draw_tower(-10, 0, -20)
        #draw_tower(10, 0, -20)
        
        glPushMatrix()
        glTranslatef(0, 0, 2)
        draw_house(-6, 0, -10, front_doors_open[0], back_doors_open[0], house_colors[0])
        draw_house(-2, 0, -10, front_doors_open[1], back_doors_open[1], house_colors[1])
        draw_house(2, 0, -10, front_doors_open[2], back_doors_open[2], house_colors[2], garage=True, garage_open=garage_open[2])
        draw_house(6, 0, -10, front_doors_open[3], back_doors_open[3], house_colors[3])
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(-9, 0, 6.5)
        draw_tower(15, 0, -20)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(9, 0, 6.5)
        draw_tower(-15, 0, -20)
        glPopMatrix()

        # Add characters and objects
        glPushMatrix()
        glTranslatef(4, 0.75, -7.3)
        glScalef(0.2, 0.2, 0.2)
        Car()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, 0.75, -7.3)
        glScalef(0.2, 0.2, 0.2)
        Trunk()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, 0.75, -7.3)
        glScalef(0.2, 0.2, 0.2)
        cat()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, 0.75, -6)
        glScalef(0.2, 0.2, 0.2)
        arm()
        Person()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

       

if __name__ == "__main__":
    main()