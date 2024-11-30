from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Initial camera parameters
camera_pos = np.array([0.0, 2.0, 10.0])  # Start slightly above street level
camera_target = np.array([0.0, 1.0, 0.0])  # Look at the center of the scene
camera_up = np.array([0.0, 1.0, 0.0])  # "Up" direction

# Camera movement speed
movement_speed = 0.5
rotation_speed = 2.0
rise_speed = 0.5


def apply_camera():
    """Apply the camera view using gluLookAt."""
    gluLookAt(
        *camera_pos,  # Camera position
        *camera_target,  # Where the camera is looking
        *camera_up  # Up vector
    )


def set_initial_position(view="street"):
    """
    Set the initial camera position.

    Parameters:
        view (str): The desired initial view. Options: "street" or "aerial".
    """
    global camera_pos, camera_target
    if view == "street":
        camera_pos[:] = [0.0, 2.0, 10.0]  # Slightly above street level
        camera_target[:] = [0.0, 1.0, 0.0]  # Looking down the street
    elif view == "aerial":
        camera_pos[:] = [5.0, 10.0, 10.0]  # Aerial position
        camera_target[:] = [0.0, 0.0, 0.0]  # Looking at the center of the scene


def move_forward():
    """Move the camera forward."""
    direction = camera_target - camera_pos
    direction = direction / np.linalg.norm(direction)  # Normalize direction vector
    camera_pos[:] += direction * movement_speed
    camera_target[:] += direction * movement_speed


def move_backward():
    """Move the camera backward."""
    direction = camera_target - camera_pos
    direction = direction / np.linalg.norm(direction)
    camera_pos[:] -= direction * movement_speed
    camera_target[:] -= direction * movement_speed


def pan_left():
    """Pan the camera to the left."""
    right_vector = np.cross(camera_target - camera_pos, camera_up)
    right_vector = right_vector / np.linalg.norm(right_vector)  # Normalize right vector
    camera_pos[:] -= right_vector * movement_speed
    camera_target[:] -= right_vector * movement_speed


def pan_right():
    """Pan the camera to the right."""
    right_vector = np.cross(camera_target - camera_pos, camera_up)
    right_vector = right_vector / np.linalg.norm(right_vector)
    camera_pos[:] += right_vector * movement_speed
    camera_target[:] += right_vector * movement_speed


def rise_up():
    """Move the camera upward."""
    camera_pos[1] += rise_speed
    camera_target[1] += rise_speed


def descend():
    """Move the camera downward."""
    camera_pos[1] -= rise_speed
    camera_target[1] -= rise_speed


def rotate_left():
    """Rotate the camera left around the target."""
    angle = np.radians(rotation_speed)
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    direction = camera_pos - camera_target
    camera_pos[:] = np.dot(rotation_matrix, direction) + camera_target


def rotate_right():
    """Rotate the camera right around the target."""
    angle = -np.radians(rotation_speed)
    rotation_matrix = np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])
    direction = camera_pos - camera_target
    camera_pos[:] = np.dot(rotation_matrix, direction) + camera_target


def set_perspective(fov=60, aspect_ratio=16 / 9, near=0.1, far=100.0):
    """Set the perspective projection."""
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, aspect_ratio, near, far)
    glMatrixMode(GL_MODELVIEW)
