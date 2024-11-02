import random
import Image.image
from Image import sound
import pygame.sprite
import bullet
from Const import *
from Sprite import  *
##初始敌机精灵类
class Enemy(GameSprite):
    ##初始化传入图片路径，设置速度，生命值
    def __init__(self,imagname=Image.image.enenmy1,speed=2,help=1):
        super().__init__(imagname,speed)
        ##生成位置x坐标随机
        self.rect.x=random.randrange(1,WIDE-self.image.get_rect().width-1)
        self.rect.y=-self.image.get_rect().height
        #飞机子弹组
        self.bullets=pygame.sprite.Group()
        ##记录被击中时间，控制动画切换
        self.hittime=0
        ##初始状态
        self.now='good'
        self.help=help
        ##记录发射子弹时间，用来控制发射间隔
        self.bullet_time=0
        #飞机击毁得分
        self.score=help
    ##更新精灵组
    def update(self,root,score):
        if self.help==0:
            self.now='over'
        if self.now == 'good':
            self.move()
            self.fire()
            self.bullets.update()
            self.bullets.draw(root)
        elif self.now == 'over':
            self.over(Image.image.enenmy1_down,score)
    ##子弹添加控制
    def fire(self,time=1500):#time为间隔时间
        if pygame.time.get_ticks() - self.bullet_time > time:
            self.bullet_time = pygame.time.get_ticks()
            self.bullets.add(
                bullet.Bullet('..\\images\\bullet2.png',
                              (self.rect.left + self.rect.width // 2, self.rect.bottom),
                              -3))
    #控制击毁图片切换
    def over(self,images,score):
        image=images
        select=(pygame.time.get_ticks()-self.hittime)//50#50为更新间隔
        print(select)
        if select>len(image)-1:
            sound.playBobmSound()
            score[0] += self.score
            print(score)
            self.kill()
        else:
            self.image = pygame.image.load(image[select])

    def move(self):
        if self.rect.y >= HIGH:
            self.kill()
        else:
            self.rect.y+=self.speed
