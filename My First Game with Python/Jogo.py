import pygame
from random import *

pygame.init()

playerx = 380 # Min 120 Max 620 380 def
playery = 230
pos_x1 = randint(320, 430)
pos_x2 = randint(520, 620)
pos_x3 = randint(120, 230)

pos_y1 = randint(800, 2000)  # TÁXI
pos_y2 = randint(800, 2000)  # POLICIA
pos_y3 = randint(800, 2000)  # PICAPE

timer = 0
tempo_segundo = 0

velocidade = 10
velocidade_game1 = 15
velocidade_game2 = velocidade_game3 = 15

fundo = pygame.image.load('pista.png')
player = pygame.image.load('Carro.png')
picape = pygame.image.load('picape.png')
taxi = pygame.image.load('taxi.png')

policia = pygame.image.load('policecar.png')
colisao = [player, picape, taxi, policia]
font = pygame.font.SysFont('arial black', 20)
texto = font.render("Tempo: ", True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center =(45, 20)
gamerover = font.render('Game Over!', True, (255, 255, 255), (0, 0, 0))

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Meu game")

janela_aberta = True

fase = 0

while janela_aberta:

    pygame.time.delay(40)

    apertar = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    if fase == 5:
        velocidade_game1 = randint(15, 30) # TÁXI
        velocidade_game2 = randint(15, 30) # POLICIA
        velocidade_game3 = randint(15, 30) # PICAPE

    if fase == 7:
        velocidade_game1 = randint(15, 35) # TÁXI
        velocidade_game2 = randint(15, 35) # POLICIA
        velocidade_game3 = randint(15, 35) # PICAPE

    if fase == 10:
        velocidade_game1 = randint(15, 35) # TÁXI
        velocidade_game2 = randint(15, 35) # POLICIA
        velocidade_game3 = randint(15, 35) # PICAPE

    if fase == 13:
        velocidade_game1 = randint(15, 35) # TÁXI
        velocidade_game2 = randint(15, 35) # POLICIA
        velocidade_game3 = randint(15, 35) # PICAPE

    if fase == 15:
        velocidade_game1 = randint(15, 35) # TÁXI
        velocidade_game2 = randint(15, 35) # POLICIA
        velocidade_game3 = randint(15, 35) # PICAPE

    if fase == 20:
        velocidade_game1 = randint(15, 35) # TÁXI
        velocidade_game2 = randint(15, 35) # POLICIA
        velocidade_game3 = randint(15, 35) # PICAPE


    if apertar[pygame.K_UP]:
        playery -= velocidade

    if apertar[pygame.K_DOWN] :
        playery += velocidade

    if apertar[pygame.K_LEFT] and playerx >= 130:
        playerx -= velocidade

    if apertar[pygame.K_RIGHT] and playerx <= 610:
        playerx += velocidade

    pos_y1 -= velocidade_game1
    pos_y2 -= velocidade_game2
    pos_y3 -= velocidade_game3

    if pos_y1 <= -200: # TÁXI
        pos_y1 = randint(800, 1500)
        pos_x1 = randint(320, 430)
        fase += 1

    if pos_y2 <= -200: # POLICIA
        pos_y2 = randint(800, 1500)
        pos_x2 = randint(520, 620)

    if pos_y3 <= -200: # PICAPE
        pos_y3 = randint(1000, 2000)
        pos_x3 = randint(120, 230)


    if playery <= -150:
        playery = 600

    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render(f"Tempo: {str(tempo_segundo)}", True, (255, 255, 255), (0, 0, 0))
        timer = 0

    janela.blit(fundo, (0, 0))
    janela.blit(player, (playerx, playery))

    janela.blit(taxi, (pos_x1, pos_y1))
    janela.blit(policia, (pos_x2, pos_y2))
    janela.blit(picape, (pos_x3, pos_y3))
    janela.blit(texto, pos_texto)

    pygame.display.update()

pygame.quit()
