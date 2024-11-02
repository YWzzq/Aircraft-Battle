import pygame as pg
##创建文字对象
def font(string,size,name='华文隶书'):
    font = pg.font.SysFont(name, size, bold=False, italic=False)
    text= font.render(string, True, (0, 0, 0), None)
    return text