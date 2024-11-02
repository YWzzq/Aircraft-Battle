import pygame.display
from DATABASE import database
import  un
import  background
import  Const
##绘制历史记录界面，与排行类似
class Record:
    def __init__(self,root):
        self.root=root
        self.x=50
        self.y=100
        self.background = pygame.image.load('..\\images\\background.png')
    def start(self,name):
        results=database.get_record(name)
        self.root.blit(self.background, (0, 0))
        clk=pygame.time.Clock()
        self.root.blit(un.font('TIME', 25), (self.x, self.y))
        self.root.blit(un.font('GRADE', 25), (self.x + 300, self.y))
        self.y += 80
        for text in results:
            self.root.blit(un.font(str(text[1]),25),(self.x,self.y))
            self.root.blit(un.font(str(text[0]), 25), (self.x+300, self.y))
            self.y+=80
        pygame.display.update()
        while True:
            clk.tick(60)
            event=pygame.event.get()
            for now in event:
                if now.type==pygame.QUIT:
                    return
