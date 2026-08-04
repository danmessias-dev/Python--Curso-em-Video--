# ==========================================================
# Exercício: Reproduzindo um arquivo MP3
#
# Objetivo:
# Reproduzir um arquivo MP3 utilizando a biblioteca pygame.
#
# Antes de executar:
# pip install pygame
# ==========================================================

import pygame

# Inicializa o mixer responsável pelo áudio
pygame.mixer.init()

# Carrega o arquivo de áudio
pygame.mixer.music.load("Exercicio/MC_Caverinha_Flash.mp3") # Precisa do arquivo MP3 dentro da pasta.

# Inicia a reprodução
pygame.mixer.music.play()

print("🎵 Reproduzindo o áudio...")

# Mantém o programa em execução até o áudio terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)