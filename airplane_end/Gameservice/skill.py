import pygame.time
import Sprite
##技能类
class Skill(Sprite.GameSprite):
    ##技能字典
    ##技能名称为键
    ##值包括 技能冷却时间、技能是否准备好、上次使用技能时间
    allskill = {'all': [5000, True, 0]}
    ##需要给出技能名称，技能图标位置
    def __init__(self,imagename,skillname,pos):
        super().__init__(imagename)
        ##
        self.skillname=skillname
        self.skill=Skill.allskill[skillname]
        self.rect.x=pos[0]
        self.rect.y=pos[1]
    ##全屏攻击技能‘all’
    ##传入敌机组，所有生命值减一
    def all(self,enemys):
        if self.skill[1]:
            #技能重置
            self.skill[1]=False
            self.skill[2]=pygame.time.get_ticks()
            if enemys:
                for enemy in enemys.sprites():
                    enemy.hittime=pygame.time.get_ticks()
                    enemy.help-=1

    ##更新技能冷却时间
    def update(self, *args):
        if pygame.time.get_ticks()-self.skill[2]>self.skill[0]:
            self.skill[1]=True
