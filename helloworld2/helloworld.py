import pygame

pygame.init()

tela = pygame.display.set_mode((600, 400))
imagem = pygame.image.load("helloworld2/assets/imagem.png")


rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((255, 255, 255))
    tela.blit(imagem, (0, 0))
    pygame.display.update()

pygame.quit()
