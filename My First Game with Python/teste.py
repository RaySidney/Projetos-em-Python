import pygame
pygame.init()
x =400
y = 300
velocidade = 10

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('brawl')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    comandos = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        if comandos[pygame.K_UP]:
            y -= velocidade
        if comandos[pygame.K_DOWN]:
            y += velocidade
        if comandos[pygame.K_RIGHT]:
            x += velocidade
        if comandos[pygame.K_LEFT]:
            x -= velocidade

        janela.fill((0, 0, 0))
    pygame.draw.circle(janela, (4, 230, 168), (x, y), 50)
    pygame.display.update()

pygame.quit()
