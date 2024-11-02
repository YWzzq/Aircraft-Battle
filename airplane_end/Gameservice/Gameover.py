import sys
import pygame as pg
import Const
from Image import image
from Gameservice import background
from Gameservice import Button
import un
##绘制游戏结束动画
class Gameover:
    ##name为用户名，用来根据用户名将成绩写入数据库
    def __init__(self,name,root):
        self.name=name
        self.root=root
        self.text1=un.font('GAMEOVER',80)
        self.again=Button.Button(image.again_button,100,280,'again')
        self.gameover=Button.Button(image.gameover_button,100,480,'gameover')
        self.background=pg.image.load(image.background)
        self.buttongroup=pg.sprite.Group(self.again,self.gameover)
    def start_game(self):
        self.clk = pg.time.Clock()
        while True:
            self.clk.tick(60)
            self.buttongroup.update((0,0))
            ##得到按钮事件处理的结果
            now=self.event_handler()
            ##只要得到事件触发的结果就退出，到主游戏界面
            if now:
                return now
            self.root.blit(self.background,(0,0))
            self.root.blit(self.text1, (45, 140))
            self.buttongroup.draw(self.root)
            pg.display.update()
    ##j监听按钮触发的定时器事件，并将结果返回到主循环
    def event_handler(self):
        event=pg.event.get()
        for now in event:
            if now.type==pg.QUIT:
                pg.quit()
                sys.exit()
            elif now.type==pg.MOUSEBUTTONDOWN:
                self.buttongroup.update(now.pos)
            elif now.type==Const.again_event:
                pg.time.set_timer(Const.again_event,0)
                return 'again'
            elif now.type==Const.gameover_event:
                pg.time.set_timer(Const.gameover_event, 0)
                return 'gameover'
        return None