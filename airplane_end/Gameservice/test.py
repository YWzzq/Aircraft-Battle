import random
import pygame.key
import Const
import bigenemy
import enemy
from background import *
from Const import *
from bigenemy import Bigenemy
from enemy import *
from hero import *
from un import *
import Penzhuang
import Gameover
import boss
from DATABASE import database
from Image import sound
import Button
from Image import image
class Airplane:

    def __init__(self,name,root):
        pg.time.set_timer(Const.enemy_creat, 1000)
        pg.time.set_timer(Const.supply_creat,5000)
        self.sc=root
        self.username=name
        self.enemygroup=pg.sprite.Group()
        self.herogroup=pg.sprite.Group(Hero('E:\\桌面\\pic1\\me2.png',WIDE/2,4))
        self.supplys=pg.sprite.Group()
        self.score=[0]
        self.text_score = font('得分:' + str(self.score), 50)
        self.text_bomb=font('* :' + str(self.herogroup.sprites()[0].bomb), 30)
        self.bomb_surface=pygame.image.load('..\\images\\bomb.png')
        self.life_surface=pygame.image.load('..\\images\\life.png')
        sound.play_background_music()
        self.pause=Button.Button(image.pause,430,10,'pause')
        self.resume=Button.Button(image.resume,430,10,'resume')
        self.buttongroup=pg.sprite.Group(self.pause,self.resume)
        self.nandu=0
    ##创建精灵组
    def creat_sprite(self):
        bg1=Background('E:\\桌面\\pic1\\background.png',False,1)
        bg2=Background('E:\\桌面\\pic1\\background.png',True,1)
        self.backgroup=pg.sprite.Group(bg1,bg2)
    ##更新精灵组
    def update_sprite(self):
        self.backgroup.update()
        self.backgroup.draw(self.sc)
        self.enemygroup.update(self.sc,self.score)
        self.herogroup.update(self.sc,self.enemygroup)
        self.herogroup.draw(self.sc)
        self.enemygroup.draw(self.sc)
        self.supplys.update()
        self.supplys.draw(self.sc)
        if self.herogroup.sprites():
            self.draw_surface()

    def exit(self):
        ##关音乐
        pg.mixer.music.stop()
    def draw_surface(self):
        self.text_score = font('得分:' + str(self.score[0]), 50)
        self.sc.blit(self.text_score,(0,0))
        ##弹药显示
        self.sc.blit(self.bomb_surface,(0,700-self.bomb_surface.get_height()))
        if self.herogroup.sprites():
            self.text_bomb=font('* :' + str(self.herogroup.sprites()[0].bomb), 50)
            self.sc.blit(self.text_bomb,(self.bomb_surface.get_width()+10,700-self.bomb_surface.get_height()))

        #life
        for now in range(1,self.herogroup.sprites()[0].help+1):
            self.sc.blit(self.life_surface,(480-now*self.life_surface.get_width(),700-self.life_surface.get_height()))
    def startgame(self):
        self.creat_sprite()
        self.clk=pg.time.Clock()
        while True:
            self.clk.tick(60)
            if self.herogroup.sprites():
                self.penzhuang()
                self.update_sprite()
                self.eventHandler()
                self.pause.update((0, 0))
                self.sc.blit(self.pause.image, self.pause.rect)
            else:
                self.exit()
                now=Gameover.Gameover(self.username,self.sc).start_game()
                if now=='again':
                    self.__init__(self.username,self.sc)
                    self.creat_sprite()
                    self.clk = pg.time.Clock()
                elif now=='gameover':
                    if self.username!='youke':
                         database.addtorecord(database.findbyName(self.username).ID,self.score)
                    self.exit()
                    return 0
            pygame.display.update()
    def eventHandler(self):
        event=pg.event.get()
        for now in event:
            if now.type==Const.supply_creat:
                if random.random()<0.5:
                    self.supplys.add(Bullet('..\\images\\bomb_supply.png',(random.randrange(0,450),0),-1,'bomb_supply'))
                elif self.herogroup.sprites()[0].bullet==1:
                    self.supplys.add(Bullet('..\\images\\bullet_supply.png', (random.randrange(0, 450), 0),-1, 'bullet_supply'))
            elif now.type==pg.QUIT:
                for sprite in self.herogroup.sprites():
                    sprite.kill()
            elif now.type==Const.enemy_creat:
                self.create_enemy()
            elif now.type == pg.MOUSEBUTTONDOWN:
                self.pause.update(now.pos)
            elif now.type==Const.pause_event:
                pg.time.set_timer(Const.pause_event,0)
                self.Resume()

    def create_enemy(self):
        if self.score[0] < 10:
            self.nandu=0
        elif self.score[0]<20:
            self.nandu=1
        else:
            self.nandu=2
        if len(self.enemygroup.sprites())<5:
            self.enemygroup.add(self.creatbyrandom(random.randint(0,self.nandu)))
           # else:
             #   self.enemygroup.add(Boss())
    def creatbyrandom(self,select):
        if select==0:
            return enemy.Enemy()
        elif select==1:
            return bigenemy.Bigenemy()
        else:
            return boss.Boss()
    def penzhuang(self):
        Penzhuang.Pengzhuang().hit(self.herogroup.sprites()[0].bulletgroup,self.enemygroup)
        Penzhuang.Pengzhuang().hit(self.herogroup.sprites()[0].bombgroup, self.enemygroup)
        Penzhuang.Pengzhuang().hitted(self.enemygroup,self.herogroup )
        Penzhuang.Pengzhuang().supply(self.herogroup.sprites()[0],self.supplys)
        #飞机碰撞
        Penzhuang.Pengzhuang().penzhuang(self.herogroup.sprites()[0],self.enemygroup)
    def Resume(self):
        pg.mixer.music.stop()
        while True:
            self.clk.tick(60)
            self.sc.blit(self.resume.image,self.resume.rect)
            self.resume.update((0,0))
            for now in pg.event.get():
                if now.type == pg.MOUSEBUTTONDOWN:
                     self.resume.update(now.pos)
                elif now.type==Const.resume_event:
                    pg.time.set_timer(Const.resume_event,0)
                    sound.play_background_music()
                    return
            pg.display.update()
#pygame.init()
#root=pygame.display.set_mode((480,700))
#Airplane('yws_123',root).startgame()