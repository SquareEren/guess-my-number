import pygame
import sys
import random

pygame.init()
arkaplan_resmi = pygame.image.load("samuraidog.jpg")
screen_width = 460
screen_height = 460

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

# Yeni sayı seçme fonksiyonu
def select_new_number():
    return random.randint(1, 100)

number = select_new_number()

# Oyun döngüsü
user_input = ''  # Kullanıcı girişini tutmak için boş bir string oluşturun
show_result = False  # Sonucu göstermek için bir bayrak
# Metin giriş kutusu
input_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 16, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = True
# Oyun döngüsü
user_input = ''  # Kullanıcı girişini tutmak için boş bir string oluşturun
show_result = False  # Sonucu göstermek için bir bayrak
pygame.draw.rect(screen, color, input_rect, 2)  # Metin giriş kutusunun çizilmesi
text_surface4 = font.render(user_input, True, BLACK)
screen.blit(text_surface4, (input_rect.x + 5, input_rect.y + 5))  # Metnin metin giriş kutusunun içine yazılması

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Kullanıcının tahmini
                guess = int(user_input)
                # Tahmini kontrol et
                if guess == number:
                    message = "Tebrikler! Sayıyı buldunuz."
                    # Yeni sayı seç
                    number = select_new_number()
                elif guess < number:
                    message = "Daha yüksek bir sayı tahmin edin."
                else:
                    message = "Daha düşük bir sayı tahmin edin."
                # Tahmin sonucunu ekrana yazdır
                text = font2.render(message, True, (255, 255, 255))
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 40))
                show_result = True
                user_input = ''  # Kullanıcının tahminini temizleyin

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode
    # Arka plan resmini çiz
    screen.blit(arkaplan_resmi, (0, 0))
    
    # Metin giriş kutusunu çiz
    pygame.draw.rect(screen, color, input_rect, 4)
    text_surface4 = font2.render(user_input, True, WHITE)
    screen.blit(text_surface4, (input_rect.x + 5, input_rect.y + 5))

    # Ekrana yazı yaz
    message = "Guess a number between 1 to 100"
    text2 = font2.render(message, True, WHITE)
    text_rect2 = text2.get_rect(center=(screen_width // 2, screen_height // 4))
    screen.blit(text2, text_rect2)
  
    # Diğer yazıları çiz
    screen.blit(text_surface, (x, y))
    screen.blit(text_surface2, (z, q))
    screen.blit(text_surface3, (b, a))
    if show_result:
        screen.blit(text, text_rect)  # Tahmin sonucunu ekrana yazdırın

    # Ekrana güncelleme yap
    pygame.display.update()
