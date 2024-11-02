import pygame
import Image.image
import  bigenemy
from Image import image
##boss精灵，只用更改需要的各种图片
class Boss(bigenemy.Bigenemy):
    def __init__(self,image=image.enenmy3,speed=1,help=3):
        super().__init__(image,speed,help)
        self.help=help
        self.speed=speed
        self.score=help
        self.hit_images=Image.image.enenmy3_hit
        self.helpimages=[pygame.Surface((self.rect.width, 10)),pygame.Surface((self.rect.width*2//3, 10)),pygame.Surface((self.rect.width//3, 10))]
        self.helpimages[0].fill((0,255,0))
        self.helpimages[1].fill((0, 255, 0))
        self.helpimages[2].fill((255,0 , 0))
