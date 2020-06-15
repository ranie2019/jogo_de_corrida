import pygame
from random import randint
pygame.init()

y = 500
x = 350
pos_x = 350

bran_y = randint(-1800, -100)
amar_y = randint(-1800, -100)
verm_y = randint(-1800, -100)
larj_y = randint(-1800, -100)

time = 0
tempo_segundos = 0

velocidade = 20
velocidade_outros = -10

fundo = pygame.image.load('rua.png')
carro = pygame.image.load('carro.png')
carro_branco = pygame.image.load('carro_branco.png')
carro_amarelo = pygame.image.load('carro_amarelo.png')
carro_laranja = pygame.image.load('carro_laranja.png')
carro_vermelho = pygame.image.load('carro_vermelho.png')

font = pygame.font.SysFont('ariel black', 50)
texto = font.render('Pontos ', True, (255, 255, 255))
pos_texto = texto.get_rect()
pos_texto.center = 75, 50

janela = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('criando um jogo')

janela_aberta =True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP] and y >= 25:
        y -= velocidade
    if comandos[pygame.K_DOWN]and y <= 440:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 750:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 130:
        x -= velocidade

    # detecta colisao

    if ((x + 100 > pos_x and y + 200 > bran_y)):
        y = 100
    if ((x +100 < pos_x and y +200 < bran_y)):
        y = 100


    if (bran_y >= +600):
        bran_y = randint(-1800, -100)
    if (amar_y >= +600):
        amar_y = randint(-1800, -300)
    if (verm_y >=  +600):
        verm_y = randint(-1800, -500)
    if (larj_y >= +600):
        larj_y = randint(-1800, -700)



    if (time < 20):
        time += 1
    else:
        tempo_segundos += 1
        texto = font.render('Pontos ' +str(tempo_segundos), True, (255, 255, 255))
        time = 0
    # velocidades dos carros

    bran_y -= velocidade_outros -2
    amar_y -= velocidade_outros -5
    verm_y -= velocidade_outros -3
    larj_y -= velocidade_outros

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(carro_branco, (pos_x -220, bran_y))
    janela.blit(carro_amarelo, (pos_x -1, amar_y))
    janela.blit(carro_vermelho, (pos_x +170, verm_y))
    janela.blit(carro_laranja, (pos_x +360, larj_y))
    janela.blit(texto, pos_texto)
    pygame.display.update()

pygame.quit()
