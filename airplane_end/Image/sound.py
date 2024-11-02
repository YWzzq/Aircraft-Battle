import pygame
from pygame.constants import *
pygame.mixer.init()
pygame.mixer.music.load("..\\sound\\game_music.ogg")
pygame.mixer.music.set_volume(0.5)
bomb = pygame.mixer.Sound("..\\sound\\enemy1_down.wav")
big__bomb = pygame.mixer.Sound("..\\sound\\enemy2_down.wav")
boss__bomb = pygame.mixer.Sound("..\\sound\\enemy3_down.wav")
boss__flying = pygame.mixer.Sound("..\\sound\\enemy3_flying.wav")
getbomb=pygame.mixer.Sound('..\\sound\\get_bomb.wav')
getbullet=pygame.mixer.Sound('..\\sound\\get_bullet.wav')
def play_background_music():
    pygame.mixer.music.play(-1)
def playBobmSound():
    pygame.mixer.Sound.play(bomb)
def playBigbobmSound():
    pygame.mixer.Sound.play(big__bomb)
def playBossbobmSound():
    pygame.mixer.Sound.play(boss__bomb)
def playBossflyingSound():
    pygame.mixer.Sound.play(boss__flying)
def playget_bombSound():
    pygame.mixer.Sound.play(getbomb)
def playget_bulletSound():
    pygame.mixer.Sound.play(getbullet)
