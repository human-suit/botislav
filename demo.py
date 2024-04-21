import pyautogui
import time
import os
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True
pyautogui.size()
pyautogui.position()
x, y = pyautogui.locateCenterOnScreen("D:\python\serts.png")
pyautogui.doubleClick(x,y, duration=1)
program_list = pyautogui.getAllTitles()
program = 'Battle.net'
for program in program_list:
    if 'Battle.net' in program_list:
        break
    time.sleep(0.5)
time.sleep(1)
x, y = pyautogui.locateCenterOnScreen("D:\python\play.png")
pyautogui.doubleClick(x,y, duration=1)
time.sleep(1)
program = 'Hearthstone'
for program in program_list:
    if 'Hearthstone' in program_list:
        break
    time.sleep(0.5)
time.sleep(3)
x, y = pyautogui.locateCenterOnScreen("D:\python\play_game.png")
pyautogui.doubleClick(x,y, duration=1)
time.sleep(1)
x, y = pyautogui.locateCenterOnScreen("D:\python\desdna.png")
pyautogui.doubleClick(x,y, duration=1)
x, y = pyautogui.locateCenterOnScreen("D:\python\clock.png")
pyautogui.doubleClick(x,y, duration=1)