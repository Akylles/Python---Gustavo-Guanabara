import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('elomar.mp3')
pygame.mixer.Sound('elomar.mp3')
pygame.mixer.music.play()
pygame.event.wait()
