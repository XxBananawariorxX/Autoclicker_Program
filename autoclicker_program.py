import pyautogui
import time
import keyboard

#program for autoclicker mouse
def click1():
    pyautogui.click(button = "left")

def main1():
    time.sleep(3)
    #number of clicks
    while True:
        if keyboard.is_pressed('b'):
            break
        else:
            click1()


#program for autoclicker keyboard
def click2():
    pyautogui.press("e")

def main():
    time.sleep(4)
    status = 0
    while True:
        if keyboard.is_pressed("s"):
            status = 1
        elif keyboard.is_pressed("p"):
            status = 0
        elif keyboard.is_pressed("b"):
            break
        elif status == 1:
            click2()
        else:
            pass






