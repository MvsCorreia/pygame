
import pygame


pygame.init()

tela = pygame.display.set_mode((400, 300))

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprite/assets/personagem.png")
        self.rect = self.image.get_rect(center=(200, 150))

sprites = pygame.sprite.Group(Jogador())

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

    tela.fill((0, 0, 0))
    sprites.draw(tela)
    pygame.display.flip()

pygame.quit()

