# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 10:46:51 2023

@author: mpurvis
"""
import pyautogui as pag
import keyboard  # using module keyboard
interrupt = False
while interrupt == False:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        for i in range(1000):
            pag.moveTo(1, 1, duration = 1.0)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                interrupt = True
                break 
            pag.moveTo(1, 1000, duration = 1.0)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                interrupt = True
                break 
            pag.click(clicks = 2) 
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                interrupt = True
                break 
            # The above should trigger the Start button, introduced as in some
            # setting the computer still sleeps with only the move of the mouse
            pag.moveTo(1900, 1000, duration = 1.0)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                interrupt = True
                break 
            pag.moveTo(1900, 1, duration = 1.0)
            if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                print('You Pressed A Key!')
                interrupt = True
                break 
    except:
        break