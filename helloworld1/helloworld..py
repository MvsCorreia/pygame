import pygame
pygame.init()

tela = pygame.display.set_mode((600, 400))
fonte = pygame.font.SysFont("Arial", 40)  

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill((0, 0, 0))
    texto = fonte.render("Olá, mundo!", True, (255, 255, 255))
    tela.blit(texto, (180, 180))
    pygame.display.update()

pygame.quit()
