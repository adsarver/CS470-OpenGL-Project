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
from structures import draw_street_lamp, draw_stoplight
from lighting import setup_street_lamp_light, setup_stoplight_light
is_daytime = True  # Start the scene in daytime
open_trunk = False
person_rotate = False
cat_move = False
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
def Person():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glColor3f(1.000, 0.627, 0.478)
    if person_rotate:
        glTranslatef(-1.85, 0, 0)
        for mesh in person_scene.mesh_list:
            glBegin(GL_QUADS)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*person_scene.vertices[vertex_i])
            glEnd()
    else:
        for mesh in person_scene.mesh_list:
            glBegin(GL_QUADS)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*person_scene.vertices[vertex_i])
            glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()
def arm():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glColor3f(1.000, 0.627, 0.478)
    if person_rotate:
        glTranslatef(-1.85, 0, 0)
        for mesh in arm_scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*arm_scene.vertices[vertex_i])
            glEnd()
    else: 
        for mesh in arm_scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*arm_scene.vertices[vertex_i])
            glEnd()

    glColor3f(1, 1, 1)
    glPopMatrix()
def cat():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glTranslatef(-1, 0, 2.5)
    glRotatef(1, 0, 1, 0)
    glColor3f(1, 0.5, 0)
    if cat_move:
        glTranslate(0, 0, -2)
        for mesh in cat_scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*cat_scene.vertices[vertex_i])
            glEnd()
    else: 
        for mesh in cat_scene.mesh_list:
            glBegin(GL_TRIANGLES)
            for face in mesh.faces:
                for vertex_i in face:
                    glVertex3f(*cat_scene.vertices[vertex_i])
            glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()

def main():
    # variables
    global person_rotate
    global open_trunk
    global is_daytime
    global cat_move
    
    pygame.init()
    display = (1080, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, -8, -15)
    glEnable(GL_DEPTH_TEST)

    # Set background color
    glClearColor(1.0, 0.7, 1.0, 1.0)


    # Lighting setup
    '''glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [10, 10, 10, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])'''

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
                    glTranslatef(0.5, 0, 0)  # Move right
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)  # Move up
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)  # Move down
                if event.key == pygame.K_i:
                    glTranslatef(0, 0, 1)  # Move forward
                if event.key == pygame.K_k:
                    glTranslatef(0, 0, -1)  # Move backward
                if event.key == pygame.K_a:
                    glRotatef(5, 1, 0, 0)  # Rotate around X-axis positive
                if event.key == pygame.K_d:
                    glRotatef(5, -1, 0, 0)  # Rotate around X-axis negative
                if event.key == pygame.K_w:
                    glRotatef(5, 0, 1, 0)  # Rotate around Y-axis positive
                if event.key == pygame.K_s:
                    glRotatef(5, 0, -1, 0)  # Rotate around Y-axis negative
                if event.key == pygame.K_q:
                    glRotatef(5, 0, 0, 1)  # Rotate around Z-axis positive
                if event.key == pygame.K_e:
                    glRotatef(5, 0, 0, -1)  # Rotate around Z-axis negative
                if event.key == pygame.K_t:
                    open_trunk = not open_trunk
                if event.key == K_1:
                    front_doors_open[0] = not front_doors_open[0]
                if event.key == K_2:
                    back_doors_open[0] = not back_doors_open[0]
                if event.key == K_3:
                    front_doors_open[1] = not front_doors_open[1]
                if event.key == K_4:
                    back_doors_open[1] = not back_doors_open[1]
                if event.key == K_5:
                    front_doors_open[2] = not front_doors_open[2]
                if event.key == K_6:
                    back_doors_open[2] = not back_doors_open[2]
                if event.key == K_7:
                    garage_open[2] = not garage_open[2]
                if event.key == K_8:
                    front_doors_open[3] = not front_doors_open[3]
                if event.key == K_9:
                    back_doors_open[3] = not back_doors_open[3]
                if event.key == pygame.K_n:
                    is_daytime = not is_daytime
                    setup_scene_lighting(is_daytime)  # Update lighting based on day/night
                if event.key == pygame.K_r:
                    person_rotate = not person_rotate
                if event.key == pygame.K_m:
                    cat_move = not cat_move
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #setup_scene_lighting(is_daytime)
        glPushMatrix()
        glTranslatef(0, 8, -8)
        glRotatef(90, 0, 1, 0)
        landscape.draw_scene(walls_texture, grass_texture, sky_texture)  # Landscape
        glPopMatrix()
        # structures.draw_scene()

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

        glPushMatrix()
        glTranslatef(-4, 0, -7)  # Position next to the street
        glScalef(0.5, 0.5, 0.5)  # Scale the streetlamp
        draw_street_lamp(0, 0, 0)
        setup_street_lamp_light()
        glPopMatrix()

        # Add the stoplight
        glPushMatrix()
        glTranslatef(0, 0, -7)  # Position on the street
        glScalef(0.5, 0.5, 0.5)  # Scale the stoplight
        draw_stoplight(0, 0, 0)
        setup_stoplight_light()
        glPopMatrix()


        # Add structures
        # draw_house(-5, 0, -15, False, False, (0.8, 0.7, 0.6), garage=True, garage_open=True)
        # draw_house(5, 0, -15, False, False, (0.9, 0.6, 0.6))
        # draw_tower(-10, 0, -20)
        # draw_tower(10, 0, -20)

        glPushMatrix()
        glTranslatef(0, 0, 2)
        draw_house(-6, 0, -10, front_doors_open[0], back_doors_open[0], house_colors[0])
        draw_house(-2, 0, -10, front_doors_open[1], back_doors_open[1], house_colors[1])
        draw_house(2, 0, -10, front_doors_open[2], back_doors_open[2], house_colors[2], garage=True,
                   garage_open=garage_open[2])
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

        '''glPushMatrix()
        glTranslatef(-1, 2, -6.5)
        draw_bush()
        glPopMatrix()'''
        
        # Add characters and objects
        glPushMatrix()
        glTranslatef(4, 0.75, -7.3)
        glScalef(0.2, 0.2, 0.2)
        Car()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(-3.5, 0.75, -10)
        glScalef(0.2, 0.2, 0.2)
        tree()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, 0.75, -7.3)
        glScalef(0.2, 0.2, 0.2)
        Trunk()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(0, 0.75, -7.3)
        glScalef(0.2, 0.2, 0.2)
        cat()
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, 0.75, -10.2)
        glScalef(0.2, 0.2, 0.2)
        arm()
        Person()
        glPopMatrix()
        
        # Adding Bushes to the houses
        glPushMatrix()
        glTranslatef(-1, 2, -6.5)
        draw_bush() #this does something weird to the lighting
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(-5, 2, -6.5)
        draw_bush()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef(3, 2, -6.5)  # Position the first sphere
        glColor3f(0.05, 0.4, 0.05)  # Green color
        draw_sphere(0.25, 20, 20)  # Sphere with radius 0.25, 20 slices, 20 stacks
        glTranslatef(1.0, 0.0, 0.0)  # Offset for the second sphere
        draw_sphere(0.25, 20, 20)  # Second sphere
        glPopMatrix()
        
        
        glPushMatrix()
        glTranslatef(7, 2, -6.5)
        draw_bush()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()