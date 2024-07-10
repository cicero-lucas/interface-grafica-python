
#teste
import pygame
import sys
import math

pygame.init()

# Configurando a tela
tela_width, tela_height = 800, 800
tela = pygame.display.set_mode((tela_width, tela_height))
pygame.display.set_caption("Cadeia de Montanhas atividade develop")

# Cor das montanhas (amarelo)
montanhaCor = (255, 255, 0)

montanhaPontos = []
for x in range(tela_width):
    y = int(300 + 100 * math.sin((x - tela_width / 2) * math.pi / 200))
    montanhaPontos.append((x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Desenhando montanhas
    pygame.draw.polygon(tela, montanhaCor, montanhaPontos)
    pygame.display.flip()
