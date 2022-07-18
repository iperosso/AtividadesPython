""" DESAFIO 021
    FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA O AUDIO DE UM ARQUIVO MP3"""

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
