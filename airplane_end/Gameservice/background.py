from Gameservice import Sprite
#背景精灵
class Background(Sprite.GameSprite):
    def __init__(self,imagname,select,speed=1):
        super().__init__(imagname,speed)
        if(select):
            self.rect.y=self.rect.height
    def update(self):
        if self.rect.y>=self.rect.height:
            self.rect.y=-self.rect.height
        self.rect.y+=self.speed

