import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

scale = 2.0 

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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_scene(walls_texture, grass_texture, sky_texture)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()