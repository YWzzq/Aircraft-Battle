import pygame
import Image.image
import enemy
##中型敌机类
##继承小敌机类，更改move函数以及增加hit状态、击中动画
##并增加血条
class Bigenemy(enemy.Enemy):
    def __init__(self,imagename=Image.image.enenmy2,speed=1,help=2):
        super().__init__(imagename,speed,help)
        self.direction = 'right'
        self.helpimages=[pygame.Surface((self.rect.width, 10)),pygame.Surface((self.rect.width//2, 10))]
        self.helpimages[0].fill((0,255,0))
        self.helpimages[1].fill((255, 0, 0))
        self.hit_images=Image.image.enenmy2_hit#击中图片列表
        self.over_images=Image.image.enenmy1_down#毁灭图片列表
    def update(self,root,score):
        #根据血量更改状态
        if self.help==0:
            self.now='over'
        if self.now == 'good':
            self.move()
            self.fire()
            self.bullets.update()
            self.bullets.draw(root)
            self.helpupdate(root)
        elif self.now=='hit':
            self.hit(self.hit_images)
            self.helpupdate(root)
        elif self.now == 'over':
            self.over(self.over_images,score)
    #血条更新
    def helpupdate(self,root):
        root.blit(self.helpimages[self.score-self.help],(self.rect.left,self.rect.top-10))
    #击中动画控制
    def hit(self,hitimages):
        if pygame.time.get_ticks() - self.hittime < 500:
            self.image = pygame.image.load(hitimages[1])
        else:
            self.image = pygame.image.load(hitimages[0])
            self.now = 'good'

    def move(self):
        if self.rect.y >= 700:
            self.kill()
        if self.direction == 'right':
            self.rect.right += self.speed
        elif self.direction == 'left':
            self.rect.right -= self.speed
        if self.rect.right > 480:
            self.direction = 'left'
        elif self.rect.right < self.image.get_width():
            self.direction = 'right'
        self.rect.bottom += self.speed

