# Este programa abre e reproduz um arquivo MP3.
import pygame

def reproduzirMusica(arquivo):
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(arquivo)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue
    except pygame.error as e:
        print('Erro')

    pygame.mixer.quit()


reproduzirMusica("Helium - TrackTribe.mp3")