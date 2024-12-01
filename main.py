import camera, landscape, lighting, structures
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import camera
import landscape
import lighting
import structures
import characters

# Global Variables
window_width = 800
window_height = 600
daytime = True  # Day/Night toggle

def init():
    glEnable(GL_DEPTH_TEST)
    camera.set_initial_position(view="street")  # Set the initial view to "street"
    camera.set_perspective(fov=60, aspect_ratio=800 / 600)  # Set perspective
    glEnable(GL_LIGHTING)
    lighting.setup_lighting(daytime)
    glClearColor(0.5, 0.7, 1.0, 1.0)  # Light blue for the sky

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    camera.apply_camera()
    landscape.draw_landscape()
    structures.draw_structures()
    characters.draw_characters()

    glutSwapBuffers()

def toggle_day_night():
    global daytime
    daytime = not daytime
    lighting.setup_lighting(daytime)

def keyboard(key, x, y):
    def keyboard(key, x, y):
        if key == b'n':  # Toggle Day/Night
            toggle_day_night()
        elif key == b'w':  # Move forward
            camera.move_forward()
        elif key == b's':  # Move backward
            camera.move_backward()
        elif key == b'a':  # Pan left
            camera.pan_left()
        elif key == b'd':  # Pan right
            camera.pan_right()
        elif key == b'r':  # Rise up
            camera.rise_up()
        elif key == b'f':  # Descend
            camera.descend()
        elif key == b'q':  # Rotate left
            camera.rotate_left()
        elif key == b'e':  # Rotate right
            camera.rotate_right()
        glutPostRedisplay()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width/height, 1, 1000)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow("Interactive Scene")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()

