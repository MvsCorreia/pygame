import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("music/assets/musica.mp3")

pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((400, 300))

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

pygame.quit()
