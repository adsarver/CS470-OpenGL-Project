from OpenGL.GL import *
import time

from OpenGL.raw.GLUT import glutPostRedisplay

# Global variables for transitioning
current_light_intensity = 1.0  # 1.0 = full sunlight, 0.0 = no sunlight
transitioning_to_night = False

def setup_nighttime_lighting():
    glEnable(GL_LIGHTING)

    # Directional moonlight blue
    glEnable(GL_LIGHT1)
    moonlight_position = [1.0, 1.0, 0.5, 0.0]
    glLightfv(GL_LIGHT1, GL_POSITION, moonlight_position)
    moonlight_diffuse = [0.3, 0.3, 0.5, 1.0]
    glLightfv(GL_LIGHT1, GL_DIFFUSE, moonlight_diffuse)
    moonlight_ambient = [0.1, 0.1, 0.2, 1.0]
    glLightfv(GL_LIGHT1, GL_AMBIENT, moonlight_ambient)


def transition_to_night():
    global current_light_intensity, transitioning_to_night

    transitioning_to_night = True
    while current_light_intensity > 0.0:
        current_light_intensity -= 0.01
        update_lighting(current_light_intensity)
        time.sleep(0.05)  # Slow down the transition
        glutPostRedisplay()  # Update the scene
    transitioning_to_night = False

def update_lighting(intensity):

    # Adjust sunlight (GL_LIGHT0)
    sunlight_diffuse = [intensity, intensity * 0.9, intensity * 0.7, 1.0]
    glLightfv(GL_LIGHT0, GL_DIFFUSE, sunlight_diffuse)

    # Adjust ambient light to get darker
    ambient_light = [intensity * 0.3, intensity * 0.3, intensity * 0.3, 1.0]
    glLightfv(GL_LIGHT0, GL_AMBIENT, ambient_light)

    # Gradually increase moonlight (GL_LIGHT1)
    moonlight_intensity = 1.0 - intensity
    moonlight_diffuse = [moonlight_intensity * 0.3, moonlight_intensity * 0.3, moonlight_intensity * 0.5, 1.0]
    glLightfv(GL_LIGHT1, GL_DIFFUSE, moonlight_diffuse)