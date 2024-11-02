import pygame as pg
##基础精灵类
##实现基础移动以及加载图片，设置大小
class GameSprite(pg.sprite.Sprite):
    def __init__(self,imagname,speed=1):
        super().__init__()
        self.image=pg.image.load(imagname)
        self.rect=self.image.get_rect()
        self.speed=speed
    def update(self, *args):
        self.rect.y+=self.speed
