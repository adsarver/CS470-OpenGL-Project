import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import time

# Global camera parameters
camera_pos = np.array([0.0, 2.0, 10.0])  # Camera starting position
camera_front = np.array([0.0, 0.0, -1.0])  # Direction camera is facing
camera_up = np.array([0.0, 1.0, 0.0])  # Up vector to define the camera's orientation

# Movement parameters
movement_speed = 2.5  # Units per second
rotation_speed = 2.0  # Degrees per second
mouse_sensitivity = 0.1  # Sensitivity for mouse movement
last_frame_time = time.time()  # Track time for consistent movement speed

# Yaw and pitch for controlling the camera direction
yaw = -90.0  # Starting direction looking towards negative Z
pitch = 0.0  # No initial pitch rotation

def apply_camera():
    """
    Apply the camera view using gluLookAt based on current camera parameters.
    """
    camera_target = camera_pos + camera_front
    gluLookAt(
        *camera_pos,        # Camera position
        *camera_target,     # Camera target (where the camera is looking)
        *camera_up          # Up vector to define which direction is up
    )

def set_initial_position(view="street"):
    """
    Set the initial camera position.
    :param view: The desired initial view. Options: "street" or "aerial".
    """
    global camera_pos, camera_front, yaw, pitch
    if view == "street":
        camera_pos[:] = [0.0, 2.0, 10.0]  # Slightly above street level
        yaw = -90.0  # Facing down the street along negative Z
        pitch = 0.0
    elif view == "aerial":
        camera_pos[:] = [5.0, 10.0, 10.0]  # Elevated aerial position
        yaw = -135.0  # Facing towards the origin from above
        pitch = -30.0
    update_camera_vectors()

def move_camera(direction):
    """
    Move the camera in the specified direction.
    :param direction: A string indicating the movement direction ("forward", "backward", "left", "right", "up", "down").
    """
    global camera_pos
    current_time = time.time()
    delta_time = current_time - last_frame_time
    camera_speed = movement_speed * delta_time

    if direction == "forward":
        camera_pos += camera_front * camera_speed
    elif direction == "backward":
        camera_pos -= camera_front * camera_speed
    elif direction == "left":
        right_vector = np.cross(camera_front, camera_up)
        right_vector = right_vector / np.linalg.norm(right_vector)
        camera_pos -= right_vector * camera_speed
    elif direction == "right":
        right_vector = np.cross(camera_front, camera_up)
        right_vector = right_vector / np.linalg.norm(right_vector)
        camera_pos += right_vector * camera_speed
    elif direction == "up":
        camera_pos += camera_up * camera_speed
    elif direction == "down":
        camera_pos -= camera_up * camera_speed

    update_camera_vectors()

def update_camera_vectors():
    """
    Update the direction vectors based on the current yaw and pitch.
    """
    global camera_front
    front = np.array([
        np.cos(np.radians(yaw)) * np.cos(np.radians(pitch)),
        np.sin(np.radians(pitch)),
        np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
    ])
    camera_front = front / np.linalg.norm(front)

def rotate_camera(xoffset, yoffset):
    """
    Rotate the camera based on mouse movement.
    :param xoffset: Horizontal mouse movement.
    :param yoffset: Vertical mouse movement.
    """
    global yaw, pitch
    yaw += xoffset * mouse_sensitivity
    pitch += yoffset * mouse_sensitivity

    # Constrain pitch to prevent flipping
    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    update_camera_vectors()

def set_perspective(fov=60, aspect_ratio=16 / 9, near=0.1, far=100.0):
    """
    Set the perspective projection for the scene.
    :param fov: Field of view in degrees.
    :param aspect_ratio: Aspect ratio of the viewport.
    :param near: Near clipping plane.
    :param far: Far clipping plane.
    """
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(fov, aspect_ratio, near, far)
    glMatrixMode(GL_MODELVIEW)
