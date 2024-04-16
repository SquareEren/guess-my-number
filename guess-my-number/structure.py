import pygame
import sys

pygame.init()
arkaplan_resmi = pygame.image.load("samuraidog.jpg")
screen_width = arkaplan_resmi.get_width()
screen_height = arkaplan_resmi.get_height()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Guess Samurai Dog's Number!")

font = pygame.font.Font("font.ttf", 42)
text_surface = font.render("Samurai Dog's", True, (255, 255, 255))

text_width, text_height = font.size("Samurai Dog")
x = (screen.get_width() - text_width) / 2
y = (screen.get_height() - text_height) / 16

font2 = pygame.font.Font("font.ttf", 20)
text_surface2 = font2.render("Number!", True, (255, 255, 255))

text_width2, text_height2 = font2.size("Guesses Your Number!")
z = (screen.get_width() - text_width2) / 1 + 70
q = (screen.get_height()) / 6

font3 = pygame.font.Font("font.ttf", 20)
text_surface3 = font3.render("Guess", True, (255, 255, 255))

text_width3, text_height3 = font3.size("Guesses Your Number!")
b = (screen.get_width() - text_width3) / 1 - 140
a = (screen.get_height()) / 30

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(arkaplan_resmi, (0, 0))
    screen.blit(text_surface, (x, y))
    screen.blit(text_surface2, (z, q))
    screen.blit(text_surface3, (b, a))
    pygame.display.update()