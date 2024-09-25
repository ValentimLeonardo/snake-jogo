# configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo da cobrinha")
largura, altura = 800, 500
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores (RGB)
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

#paramentro da cobrinha
tamanho_quadrado = 12
velocidade_jogo = 15

def gerar_comida():
    comida_x = round(random.randrange(0,(largura - tamanho_quadrado)) / 12.0) * 12.0
    comida_y = round(random.randrange(0,(altura - tamanho_quadrado)) / 12.0) * 12.0


    return comida_x, comida_y
def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def rodar_jogo():
    fim_de_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_de_jogo:

        tela.fill(preta)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True

        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        pygame.display.update()
        relogio.tick(velocidade_jogo)
#Criar um loop infinito

#desenhar os objetos de jogo na tela
# pontuação
# cobrinha
# comida

#criar lógica de finalizar o jogo
# o que acontece:
# cobra bateu na parede
# cobra bateu em si mesma

#pegar as interações com o usuario
#fecho a tela
#apertou as telas do teclado para mover a cobra

rodar_jogo()