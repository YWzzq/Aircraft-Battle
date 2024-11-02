import pygame
##储存一些常量
##屏幕大小
WIDE=480
HIGH=700
##定时器事件
enemy_creat=pygame.USEREVENT
supply_creat=enemy_creat+1
again_event=supply_creat+1
gameover_event=again_event+1
start_event=gameover_event+1
paihang_event=start_event+1
histroy_event=paihang_event+1
pause_event=histroy_event+1
resume_event=pause_event+1