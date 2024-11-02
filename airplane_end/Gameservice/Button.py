from Gameservice import Sprite
import pygame as pg
import  Paihang
import  record
import Const
#按钮类，处理pygame界面开始游戏等按钮控制
##通过按钮名字判断触发哪种事件
class Button(Sprite.GameSprite):
    def __init__(self,image,x,y,name):
        super().__init__(image[0])
        self.rect.x=x
        self.rect.y=y
        self.images=image
        self.time=0
        self.name=name
        self.press=False
    def update(self, pos):
        ##判断按钮是否按下
        if pos[0]<self.rect.right and pos[0]>self.rect.left and pos[1]<self.rect.bottom and pos[1]>self.rect.top:
            self.time=pg.time.get_ticks()##记录按键时间
            self.image=pg.image.load(self.images[1])
            self.press=True

        else:
            if(pg.time.get_ticks()-self.time>100):##保留100s按下图片，之后切换正常图片
                self.image=pg.image.load(self.images[0])
                if self.press:
                    self.press=False
                    ##根据按键名开始相应定时器事件
                    if (self.name == 'start'):
                        pg.time.set_timer(Const.start_event,100)
                    elif(self.name=='paihang'):
                        pg.time.set_timer(Const.paihang_event, 100)

                    elif self.name=='histroy':
                        pg.time.set_timer(Const.histroy_event, 100)
                    elif self.name=='again':
                        pg.time.set_timer(Const.again_event, 100)
                    elif self.name=='gameover':
                        pg.time.set_timer(Const.gameover_event, 100)
                    elif self.name=='pause':
                        pg.time.set_timer(Const.pause_event,100)
                    elif self.name=='resume':
                        pg.time.set_timer(Const.resume_event, 100)
