import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

scale = 8

scene_vertices = {
    "walls": [
        # Front face
        [-scale, -scale, scale, 0, 0], [scale, -scale, scale, 1, 0],
        [scale, scale, scale, 1, 1], [-scale, scale, scale, 0, 1],

        # Back face
        [scale, -scale, -scale, 0, 0], [-scale, -scale, -scale, 1, 0],
        [-scale, scale, -scale, 1, 1], [scale, scale, -scale, 0, 1],

        # Left face
        [-scale, -scale, -scale, 0, 0], [-scale, -scale, scale, 1, 0],
        [-scale, scale, scale, 1, 1], [-scale, scale, -scale, 0, 1],

        # Right face
        [scale, -scale, scale, 0, 0], [scale, -scale, -scale, 1, 0],
        [scale, scale, -scale, 1, 1], [scale, scale, scale, 0, 1],
    ],
    "ground": [
        # Bottom face
        [-scale, -scale, -scale, 0, 0], [scale, -scale, -scale, 1, 0],
        [scale, -scale, scale, 1, 1], [-scale, -scale, scale, 0, 1],
    ],
    "sky": [
        # Top face
        [-scale, scale, scale, 0, 0], [scale, scale, scale, 1, 0],
        [scale, scale, -scale, 1, 1], [-scale, scale, -scale, 0, 1],
    ]
}

def load_texture(file_path):
    image = pygame.image.load(file_path)
    img_data = pygame.image.tostring(image, "RGBA", True)
    width, height = image.get_size()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glBindTexture(GL_TEXTURE_2D, 0)
    
    return texture_id

def draw_scene(walls_texture, ground_texture, sky_texture):
    glDisable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, walls_texture)
    glBegin(GL_QUADS)
    for i in range(0, len(scene_vertices["walls"]), 4):
        for vertex in scene_vertices["walls"][i:i+4]:
            glTexCoord2f(vertex[3], vertex[4])
            glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    glBindTexture(GL_TEXTURE_2D, ground_texture)
    glBegin(GL_QUADS)
    for vertex in scene_vertices["ground"]:
        glTexCoord2f(vertex[3], vertex[4])
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    glBindTexture(GL_TEXTURE_2D, sky_texture)
    glBegin(GL_QUADS)
    for vertex in scene_vertices["sky"]:
        glTexCoord2f(vertex[3], vertex[4])
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()

    glDisable(GL_TEXTURE_2D)
    glEnable(GL_DEPTH_TEST)

def draw_lake():
    glMatrixMode(GL_MODELVIEW)
    glColor3f(0, 0.3333, 1)
    glBegin(GL_QUADS)
    glVertex3f(.5, -2, -2)
    glVertex3f(2, -2, -2)
    glVertex3f(2, -2, 2)
    glVertex3f(.5, -2, 2)
    glEnd()
    glColor3f(1, 1, 1)

def draw_road1():
    glMatrixMode(GL_MODELVIEW)
    glColor3f(0.162, 0.168, 0.18)
    glBegin(GL_QUADS)
    glVertex3f(-0.55, -2, -2)
    glVertex3f(-0.55, -2, 2)
    glVertex3f(-0.85, -2, 2)
    glVertex3f(-0.85, -2, -2)
    glEnd()
    glColor3f(1, 1, 1)

def draw_road2():
    glMatrixMode(GL_MODELVIEW)
    glColor3f(0.162, 0.168, 0.18)
    glBegin(GL_QUADS)
    glVertex3f(0.5, -2, 0.15)
    glVertex3f(0.5, -2, -0.15)
    glVertex3f(-2, -2, -0.15)
    glVertex3f(-2, -2, 0.15)
    glEnd()
    glColor3f(1, 1, 1)
    
def draw_sphere(x, y, z, radius):
    glPushMatrix()
    glTranslatef(x, y, z)
    quad = gluNewQuadric()
    gluSphere(quad, radius, 16, 16)
    glPopMatrix()
    
    
def draw_bush():
    glPushMatrix()
    glColor3f(0.05, 0.4, 0.05)
    draw_sphere(0, -1.8, 0, 0.25)
    draw_sphere(-2, -1.8, 0, 0.25)
    glPopMatrix()
    glColor3f(1.0, 1.0, 1.0)


    

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.OPENGL | pygame.DOUBLEBUF)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    sky_texture = load_texture("Textures/clouds.jpg")
    walls_texture = load_texture("Textures/snowymountains.jpg")
    grass_texture = load_texture("Textures/grasstexture.jpg")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5,0,0)
                    if event.key == pygame.K_UP:
                        glTranslatef(0,1,0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0,-1,0)
                    if event.key == pygame.K_a:
                        glRotatef(5, 0, 1, 0)
                    if event.key == pygame.K_d:
                        glRotatef(5, 0, -1, 0)
                    if event.key == pygame.K_w:
                        glRotatef(5, 1, 0, 0)
                    if event.key == pygame.K_s:
                        glRotatef(5, -1, 0, 0)
                    if event.key == pygame.K_q:
                        glRotatef(5, 0, 0, 1)
                    if event.key == pygame.K_e:
                        glRotatef(5, 0, 0, -1)
                    if event.key == pygame.K_t:
                        open_trunk = not open_trunk
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_scene(walls_texture, grass_texture, sky_texture)
        draw_lake()
        draw_road1()
        draw_road2()
        #draw_bush()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()