import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from math import pi

def perlin(x, y, seed=0):
    np.random.seed(seed)
    n = x + y * 57
    n = (n < 13) ^ n
    return (1.0 - ((n * (n * n * 15731 + 789221) + 1376312589) & 0x7fffffff) / 1073741824.0)

def create_terrain(width, height, resolution, seed):
    terrain = []
    for y in range(height):
        row = []
        for x in range(width):
            noise = perlin(x / resolution, y / resolution, seed=seed)
            row.append(noise)
        terrain.append(row)
    return terrain

def draw_mountain(terrain):
    glColor3f(0.3, 0.9, 0.3)
    glBegin(GL_TRIANGLES)
    for y in range(len(terrain) - 1):
        for x in range(len(terrain[0]) - 1):
            glVertex3f(x, y, terrain[y][x])
            glVertex3f(x + 1, y, terrain[y][x + 1])
            glVertex3f(x, y + 1, terrain[y + 1][x])
            
            glVertex3f(x + 1, y, terrain[y][x + 1])
            glVertex3f(x + 1, y + 1, terrain[y + 1][x + 1])
            glVertex3f(x, y + 1, terrain[y + 1][x + 1])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    terrain = create_terrain(width, height, resolution, seed)
    glTranslatef(-len(terrain[0]) / 2, -len(terrain) / 2, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glRotatef(1, 1, 1, 1)

        draw_mountain(terrain)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    width = 50
    height = 50
    resolution = 10
    seed = 0

    main()
