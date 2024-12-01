import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import pywavefront


person_scene = pywavefront.Wavefront('PyWaveObjs\\person.obj', collect_faces=True)

person_scene_box = (person_scene.vertices[0], person_scene.vertices[0])
for vertex in person_scene.vertices:
    min_v = [min(person_scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(person_scene_box[1][i], vertex[i]) for i in range(3)]
    person_scene_box = (min_v, max_v)

scene_size     = [person_scene_box[1][i]-person_scene_box[0][i] for i in range(3)]
max_scene_size = max(scene_size)
scaled_size    = 5
scene_scale    = [scaled_size/max_scene_size for i in range(3)]
scene_trans    = [-(person_scene_box[1][i]+person_scene_box[0][i])/2 for i in range(3)]

def Person():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glColor3f(1.000, 0.627, 0.478)
    for mesh in person_scene.mesh_list:
        glBegin(GL_QUADS)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*person_scene.vertices[vertex_i])
        glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()

arm_scene = pywavefront.Wavefront('PyWaveObjs\\PersonArm.obj', collect_faces=True)

arm_scene_box = (arm_scene.vertices[0], arm_scene.vertices[0])
for vertex in arm_scene.vertices:
    min_v = [min(arm_scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(arm_scene_box[1][i], vertex[i]) for i in range(3)]
    arm_scene_box = (min_v, max_v)


def arm():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glColor3f(1.000, 0.627, 0.478)
    for mesh in arm_scene.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*arm_scene.vertices[vertex_i])
        glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()

cat_scene = pywavefront.Wavefront('PyWaveObjs\\Cat.obj', collect_faces=True)

cat_scene_box = (cat_scene.vertices[0], cat_scene.vertices[0])
for vertex in cat_scene.vertices:
    min_v = [min(cat_scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(cat_scene_box[1][i], vertex[i]) for i in range(3)]
    cat_scene_box = (min_v, max_v)


def cat():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    glTranslatef(-1, 0, 2.5)
    glRotatef(1, 0, 1, 0)
    for mesh in cat_scene.mesh_list:
        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*cat_scene.vertices[vertex_i])
        glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()

Car_scene = pywavefront.Wavefront('PyWaveObjs\\Car.obj', collect_faces=True)

Car_scene_box = (Car_scene.vertices[0], Car_scene.vertices[0])
for vertex in Car_scene.vertices:
    min_v = [min(Car_scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(Car_scene_box[1][i], vertex[i]) for i in range(3)]
    Car_scene_box = (min_v, max_v)


def Car():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    for mesh in Car_scene.mesh_list:
        glBegin(GL_LINES)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*Car_scene.vertices[vertex_i])
        glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()

Trunk_scene = pywavefront.Wavefront('PyWaveObjs\\Trunk.obj', collect_faces=True)

Trunk_scene_box = (Trunk_scene.vertices[0], Trunk_scene.vertices[0])
for vertex in Trunk_scene.vertices:
    min_v = [min(Trunk_scene_box[0][i], vertex[i]) for i in range(3)]
    max_v = [max(Trunk_scene_box[1][i], vertex[i]) for i in range(3)]
    Trunk_scene_box = (min_v, max_v)


def Trunk():
    glPushMatrix()
    glScalef(*scene_scale)
    glTranslatef(*scene_trans)
    for mesh in Trunk_scene.mesh_list:
        glBegin(GL_QUADS)
        for face in mesh.faces:
            for vertex_i in face:
                glVertex3f(*Trunk_scene.vertices[vertex_i])
        glEnd()
    glColor3f(1, 1, 1)
    glPopMatrix()

def main():
        pygame.init()
        display = (1080, 720)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -10)

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
                    if event.key == pygame.K_a:
                        glTranslatef(0.5, 0, 0)
                        glPushMatrix()
                        Person()
                        glTranslatef(0.5, 0 , 0)

                        glPopMatrix()
                    if event.key == pygame.K_d:
                        glRotatef(5, -1, 0, 0)
                    if event.key == pygame.K_w:
                        glRotatef(45, 0, 1, 0)
                    if event.key == pygame.K_s:
                        glRotatef(45, 0, -1, 0)
                    if event.key == pygame.K_q:
                        glRotatef(5, 0, 0, 1)
                    if event.key == pygame.K_e:
                        glRotatef(5, 0, 0, -1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

            Person()
            arm()
            cat()
            Car()
            Trunk()
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

            pygame.display.flip()
            pygame.time.wait(10)

main()