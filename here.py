#!/usr/bin/env python3
""" usage: passthrough-serial
"""
import pygame
# coding: utf-8

py_map={
    pygame.K_LCTRL:"KEY_LEFT_CTRL",
    pygame.K_LSHIFT:"KEY_LEFT_SHIFT",
    pygame.K_LALT:"KEY_LEFT_ALT",
    pygame.K_LSUPER:"KEY_LEFT_GUI",
    pygame.K_RCTRL:"KEY_RIGHT_CTRL",
    pygame.K_RSHIFT:"KEY_RIGHT_SHIFT",
    pygame.K_RALT:"KEY_RIGHT_ALT",
    pygame.K_RSUPER:"KEY_RIGHT_GUI",
    pygame.K_UP:"KEY_UP_ARROW",
    pygame.K_DOWN:"KEY_DOWN_ARROW",
    pygame.K_LEFT:"KEY_LEFT_ARROW",
    pygame.K_RIGHT:"KEY_RIGHT_ARROW",
    pygame.K_BACKSPACE:"KEY_BACKSPACE",
    pygame.K_TAB:"KEY_TAB",
    pygame.K_RETURN:"KEY_RETURN",
    pygame.K_ESCAPE:"KEY_ESC",
    pygame.K_INSERT:"KEY_INSERT",
    pygame.K_DELETE:"KEY_DELETE",
    pygame.K_PAGEUP:"KEY_PAGE_UP",
    pygame.K_PAGEDOWN:"KEY_PAGE_DOWN",
    pygame.K_HOME:"KEY_HOME",
    pygame.K_END:"KEY_END",
    pygame.K_CAPSLOCK:"KEY_CAPS_LOCK",
    pygame.K_F1:"KEY_F1",
    pygame.K_F2:"KEY_F2",
    pygame.K_F3:"KEY_F3",
    pygame.K_F4:"KEY_F4",
    pygame.K_F5:"KEY_F5",
    pygame.K_F6:"KEY_F6",
    pygame.K_F7:"KEY_F7",
    pygame.K_F8:"KEY_F8",
    pygame.K_F9:"KEY_F9",
    pygame.K_F10:"KEY_F10",
    pygame.K_F11:"KEY_F11",
    pygame.K_F12:"KEY_F12" }
orig_map = {"KEY_LEFT_CTRL":128,
            "KEY_LEFT_SHIFT":129,
            "KEY_LEFT_ALT":130,
            "KEY_LEFT_GUI":131,
            "KEY_RIGHT_CTRL":132,
            "KEY_RIGHT_SHIFT":133,
            "KEY_RIGHT_ALT":134,
            "KEY_RIGHT_GUI":135,
            "KEY_UP_ARROW":218,
            "KEY_DOWN_ARROW":217,
            "KEY_LEFT_ARROW":216,
            "KEY_RIGHT_ARROW":215,
            "KEY_BACKSPACE":178,
            "KEY_TAB":179,
            "KEY_RETURN":176,
            "KEY_ESC":177,
            "KEY_INSERT":209,
            "KEY_DELETE":212,
            "KEY_PAGE_UP":211,
            "KEY_PAGE_DOWN":214,
            "KEY_HOME":210,
            "KEY_END":213,
            "KEY_CAPS_LOCK":193,
            "KEY_F1":194,
            "KEY_F2":195,
            "KEY_F3":196,
            "KEY_F4":197,
            "KEY_F5":198,
            "KEY_F6":199,
            "KEY_F7":200,
            "KEY_F8":201,
            "KEY_F9":202,
            "KEY_F10":203,
            "KEY_F11":204,
            "KEY_F12":205}

if __name__ == "__main__":
    from docopt import docopt
    args = docopt(__doc__)
    import sys, pygame
    from pprint import pprint
    from struct import pack
    import serial
    pygame.init()
    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0

    ser = serial.Serial('/dev/ttyUSB0', 9600)

    screen = pygame.display.set_mode(size)
    while True:
        for event in pygame.event.get():

            if event.type in (pygame.KEYUP ,pygame.KEYDOWN):
                if event.type == pygame.KEYUP:
                    press=False
                else:
                    press=True

                if event.key in py_map:
                    key=orig_map[py_map[event.key]]
                    print("{} mapped to {} ({})".format(event.key,
                        py_map[event.key],key))
                else:
                    key=event.key
                print("{} {}".format("pressed" if press else "released",key))
                ser.write(pack("!BB",1 if press else 0,key))
                #print(ser.readlines())
