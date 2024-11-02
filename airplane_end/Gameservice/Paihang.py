import pygame.display
from DATABASE import database
import  un
import  background
##排行榜界面
class Paihang:
    def __init__(self,root):
        self.root=root
        self.x=80
        self.y=100
        self.background = pygame.image.load('..\\images\\background.png')
    def start(self):
        ##得到数据库排行结果
        results=database.get_paihang()
        self.root.blit(self.background, (0, 0))
        clk=pygame.time.Clock()
        ##绘制标题栏
        self.root.blit(un.font('ID', 32), (self.x, self.y))
        self.root.blit(un.font('NAME', 32), (self.x + 100, self.y))
        self.root.blit(un.font('GRADE', 32), (self.x + 250, self.y))
        self.y += 100
        ##绘制ID,NAME,GRADE
        for text in results:
            self.root.blit(un.font(str(text[0]),32),(self.x,self.y))
            self.root.blit(un.font(text[1], 32), (self.x+100, self.y))
            self.root.blit(un.font(str(text[3]), 32), (self.x+250, self.y))
            self.y+=100
        pygame.display.update()
        ##主循环用来监听退出事件
        ##退出后返回开始界面
        while True:
            clk.tick(60)
            event=pygame.event.get()
            for now in event:
                if now.type==pygame.QUIT:
                    return

