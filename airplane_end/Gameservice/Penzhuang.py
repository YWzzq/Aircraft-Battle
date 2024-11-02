import pygame.sprite
from  Image import sound
class Pengzhuang:
    ##敌机与子弹碰撞
    def hit(self,bullets,airplanes):
        if bullets and airplanes:
            select = True

            if bullets.sprites()[0].kind == 'bomb':
                select = False

            dic = pygame.sprite.groupcollide(airplanes, bullets, False, select)
            for airplane in airplanes.sprites():
                if airplane in dic:
                    # 防止重复刷新
                    if airplane.now == 'good':
                        airplane.now='hit'
                        airplane.help-=1

                        airplane.hittime = pygame.time.get_ticks()
    ##英雄机被子弹击中检测
    def hitted(self,enemys,heros):
        for enemy in enemys.sprites():
            self.hit(enemy.bullets,heros)
    #飞机碰撞检查
    def penzhuang(self,hero,ennemys):
        list=pygame.sprite.spritecollide(hero,ennemys,False)
        if list:
            select=False#是否有效碰撞
            if hero.now=='good':
                for ennemy in list:
                    if ennemy.now == 'good':
                        ennemy.now='hit'
                        ennemy.help-=1
                        select=True
                        ennemy.hittime = pygame.time.get_ticks()
                if select:
                    hero.now='hit'
                    hero.hittime=pygame.time.get_ticks()
                    hero.help-=1

    #不急碰撞检测
    def supply(self,hero,supplys):
        list=pygame.sprite.spritecollide(hero,supplys,True)
        if list:
            if list[0].kind=='bomb_supply':
                hero.bomb+=1
                sound.playget_bombSound()
            else:
                sound.playget_bulletSound()
                ##控制子弹冷却时间
                hero.bullet_time=pygame.time.get_ticks()
                hero.bullet+=1