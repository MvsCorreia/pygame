#https://www.canva.com/design/DAGkG2aq86Q/l2S_QreZbaRgXaT9CFZ29g/edit?utm_content=DAGkG2aq86Q&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

import pygame
import random

pygame.init()
pygame.mixer.init()

# Tela
LARGURA, ALTURA = 1200, 768
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pule os Obstáculos")

# Fontes
fonte = pygame.font.Font(None, 36)
fonte_game_over = pygame.font.Font(None, 80)

# Sons


# Imagens
fundo_cor = (50, 50, 50)

jogador_img = pygame.image.load("desafio/assets/personagem.png").convert_alpha()
jogador_img = pygame.transform.scale(jogador_img, (80, 80))

obstaculo_img = pygame.image.load("desafio/assets/obstaculo.png").convert_alpha()
obstaculo_img = pygame.transform.scale(obstaculo_img, (40, 40))

# Relógio
clock = pygame.time.Clock()

# Sprites
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = jogador_img
        self.rect = self.image.get_rect(midbottom=(80, ALTURA - 50))
        self.vel_y = 0
        self.no_chao = True

    def update(self):
        self.vel_y += 1  
        self.rect.y += self.vel_y
        if self.rect.bottom >= ALTURA - 50:
            self.rect.bottom = ALTURA - 50
            self.vel_y = 0
            self.no_chao = True

    def pular(self):
        if self.no_chao:
            self.vel_y = -15 
            self.no_chao = False

class Obstaculo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = obstaculo_img
        self.rect = self.image.get_rect(midbottom=(LARGURA, ALTURA - 50))

    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

# Grupos de sprites
jogador = Jogador()
grupo = pygame.sprite.Group(jogador)
obstaculos = pygame.sprite.Group()

# Temporizador para obstáculos (evento a cada 1.5s)
pygame.time.set_timer(pygame.USEREVENT, 1500)

# Pontuação e tempo
pontos = 0
inicio = pygame.time.get_ticks()

rodando = True
colidiu = False  # flag para indicar colisão

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        #Pulo do personagem



        if evento.type == pygame.USEREVENT and not colidiu:
            obstaculo = Obstaculo()
            grupo.add(obstaculo)
            obstaculos.add(obstaculo)

    if not colidiu:
        grupo.update()

    # Checa colisão
    if not colidiu and pygame.sprite.spritecollide(jogador, obstaculos, False):
        colidiu = True #COLIDIU 


    # Atualiza a pontuação se o jogador passar pelos obstáculos
    if not colidiu:
        for o in obstaculos:
            if o.rect.right < jogador.rect.left and not hasattr(o, 'contado'):
                pontos += 1
                o.contado = True

    # Calcula o tempo decorrido (em segundos)
    tempo = (pygame.time.get_ticks() - inicio) // 1000

    # Desenho da tela
    tela.fill(fundo_cor)
    grupo.draw(tela)
    texto_info = fonte.render(f"Pontos: {pontos}   Tempo: {tempo}s", True, (255, 255, 255))
    tela.blit(texto_info, (10, 10))

    # Caso haja colisão, exibe a tela de Game Over e pausa o jogo
    if colidiu:
        game_over_text = fonte_game_over.render("GAME OVER", True, (255, 0, 0))
        pos_x = LARGURA // 2 - game_over_text.get_width() // 2
        pos_y = ALTURA // 2 - game_over_text.get_height() // 2
        tela.blit(game_over_text, (pos_x, pos_y))
        pygame.display.flip()
        pygame.time.delay(3000)
        rodando = False
    else:
        pygame.display.flip()

    clock.tick(60)

pygame.quit()
