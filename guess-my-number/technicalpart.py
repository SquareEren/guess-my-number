import pygame
import random
import sys

# Ekran boyutu
WIDTH = 800
HEIGHT = 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Oyunu başlat
pygame.init()

# Ekranı oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sayı Tahmin Oyunu")

# Font
font = pygame.font.Font("font.ttf", 25)

# Yeni sayı seçme fonksiyonu
def select_new_number():
    return random.randint(1, 100)

number = select_new_number()
# Metin giriş kutusu
input_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 16, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
user_input = ''
show_result = False

# Oyun döngüsü
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
                text = font.render(message, True, BLACK)
                text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
                screen.blit(text, text_rect)
                pygame.display.update()
                # Metin giriş kutusunu temizle
                user_input = ''
                show_result = True
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

    # Arka planı beyaz yap
    screen.fill(WHITE)

    # Metin giriş kutusunu çiz
    pygame.draw.rect(screen, color, input_rect, 2)
    text_surface = font.render(user_input, True, BLACK)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Ekrana yazı yaz
    message = "1 ile 100 arasında bir sayı tahmin edin ve ENTER tuşuna basın."
    text = font.render(message, True, BLACK)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//4))
    screen.blit(text, text_rect)

    # Tahmin sonucunu ekranda tut
    if show_result:
        pygame.time.wait(2000)  # 2 saniye beklet
        show_result = False

    # Ekranı güncelle
    pygame.display.update()
