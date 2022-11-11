# DESCRIPTION
    # THIS PROGRAM TAKES A SCREENSHOT EVERY SECOND CLICK, AMONG OTHER
    # FUNCTIONS, MADE TO BE USED FOR THE MY SINGING MONSTERS MEMORY
    # GAME
# CREDITS
    # JOHAN - EVERYTHING

import pyautogui
import os
import win32api
import time
import win32con
import subprocess
import psutil

#CREATES SCREENSHOTS FOLDER IF IT DOESN'T EXIST ALREADY
if os.path.exists(os.getcwd() + '\\Screenshots\\') == False:
    os.mkdir(os.getcwd() + '\\Screenshots\\')

# DELETE IMAGES ON START
exec(open('delete.py').read())

# MISC VARIABLES
screenshotNumber = 1
state_RSHIFT = win32api.GetKeyState(win32con.VK_RSHIFT)
state_LSHIFT = win32api.GetKeyState(win32con.VK_LSHIFT)
state_LCTRL = win32api.GetKeyState(win32con.VK_LCONTROL)
running = True
state_RCTRL = win32api.GetKeyState(win32con.VK_RCONTROL)

# CLICKING FUNCITON VARIABLES & FUNCTIONS
clickTimes = 0
state_left = win32api.GetKeyState(0x01)
canClick = True

# SET WINDOW SIZE
cmd = 'mode 115,16'
os.system(cmd)

# INSTRUCTIONS
print('WELCOME TO MY MEMORY GAME CHEATING PROGRAM\n\n\nThis program works based on clicks, so if you click on one memory card, and then a second memory card,\nit will take a screenshot.\n\nPress CTRL to exit\n\nPress LSHIFT to fix the order, so if you accidentally click too fast and you only get one card in your screenshot\nthen you can just press LSHIFT to delete the most recent screenshot and reset your invisible clicks counter to 0\n\nPress RSHIFT to signify that you''ve moved on to the next level, resetting all variables.\n\nPress RCTRL to stop being able to take screenshots with your mouse clicks.')
print('')

# INPUT FUNCTIONS
while running:
    # CLICKING/SCREENSHOTTING
    currentLMBState = win32api.GetKeyState(0x01)
    if currentLMBState != state_left:
        state_left = currentLMBState
            
        if currentLMBState < 0:
                pass
        else:
            if canClick:
                clickTimes += 1
                if clickTimes == 2:
                    time.sleep(.5)
                    myScreenshot = pyautogui.screenshot()
                    myScreenshot.save(os.getcwd() + r'\Screenshots\screenshot_' + str(screenshotNumber) + r'.png')
                    screenshotNumber += 1
                else:
                    if clickTimes > 2:
                        clickTimes = 1
            else:
                pass
    
    # NEW LEVEL/RESETTING
    currentRSHIFTState = win32api.GetKeyState(win32con.VK_RSHIFT)
    if currentRSHIFTState != state_RSHIFT:
        state_RSHIFT = currentRSHIFTState
        if currentRSHIFTState < 0:
            pass
        else:
            exec(open('delete.py').read())
            clickTimes = 0
            canClick = True
            screenshotNumber = 1
            if "microsoft.photos.exe" in (i.name() for i in psutil.process_iter()):
                subprocess.call("TASKKILL /F /IM microsoft.photos.exe", shell=True)
    
    # FIXING ORDER
    currentLSHIFTState = win32api.GetKeyState(win32con.VK_LSHIFT)
    if currentLSHIFTState != state_LSHIFT:
        state_LSHIFT = currentLSHIFTState
        if currentLSHIFTState < 0:
            pass
        else:
            screenshotNumber-=1
            os.remove(os.getcwd() + r'\Screenshots\screenshot_' + str(screenshotNumber) + r'.png')
            clickTimes = 0
            canClick = True
    
    # EXITING THE PROGRAM
    currentLCTRLState = win32api.GetKeyState(win32con.VK_LCONTROL)
    if currentLCTRLState != state_LCTRL:
        state_LCTRL = currentLCTRLState
        if currentLCTRLState < 0:
            pass
        else:
            running = False
            if "microsoft.photos.exe" in (i.name() for i in psutil.process_iter()):
                subprocess.call("TASKKILL /F /IM microsoft.photos.exe", shell=True)
            pass
    
    # SCREENSHOT ABILITY CONTROL
    currentRCTRLState = win32api.GetKeyState(win32con.VK_RCONTROL)
    if currentRCTRLState != state_RCTRL:
        state_RCTRL = currentRCTRLState
        if currentRCTRLState < 0:
            pass
        else:
            if canClick == True:
                canClick = False
            else:
                canClick = True
    print('\rCan you take a screenshot with your clicks?',canClick, end=" ")
