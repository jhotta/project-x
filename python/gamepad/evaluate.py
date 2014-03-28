#! /usr/bin/env python
# coding: utf-8
# パクったファイルなので、内容にはこだわらないことにする。

import pygame

def init_gamepad():
    pygame.joystick.init()
    try:
        j = pygame.joystick.Joystick(0) # create a joystick instance
        j.init() # init instance
        print 'Joystickの名称: ' + j.get_name()
        print 'ボタン数 : ' + str(j.get_numbuttons())
        print dir(j)
        # print j.get_id()
        # print j.get_init()
        # print j.get_numaxes()
        # print j.get_numhats()
        # print j.get_numballs()
        return j
    except pygame.error:
        print 'Joystickが見つかりませんでした。'

def get_gamepad_action(j):
    pygame.init()
    while 1:
        for e in pygame.event.get(): # イベントチェック
            if e.type == pygame.QUIT: # 終了が押された？
                return
            if (e.type == pygame.KEYDOWN and
                e.key  == pygame.K_ESCAPE): # ESCが押された？
                return
            # Joystick関連のイベントチェック
            if e.type == pygame.JOYAXISMOTION: # 7
                rx , ry = j.get_axis(0), j.get_axis(1)
                lx , ly = j.get_axis(2), j.get_axis(3)
                print 'rx and ry : ' + str(rx) +' , '+ str(ry)
                print 'lx and ly : ' + str(lx) +' , '+ str(ly)
            elif e.type == pygame.JOYBALLMOTION: # 8
                print 'ball motion'
            elif e.type == pygame.JOYHATMOTION: # 9
                print j.get_hat(0)
                print 'hat motion'
            elif e.type == pygame.JOYBUTTONDOWN: # 10
                print str(e.button)+'番目のボタンが押された'
                print [j.get_button(0), j.get_button(1), j.get_button(2), j.get_button(3), j.get_button(4), j.get_button(5), j.get_button(6), j.get_button(7), j.get_button(8), j.get_button(9), j.get_button(10), j.get_button(11), j.get_button(12)]
            elif e.type == pygame.JOYBUTTONUP: # 11
                print str(e.button)+'番目のボタンが離された'

if __name__ == '__main__':
    pad_instance = init_gamepad()
    get_gamepad_action(pad_instance)
