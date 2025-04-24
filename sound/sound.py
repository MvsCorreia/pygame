import pygame

pygame.init()
pygame.mixer.init()  # Inicializa o mixer de som

# Carrega um efeito sonoro (formato: WAV, OGG ou compatível)
som = pygame.mixer.Sound("sound/assets/jump.mp3")

tela = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Exemplo de Som")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()     

        if evento.type == pygame.KEYDOWN:  
            if evento.key == pygame.K_SPACE:
                som.play()  

    tela.fill((30, 30, 30))
    pygame.display.flip() 