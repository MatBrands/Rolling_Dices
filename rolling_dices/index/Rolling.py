import numpy as np
from numpy import random
from index.Dice import *
from OpenGL.GLU import gluPerspective
from OpenGL.GLUT import glutKeyboardFunc, glutSwapBuffers

EXTREMIDADE_MIN = -10
EXTREMIDADE_MAX = 10
PROFUNDIDADE_MIN = -12
PROFUNDIDADE_MAX = -20

def iluminacao():
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

def rotacao():
    if (random.randint(0, 2) == 0):
        return True
    else:
        return False

class Rolling:
    def __init__(self) -> None:
        self.iterate()
        self.jogar_dado = False
        self.angulo = np.array([0, 0, 0])
        self.visualizar_resultado = False
        self.axis = np.array([0, 0, -3])
        self.velocidade = 0
    
    def iterate(self) -> None:
        glDepthFunc(GL_LESS)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(90, 1, 0.1, 100)
        self.dice = Dice()
        iluminacao()
        glutKeyboardFunc(self.key_control)
    
    def key_control(self, key, _, __) -> None:
        if key == b" ":
            self.axis = [0, 0, -3.0]
            self.jogar_dado = True
            
    def showScreen(self) -> None:
        glColor3f(1.0, 1.0, 1.0)
        self.limpa_desenha()

        if self.jogar_dado:
            rot_x = rotacao()
            rot_y = rotacao()
            rot_z = rotacao()

            while (self.axis[2] != (PROFUNDIDADE_MAX + PROFUNDIDADE_MIN)/2):
                self.axis[2] -= 0.25
                self.limpa_desenha()

            for i in range (0, 500):
                self.velocidade = i
                if self.axis[0] > EXTREMIDADE_MAX:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_x = False
                    rot_y = rotacao()
                    rot_z = rotacao()
                elif self.axis[0] < EXTREMIDADE_MIN:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_x = True
                    rot_y = rotacao()
                    rot_z = rotacao()
                if self.axis[1] > EXTREMIDADE_MAX:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_y = False
                    rot_x = rotacao()
                    rot_z = rotacao()
                elif self.axis[1] < EXTREMIDADE_MIN:
                    glColor3f(random.random(), random.random(), random.random())
                    rot_y = True
                    rot_x = rotacao()
                    rot_z = rotacao()
                if self.axis[2] > PROFUNDIDADE_MIN:
                    rot_z = False
                    rot_x = rotacao()
                    rot_y = rotacao()
                elif self.axis[2] < PROFUNDIDADE_MAX:
                    rot_z = True
                    rot_x = rotacao()
                    rot_y = rotacao()

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
                self.limpa_desenha()

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

                self.limpa_desenha()

            while self.axis[2] != -3:
                if self.axis[2] < -3:
                    self.axis[2] += 0.25
                self.limpa_desenha()
            glColor3f(1.0, 1.0, 1.0)
            self.jogar_dado = False
            self.visualizar_resultado = True
            self.ajeitaAngulo()
            
    def girarDado(self):
        if self.jogar_dado:
            if (self.visualizar_resultado == False):
                if self.velocidade < 250:
                    self.angulo[0] += random.randint(1, self.velocidade+10)
                    self.angulo[1] += random.randint(1, self.velocidade+10)
                    self.angulo[2] += random.randint(1, self.velocidade+10)
                else:
                    self.angulo[0] += random.randint(1, 500-self.velocidade+10)
                    self.angulo[1] += random.randint(1, 500-self.velocidade+10)
                    self.angulo[2] += random.randint(1, 500-self.velocidade+10)

    def ajeitaAngulo(self):
        self.angulo = np.array([self.angulo[0]%360, self.angulo[1]%360, self.angulo[2]%360])
        aux = np.zeros(3)
        while (self.visualizar_resultado):
            for i in range (0, 3):
                for j in range (0, 450, 90):
                    temp = self.angulo[i] - j
                    temp_2 = j - self.angulo[i]
                    if ((temp <= 45 and temp >= 0) or (temp_2 >= -45 and temp_2 <= 0) or (temp_2 <= 45 and temp_2 >= 0) or (temp >= -45 and temp <= 0)):
                        aux[i] = j
            self.angulo = aux
            self.visualizar_resultado = False
        self.axis[0] = 0.0
        self.limpa_desenha()

    def limpa_desenha(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(self.axis[0], self.axis[1], self.axis[2])

        glRotatef(self.angulo[0], 1.0, 0.0, 0.0)
        glRotatef(self.angulo[1], 0.0, 1.0, 0.0)
        glRotatef(self.angulo[2], 0.0, 0.0, 1.0)
        self.dice.print_cube()
        self.girarDado()
        glutSwapBuffers()