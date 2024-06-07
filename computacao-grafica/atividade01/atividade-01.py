import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def construir_casa(x, y, z, width, height, depth, size):
    try:
        glBegin(GL_QUADS)

        #frente da casa 
        glColor3f(0.5, 0.5, 0.5) 
        glVertex3f(x, y, z)
        glVertex3f(x + width*size, y, z)
        glVertex3f(x + width*size, y + height*size, z)
        glVertex3f(x, y + height*size, z)

        # Fundo da casa
        glColor3f(0.5, 0.5, 0.5) 
        glVertex3f(x, y, z + depth*size)
        glVertex3f(x + width*size, y, z + depth*size)
        glVertex3f(x + width*size, y + height*size, z + depth*size)
        glVertex3f(x, y + height*size, z + depth*size)
        
        # lateral esquedar
        glColor3f(0.5, 0.5, 0.5)  
        glVertex3f(x, y, z)
        glVertex3f(x, y, z + depth*size)
        glVertex3f(x, y + height*size, z + depth*size)
        glVertex3f(x, y + height*size, z)
        
        # latera direita
        glColor3f(0.5, 0.5, 0.5)  
        glVertex3f(x + width*size, y, z)
        glVertex3f(x + width*size, y, z + depth*size)
        glVertex3f(x + width*size, y + height*size, z + depth*size)
        glVertex3f(x + width*size, y + height*size, z)
        
        # telhado triangular 
        glColor3f(0.1, 0.1, 0.3) 
        glVertex3f(x - 0.2*size, y + height*size, z)
        glVertex3f(x + width*size + 0.4*size, y + height*size, z)
        glVertex3f(x + width*size / 2, y + height*size * 1.6, z + depth*size / 2)
        glVertex3f(x - 0.2*size, y + height*size, z + depth*size)
        
        glColor3f(0.1, 0.1, 0.3)  
        glVertex3f(x - 0.2*size, y + height*size, z + depth*size)
        glVertex3f(x + width*size / 2, y + height*size * 1.6, z + depth*size / 2)
        glVertex3f(x + width*size + 0.2*size, y + height*size, z + depth*size)
        glVertex3f(x + width*size / 2, y + height*size * 1.6, z + depth*size / 2)

        glEnd()

        # Porta
        glColor3f(0.0, 0.0, 0.3)  
        glBegin(GL_QUADS)
        glVertex3f(x + width*size * 0.35, y, z)
        glVertex3f(x + width*size * 0.65, y, z)
        glVertex3f(x + width*size * 0.65, y + height*size * 0.5, z)
        glVertex3f(x + width*size * 0.35, y + height*size * 0.5, z)
        glEnd()

        # Janelas
        glColor3f(0.0, 0.0, 0.0) 
        glLineWidth(2.1)
        glBegin(GL_LINE_LOOP)
        glVertex3f(x + width*size * 0.1, y + height*size * 0.6, z)
        glVertex3f(x + width*size * 0.3, y + height*size * 0.6, z)
        glVertex3f(x + width*size * 0.3, y + height*size * 0.8, z)
        glVertex3f(x + width*size * 0.1, y + height*size * 0.8, z)
        glEnd()

        glColor3f(0.0, 0.0, 0.0) 
        glBegin(GL_LINE_LOOP)
        glVertex3f(x + width*size * 0.7, y + height*size * 0.6, z)
        glVertex3f(x + width*size * 0.9, y + height*size * 0.6, z)
        glVertex3f(x + width*size * 0.9, y + height*size * 0.8, z)
        glVertex3f(x + width*size * 0.7, y + height*size * 0.8, z)
        glEnd()

        glColor3f(0.3, 0.6, 0.8)  
        glBegin(GL_QUADS)
        glVertex3f(x + width*size * 0.1 + 0.01, y + height*size * 0.6 + 0.01, z)
        glVertex3f(x + width*size * 0.3 - 0.01, y + height*size * 0.6 + 0.01, z)
        glVertex3f(x + width*size * 0.3 - 0.01, y + height*size * 0.8 - 0.01, z)
        glVertex3f(x + width*size * 0.1 + 0.01, y + height*size * 0.8 - 0.01, z)
        glEnd()

        glBegin(GL_QUADS)
        glVertex3f(x + width*size * 0.7 + 0.01, y + height*size * 0.6 + 0.01, z)
        glVertex3f(x + width*size * 0.9 - 0.01, y + height*size * 0.6 + 0.01, z)
        glVertex3f(x + width*size * 0.9 - 0.01, y + height*size * 0.8 - 0.01, z)
        glVertex3f(x + width*size * 0.7 + 0.01, y + height*size * 0.8 - 0.01, z)
        glEnd()

    except:
        print('erro ao contruir a casa')

# Função principal que gera o grafico
def main():
    pygame.init()
    display = (1450, 750)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glTranslatef(0.0, 0.0, -10)
    
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        try:
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            #função construir casa
            construir_casa(-4, -1, 0, 2, 2, 1, 0.6) # Casa pequena
            construir_casa(-1, -1, 0, 2, 2, 1, 1.1)# Casa média
            construir_casa(2, -1, 0, 2, 2, 1, 1.6)# Casa média
            
            pygame.display.flip()
            pygame.time.wait(10)
        except:
            print("erro!")

if __name__ == "__main__":
    main()
