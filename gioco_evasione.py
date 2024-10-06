import pygame
import random

# Inizializza Pygame
pygame.init()

# Dimensioni della finestra
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Evasione del Quadrato")

# Colori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font per lo score
font = pygame.font.SysFont("Arial", 30)

# Variabili del giocatore
player_size = 50
player_x = width // 2
player_y = height - 2 * player_size
player_speed = 10

# MODIFICA DEL CODE (QUI TI HO MESSO GLI ASSETS)
player_image = pygame.image.load("assets/navicella.png")  
player_image = pygame.transform.scale(player_image, (player_size, player_size))

enemy_image = pygame.image.load("assets/enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

# Variabili dei nemici
enemy_size = 50
enemy_speed = 5
enemies = [[random.randint(0, width - enemy_size), 0]]

# Variabile dello score
score = 0

# Clock per il controllo dei frame
clock = pygame.time.Clock()

# QUA TI HO MESSO LO SCORE
def show_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Funzione principale del gioco
def game_loop():
    global player_x, player_y, score
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed

        # Aggiornamento nemici
        if len(enemies) < 10 and random.randint(1, 20) == 1:
            enemies.append([random.randint(0, width - enemy_size), 0])

        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > height:
                enemies.remove(enemy)
                score += 1  # Incrementa lo score quando un nemico viene evitato

            # Collisione
            if (enemy[0] < player_x < enemy[0] + enemy_size or
                enemy[0] < player_x + player_size < enemy[0] + enemy_size) and \
               (enemy[1] < player_y < enemy[1] + enemy_size or
                enemy[1] < player_y + player_size < enemy[1] + enemy_size):
                game_over = True

        # Disegna tutto
        screen.fill(BLACK)
        screen.blit(player_image, (player_x, player_y))
        for enemy in enemies:
            screen.blit(enemy_image, (enemy[0], enemy[1]))

        # Mostra lo score
        show_score(score)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Avvia il gioco
game_loop()
