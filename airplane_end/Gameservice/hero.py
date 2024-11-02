import time
import pygame
import skill
from Sprite import *
from Const import *
from bullet import *
##英雄机精灵组，主要有三种状态
class Hero(GameSprite):
    def __init__(self,imagname,pos,speed=2):
        super().__init__(imagname,speed)
        ##英雄位置
        self.rect.x=pos-self.rect.width/2
        self.rect.y=HIGH-self.rect.height
        ##子弹组
        self.bulletgroup=pg.sprite.Group()
        ##穿透导弹组
        self.bombgroup=pg.sprite.Group()
        ##技能组
        self.skillgroup=pg.sprite.Group(skill.Skill('..\\images\\enemy1_down3.png','all',(480-59,500)))
        ##记录发射子弹时间，控制发射子弹间隔
        self.last_short_time=0
        self.help=4
        self.now='good'
        ##被击中时间，主要用来制作击中以及毁灭动画
        self.hittime=0
        ##导弹数量
        self.bomb=3
        ##火力值
        self.bullet=1
        ##获得二倍火力值冷却
        self.bullet_time=0

    ##键盘控制
    def update(self,root,enemys):
        if self.help==0:
            self.now='over'
        if self.now=='good':
            self.key_control(enemys)
            self.alter()
        elif self.now=='hit':
            if pygame.time.get_ticks()-self.hittime<500:
                self.image=pygame.image.load('..\\images\\me_destroy_1.png')
            else:
                self.image=pygame.image.load('..\\images\\me1.png')
                self.now='good'
        else:
            if pygame.time.get_ticks() - self.hittime < 150:
                self.image = pygame.image.load('..\\images\\me_destroy_1.png')
            elif pygame.time.get_ticks() - self.hittime<300:
                self.image = pygame.image.load('..\\images\\me_destroy_2.png')
            elif pygame.time.get_ticks() - self.hittime<450:
                self.image = pygame.image.load('..\\images\\me_destroy_3.png')
            elif pygame.time.get_ticks() - self.hittime<600:
                self.image = pygame.image.load('..\\images\\me_destroy_4.png')
            else:
                self.kill()
        self.skillgroup.update()
        ##更新图标
        for skill in self.skillgroup.sprites():
            if skill.skill[1]:
                root.blit(skill.image,skill.rect)
        self.bombgroup.update()
        self.bombgroup.draw(root)
        self.bulletgroup.update()
        self.bulletgroup.draw(root)

    def key_control(self,enemys):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE]:
            current_time = time.time()
            # ￥每0.5秒允许一个子弹
            if current_time - self.last_short_time > 0.1:
                self.last_short_time = current_time
                ##加子弹发射
                if self.bullet == 1:
                    self.bulletgroup.add(Bullet('..\\images\\bullet1.png', self.rect.midtop, 2))
                else:
                    self.bulletgroup.add(
                        Bullet('..\\images\\bullet1.png', (self.rect.midtop[0] - 38, self.rect.midtop[1] + 24), 2))
                    self.bulletgroup.add(
                        Bullet('..\\images\\bullet1.png', (self.rect.midtop[0] + 38, self.rect.midtop[1] + 24), 2))
                    if pygame.time.get_ticks() - self.bullet_time > 10000:
                        self.bullet = 1
        if keys[pygame.K_1]:
            if self.bomb > 0:
                current_time = time.time()
                if current_time - self.last_short_time > 1:
                    self.last_short_time = current_time
                    self.bomb -= 1

                    self.bombgroup.add(
                        Bullet('..\\images\\bomb.png', (self.rect.x + self.rect.width / 2 - 20, self.rect.y - 1),
                               3, 'bomb'))
        if keys[pygame.K_2]:
            self.skillgroup.sprites()[0].all(enemys)

    def alter(self):
        if(self.rect.x<0):
            self.rect.x=0
        if self.rect.y<0:
            self.rect.y=0
        if self.rect.x>WIDE-self.rect.width:
            self.rect.x=WIDE-self.rect.width
        if self.rect.y>HIGH-self.rect.height:
            self.rect.y=HIGH-self.rect.height