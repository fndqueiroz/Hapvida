import pygame
import random

pygame.init()

# Configurações
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🐍 Cobrinha")

relogio = pygame.time.Clock()

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)

# Cobrinha
tamanho = 10
x = largura // 2
y = altura // 2
vel_x = 0
vel_y = 0

corpo = []
comprimento = 1

# Comida
comida_x = random.randrange(0, largura, tamanho)
comida_y = random.randrange(0, altura, tamanho)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                vel_x = -tamanho
                vel_y = 0
            elif evento.key == pygame.K_RIGHT:
                vel_x = tamanho
                vel_y = 0
            elif evento.key == pygame.K_UP:
                vel_y = -tamanho
                vel_x = 0
            elif evento.key == pygame.K_DOWN:
                vel_y = tamanho
                vel_x = 0

    x += vel_x
    y += vel_y

    # Colisão com parede
    if x < 0 or x >= largura or y < 0 or y >= altura:
        rodando = False

    tela.fill(preto)

    # Desenha comida
    pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho, tamanho])

    # Corpo da cobrinha
    cabeca = [x, y]
    corpo.append(cabeca)

    if len(corpo) > comprimento:
        del corpo[0]

    # Colisão com o próprio corpo
    for parte in corpo[:-1]:
        if parte == cabeca:
            rodando = False

    for parte in corpo:
        pygame.draw.rect(tela, verde, [parte[0], parte[1], tamanho, tamanho])

    # Comer comida
    if x == comida_x and y == comida_y:
        comida_x = random.randrange(0, largura, tamanho)
        comida_y = random.randrange(0, altura, tamanho)
        comprimento += 1

    pygame.display.update()
    relogio.tick(10)

pygame.quit()
