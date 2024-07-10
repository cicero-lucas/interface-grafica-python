import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Função para criar uma montanha mais alta e realista
def create_mountain(x_offset):
    num_segments = 100
    num_layers = 50
    mountain_vertices = []
    for layer in range(num_layers):
        layer_vertices = []
        for segment in range(num_segments):
            x = (segment / num_segments - 0.5) * 50 + x_offset
            y = (layer / num_layers) * 15  # Ajuste da altura da montanha
            z = (segment / num_segments - 0.5) * 50
            y += 5 * (1 - (abs(segment - num_segments / 2) / (num_segments / 2)))  # Adicionar detalhes à montanha
            layer_vertices.append((x, y, z))
        mountain_vertices.append(layer_vertices)
    return mountain_vertices


def draw_mountain(mountain_vertices, modo):
    glEnable(GL_MAP2_VERTEX_3)
    quant = len(mountain_vertices[0])
    if modo == 1:
        glColor3fv((0.5, 0.25, 0.1))  # Cor marrom
        for w in range(len(mountain_vertices) - 1):
            glBegin(GL_QUAD_STRIP)
            for t in range(len(mountain_vertices[w])):
                glVertex3fv(mountain_vertices[w][t])
                glVertex3fv(mountain_vertices[w + 1][t])
            glEnd()
    else:
        glColor3fv((1, 1, 2))  # Cor branca
        for w in range(len(mountain_vertices)):
            glBegin(GL_LINE_STRIP)
            for t in range(len(mountain_vertices[w])):
                glVertex3fv(mountain_vertices[w][t])
            glEnd()
            glBegin(GL_LINE_STRIP)
            for t in range(len(mountain_vertices[w])):
                glVertex3fv(mountain_vertices[t][w])
            glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 200)  # Aumentar a profundidade de visualização

    glTranslatef(0.0, -10.0, -100)  # Ajuste de posição inicial

    mountain = create_mountain(0)

    modo = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    glRotate(11, 0, 1, 0)
                else:
                    modo = 2 if modo == 1 else 1
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_mountain(mountain, modo)
        pygame.display.flip()
        pygame.time.wait(100)

main()
