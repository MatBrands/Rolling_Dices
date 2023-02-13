from OpenGL.GLUT import *
from sys import argv, path
path.insert(1, '../')

from index.Rolling import *

if __name__ == '__main__':
    glutInit(argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(-200, -200)
    windows = glutCreateWindow("Rolling Dices")
    rolling = Rolling(windows)
    glutDisplayFunc(rolling.show_screen)
    glutIdleFunc(rolling.show_screen)
    glutMainLoop()