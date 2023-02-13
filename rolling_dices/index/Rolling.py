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

    globalAmb = np.array([0.1, 0.1, 0.1, 1])
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

def random_bool():
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
    
    def key_control(self, key: str, x, y) -> None:
        if key == b' ':
            self.axis = np.array([0, 0, -3.0])
            self.roll_dice = True
        elif key == b'\x03':
            glutDestroyWindow(self.window)
            
    def show_screen(self) -> None:
        glColor3f(1.0, 1.0, 1.0)
        self.clear_and_draw()

        if self.roll_dice:
            rot_x, rot_y = random_bool(), random_bool()

            while (self.axis[2] != (MAX_DEPTH + MIN_DEPTH)/2):
                self.axis[2] -= 0.25
                self.clear_and_draw()

            for i in range(2):
                if not i: a = 0; b = 150; c = 1
                else: a = 150; b = 0; c = -1
                    
                for j in range(a, b, c):
                    self.speed = j
                    
                    if self.axis[0] > MAX_EXTREMITY or self.axis[0] < MIN_EXTREMITY or self.axis[1] > MAX_EXTREMITY or self.axis[1] < MIN_EXTREMITY:
                        glColor3f(random.random(), random.random(), random.random())
                    
                    if self.axis[0] > MAX_EXTREMITY: rot_x, rot_y = False, random_bool()
                    elif self.axis[0] < MIN_EXTREMITY: rot_x, rot_y = True, random_bool()
                    
                    if self.axis[1] > MAX_EXTREMITY: rot_x, rot_y = random_bool(), False
                    elif self.axis[1] < MIN_EXTREMITY: rot_x, rot_y = random_bool(), True
                    
                    if rot_x: self.axis[0] += np.round(random.uniform(.0, .4), 2)
                    else: self.axis[0] -= np.round(random.uniform(.0, .4), 2)
                    
                    if rot_y: self.axis[1] += np.round(random.uniform(.0, .4), 2)
                    else: self.axis[1] -= np.round(random.uniform(.0, .4), 2)
                    
                    self.clear_and_draw()
                
            while (self.axis[0] != 0 or self.axis[1] != 0):
                self.axis = np.round(self.axis, 1)
                if (self.axis[0] < 0): self.axis[0] += 0.1
                elif(self.axis[0] > 0): self.axis[0] -= 0.1
                
                if (self.axis[1] < 0): self.axis[1] += 0.1
                elif(self.axis[1] > 0): self.axis[1] -= 0.1
                self.clear_and_draw()

            while self.axis[2] != -3:
                if self.axis[2] < -3: self.axis[2] += 0.25
                
                self.clear_and_draw()
                
            glColor3f(1.0, 1.0, 1.0)
            self.roll_dice = False
            self.finish = True
            self.fix_angle()
            
    def roll_the_dice(self) -> None:
        if self.roll_dice:
            if not self.finish:
                if self.speed < 250:
                    self.angle = np.array([
                        self.angle[0] + random.randint(1, self.speed+10),
                        self.angle[1] + random.randint(1, self.speed+10),
                        self.angle[2] + random.randint(1, self.speed+10)
                        ]
                    )
                else:
                    self.angle = np.array([
                        self.angle[0] + random.randint(1, 500-self.speed+10),
                        self.angle[1] + random.randint(1, 500-self.speed+10),
                        self.angle[2] + random.randint(1, 500-self.speed+10)
                        ]
                    )

    def fix_angle(self) -> None:
        self.angle = np.array([self.angle[0]%360, self.angle[1]%360, self.angle[2]%360])
        fixing_angle = np.zeros(3)
        while (self.finish):
            for i in range (0, 3):
                for j in range (0, 450, 90):
                    temp = self.angle[i] - j, j - self.angle[i]
                    if ((-45 <= temp[0] <= 45) or (-45 <= temp[1] <= 45)): fixing_angle[i] = j
            self.angle = fixing_angle
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