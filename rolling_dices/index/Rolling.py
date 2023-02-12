import numpy as np
from numpy import random
from index.Dice import *
from OpenGL.GLU import gluPerspective
from OpenGL.GLUT import glutKeyboardFunc, glutSwapBuffers, glutDestroyWindow

MIN_EXTREMITY = -10
MAX_EXTREMITY = 10
MIN_DEPTH = -12
MAX_DEPTH = -20

def ilumination():
    glClearColor(0, 0, 0, 1)

    glEnable(GL_DEPTH_TEST)

    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_CULL_FACE)
    glCullFace(GL_BACK)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
    
    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_TRUE)

    globalAmb = [0.1, 0.1, 0.1, 1]
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, globalAmb)
    
    light = np.array(
        [
            [0.1, 0.1, 0.1, 1], #Ambient
            [0.8, 0.8, 0.8, 1], #Diffuse
            [1.0,  1.0,  1.0, 1], #Specular
            [0, 0, 3, 1] # Position
        ]
    )

    glLightfv(GL_LIGHT0, GL_AMBIENT, light[0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light[1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, light[2])
    glLightfv(GL_LIGHT0, GL_POSITION, light[3])

def rotation():
    if (random.randint(0, 2) == 0):
        return True
    else:
        return False

class Rolling:
    def __init__(self, window) -> None:
        self.config()
        self.window = window
        self.roll_dice = False
        self.angle = np.array([0, 0, 0])
        self.finish = False
        self.axis = np.array([0, 0, -3])
        self.speed = 0
    
    def config(self) -> None:
        glDepthFunc(GL_LESS)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(90, 1, 0.1, 100)
        self.dice = Dice()
        ilumination()
        glutKeyboardFunc(self.key_control)
    
    def key_control(self, key, x, y) -> None:
        if key == b' ':
            self.axis = [0, 0, -3.0]
            self.roll_dice = True
        elif key == b'\x03':
            glutDestroyWindow(self.window)
            
    def showScreen(self) -> None:
        glColor3f(1.0, 1.0, 1.0)
        self.clear_and_draw()

        if self.roll_dice:
            rot_x = rotation()
            rot_y = rotation()
            rot_z = rotation()

            while (self.axis[2] != (MAX_DEPTH + MIN_DEPTH)/2):
                self.axis[2] -= 0.25
                self.clear_and_draw()

            for i in range (0, 500):
                self.speed = i
                if self.axis[0] > MAX_EXTREMITY:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_x = False
                    rot_y = rotation()
                    rot_z = rotation()
                elif self.axis[0] < MIN_EXTREMITY:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_x = True
                    rot_y = rotation()
                    rot_z = rotation()
                if self.axis[1] > MAX_EXTREMITY:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_y = False
                    rot_x = rotation()
                    rot_z = rotation()
                elif self.axis[1] < MIN_EXTREMITY:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_y = True
                    rot_x = rotation()
                    rot_z = rotation()
                if self.axis[2] > MIN_DEPTH:
                    rot_z = False
                    rot_x = rotation()
                    rot_y = rotation()
                elif self.axis[2] < MAX_DEPTH:
                    rot_z = True
                    rot_x = rotation()
                    rot_y = rotation()

                if rot_x:
                    self.axis[0] += 0.25
                else:
                    self.axis[0] -= 0.25
                if rot_y:
                    self.axis[1] += 0.25
                else:
                    self.axis[1] -= 0.25
                if rot_z:
                    self.axis[2] += 0.25
                else:
                    self.axis[2] -= 0.25
                self.clear_and_draw()

            while (self.axis[0] != 0 or self.axis[1] != 0):
                if (self.axis[0] < 0):
                    self.axis[0] += 0.25
                elif(self.axis[0] > 0):
                    self.axis[0] -= 0.25
                if (self.axis[1] < 0):
                    self.axis[1] += 0.25
                elif(self.axis[1] > 0):
                    self.axis[1] -= 0.25
                if (self.axis[2] < -3):
                    self.axis[2] += 0.25

                self.clear_and_draw()

            while self.axis[2] != -3:
                if self.axis[2] < -3:
                    self.axis[2] += 0.25
                self.clear_and_draw()
            glColor3f(1.0, 1.0, 1.0)
            self.roll_dice = False
            self.finish = True
            self.fix_angle()
            
    def roll_the_dice(self) -> None:
        if self.roll_dice:
            if (self.finish == False):
                if self.speed < 250:
                    self.angle[0] += random.randint(1, self.speed+10)
                    self.angle[1] += random.randint(1, self.speed+10)
                    self.angle[2] += random.randint(1, self.speed+10)
                else:
                    self.angle[0] += random.randint(1, 500-self.speed+10)
                    self.angle[1] += random.randint(1, 500-self.speed+10)
                    self.angle[2] += random.randint(1, 500-self.speed+10)

    def fix_angle(self) -> None:
        self.angle = np.array([self.angle[0]%360, self.angle[1]%360, self.angle[2]%360])
        aux = np.zeros(3)
        while (self.finish):
            for i in range (0, 3):
                for j in range (0, 450, 90):
                    temp = self.angle[i] - j
                    temp_2 = j - self.angle[i]
                    if ((temp <= 45 and temp >= 0) or (temp_2 >= -45 and temp_2 <= 0) or (temp_2 <= 45 and temp_2 >= 0) or (temp >= -45 and temp <= 0)):
                        aux[i] = j
            self.angle = aux
            self.finish = False
        self.axis[0] = 0.0
        self.clear_and_draw()

    def clear_and_draw(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(self.axis[0], self.axis[1], self.axis[2])

        glRotatef(self.angle[0], 1.0, 0.0, 0.0)
        glRotatef(self.angle[1], 0.0, 1.0, 0.0)
        glRotatef(self.angle[2], 0.0, 0.0, 1.0)
        self.dice.print_cube()
        self.roll_the_dice()
        glutSwapBuffers()