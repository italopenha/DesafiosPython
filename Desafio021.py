# Este programa abre e reproduz um arquivo MP3.
import pygame

pygame.init()
pygame.mixer.music.load("d021.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()