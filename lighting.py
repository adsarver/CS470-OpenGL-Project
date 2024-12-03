from OpenGL.GL import *

def setup_street_lamp_light():
    glEnable(GL_LIGHT1)
    glPushMatrix()
    glLoadIdentity()  # Reset transformations
    light_position = [0.0, 3.0, 0.0, 1.0]  # Position at the lamp head
    light_diffuse = [0.8, 0.8, 0.6, 1.0]  #  diffuse light
    light_ambient = [0.1, 0.1, 0.05, 1.0]  #  ambient light
    light_specular = [0.6, 0.6, 0.5, 1.0]  #specular light

    glLightfv(GL_LIGHT1, GL_POSITION, light_position)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular)
    glPopMatrix()

def setup_stoplight_light():
    glEnable(GL_LIGHT2)
    glPushMatrix()
    glLoadIdentity()
    light_position = [0.0, 2.5, 0.3, 1.0]
    light_diffuse = [0.8, 0.0, 0.0, 1.0]
    light_ambient = [0.05, 0.0, 0.0, 1.0]
    light_specular = [0.7, 0.0, 0.0, 1.0]

    glLightfv(GL_LIGHT2, GL_POSITION, light_position)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light_specular)
    glPopMatrix()

def setup_scene_lighting(is_daytime):
    glEnable(GL_LIGHTING)

    # Global ambient lighting
    global_ambient = [0.8, 0.8, 0.8, 1.0] if is_daytime else [0.2, 0.2, 0.4, 1.0]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)

    # Light 0 for main lighting
    glEnable(GL_LIGHT0)
    light_position = [10, 10, 10, 1]
    light_diffuse = [1.0, 1.0, 1.0, 1.0] if is_daytime else [0.4, 0.4, 0.5, 1.0]
    light_ambient = [0.2, 0.2, 0.2, 1.0] if is_daytime else [0.1, 0.1, 0.2, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)