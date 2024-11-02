from Sprite import *
##子弹精灵包括速度、种类主要属性
class Bullet(GameSprite):
    #附带英雄机位置
    def __init__(self,imagname,position,dir,kind='bullet'):
        super().__init__(imagname)
        self.rect.x=position[0]
        self.rect.y=position[1]
        self.speed=dir
        self.kind=kind
        print(self.kind)
    def update(self, *args):
        if self.rect.y<0 or self.rect.y>730:
            self.kill()
        else:
            self.rect.y-=self.speed