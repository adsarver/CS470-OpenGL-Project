from OpenGL.GL import *

def setup_street_lamp_light():
    glEnable(GL_LIGHT1)
    light_position = [0.0, 3.0, 0.0, 1.0]  # Position at the lamp head
    light_diffuse = [1.0, 1.0, 0.8, 1.0]  # Warm yellow light
    light_ambient = [0.2, 0.2, 0.1, 1.0]
    light_specular = [1.0, 1.0, 0.8, 1.0]

    glLightfv(GL_LIGHT1, GL_POSITION, light_position)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT1, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT1, GL_SPECULAR, light_specular)

def setup_stoplight_light():
    glEnable(GL_LIGHT2)
    light_position = [0.0, 2.5, 0.3, 1.0]  # Position at the red light
    light_diffuse = [1.0, 0.0, 0.0, 1.0]  # Bright red light for stoplight
    light_ambient = [0.1, 0.0, 0.0, 1.0]
    light_specular = [1.0, 0.0, 0.0, 1.0]

    glLightfv(GL_LIGHT2, GL_POSITION, light_position)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT2, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT2, GL_SPECULAR, light_specular)