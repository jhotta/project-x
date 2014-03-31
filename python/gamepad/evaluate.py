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
        print j.get_id()
        print j.get_init()
        print j.get_numaxes()
        print j.get_numhats()
        print j.get_numballs()
        return j
    except pygame.error:
        print 'Joystickが見つかりませんでした。'

def get_gamepad_action(j):
    axis_value = {'0':0.0, '1':0.0, '2':0.0, '3':0.0}
    pygame.init()
    pygame.display.set_mode((240, 240))
    while 1:
        # print axis_value
        for e in pygame.event.get(): # イベントチェック
            # print e
            # Joystick関連のイベントチェック
            if e.type == pygame.JOYAXISMOTION: # 7
                # print str(e.axis)
                # print e.value
                axis_value[str(e.axis)] = e.value
                print axis_value
                # rx , ry = j.get_axis(0), j.get_axis(1)
                # lx , ly = j.get_axis(2), j.get_axis(3)
                #print 'rx and ry : ' + str(rx) +' , '+ str(ry)
                #print 'lx and ly : ' + str(lx) +' , '+ str(ly)
            elif e.type == pygame.JOYBALLMOTION: # 8
                print e.value
                print 'ball motion'
            elif e.type == pygame.JOYHATMOTION: # 9
                # import pdb; pdb.set_trace()
                print e.value
                # print j.get_hat(0)
                print 'hat motion'
            elif e.type == pygame.JOYBUTTONDOWN: # 10
                print str(e.button)+'番目のボタンが押された'
            elif e.type == pygame.JOYBUTTONUP: # 11
                print str(e.button)+'番目のボタンが離された'

if __name__ == '__main__':
    pad = init_gamepad()
    get_gamepad_action(pad)
