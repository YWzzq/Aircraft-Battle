import sys
import pygame as pg
from Image import image
from Gameservice import Const
from Gameservice import un
from Gameservice import background
from Gameservice import Button
import test
import Paihang
import record
class Startgame:
    def __init__(self,name):
        ##初始化
        pg.init()
        ##记录用户名
        self.name=name
        ##创建窗口
        self.root=pg.display.set_mode((Const.WIDE,Const.HIGH))
        self.text1=un.font('飞机大战',80)
        ##添加背景
        self.background = pg.image.load(image.background)
        ##添加三个按钮
        self.start=Button.Button(image.start_button,100,280,'start')
        self.paihang=Button.Button(image.paihang_button,100,380,'paihang')
        self.history= Button.Button(image.histroy_button,100, 480,'histroy')
        self.buttongroup=pg.sprite.Group(self.start)
        ##游客登录无排行和历史记录
        if name!='youke':
            self.buttongroup.add(self.history,self.paihang)
    ##主函数
    def start_game(self):
        self.clk = pg.time.Clock()
        while True:
            self.clk.tick(60)
            self.buttongroup.update((0,0))
            self.event_handler()
            self.root.blit(self.background,(0,0))
            self.root.blit(self.text1, (90, 140))
            self.buttongroup.draw(self.root)
            pg.display.update()
    ##用来监听相应按钮，并调用相应函数，以及退出事件
    def event_handler(self):
        event=pg.event.get()
        for now in event:
            if now.type==pg.QUIT:
                pg.quit()
                sys.exit()
            elif now.type==pg.MOUSEBUTTONDOWN:
                self.buttongroup.update(now.pos)
            elif now.type==Const.start_event:
                pg.time.set_timer(Const.start_event, 0)
                test.Airplane(self.name, self.root).startgame()
            elif now.type==Const.paihang_event:
                pg.time.set_timer(Const.paihang_event, 0)
                Paihang.Paihang(self.root).start()
            elif now.type==Const.histroy_event:
                pg.time.set_timer(Const.histroy_event, 0)
                record.Record(self.root).start(self.name)