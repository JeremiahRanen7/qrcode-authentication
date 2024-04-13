import pygame

pygame.mixer.init()
authorized_sound = pygame.mixer.Sound("authorized.wav")
unauthorized_sound = pygame.mixer.Sound("unauthorized.wav")

def play_sound(myOutput):
    if myOutput == "Authorized":
        authorized_sound.play()
    else:
        unauthorized_sound.play()
