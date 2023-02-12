from OpenGL.GL import *
from PIL import Image

class Dice:
    def __init__(self) -> None:
        self.id_for_texture = self.set_texture()

    def load_image(self, filename):
        image = Image.open(filename)
        width, height, pbits = image.size[0], image.size[1], image.convert("RGBA").tobytes("raw", "RGBA")
        del image
        
        id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, id)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pbits)
        
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        
        return id

    def set_texture(self):
        glEnable(GL_TEXTURE_2D)
        return [self.load_image(f'./media/dice_{i}.png') for i in range (1, 7)]

    def print_cube(self):
        mat_specular = [1, 1, 1, 1]
        mat_amb = [0, 0, 0, 1]
        glMaterialfv(GL_FRONT, GL_AMBIENT, mat_amb)
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
        glMaterialf(GL_FRONT, GL_SHININESS, 128)

        #Frente
        glNormal3f(0, 0, 1)
        glBindTexture(GL_TEXTURE_2D, self.id_for_texture[0])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glEnd()

        #Costa
        glNormal3f(0, 0, -1)
        glBindTexture(GL_TEXTURE_2D, self.id_for_texture[1])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glEnd()

        #Cima
        glNormal3f(0, 1, 0)
        glBindTexture(GL_TEXTURE_2D, self.id_for_texture[2])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0,  1.0,  1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0,  1.0, -1.0)
        glEnd()

        #Baixo
        glNormal3f(0, -1, 0)
        glBindTexture(GL_TEXTURE_2D, self.id_for_texture[3])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0,  1.0)
        glEnd()

        #Direita
        glNormal3f(1, 0, 0)
        glBindTexture(GL_TEXTURE_2D, self.id_for_texture[4])
        glBegin(GL_QUADS)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0,  1.0, -1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, -1.0,  1.0)
        glEnd()

        #Esquerda
        glNormal3f(-1, 0, 0)
        glBindTexture(GL_TEXTURE_2D, self.id_for_texture[5])
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.0, -1.0,  1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.0,  1.0,  1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0,  1.0, -1.0)
        glEnd()