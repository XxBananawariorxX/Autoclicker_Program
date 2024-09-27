import pyautogui
import time
import keyboard

#program for autoclicker mouse
def click1():
    pyautogui.click(button = "left", interval = 1)

def main1():
    time.sleep(2)
    #number of clicks, just change While True to like for i in range(50) or something
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


#program for autoclicker keyboard
def click2():
    pyautogui.press("e", interval = 2.5)

def main2():
    time.sleep(1)
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

main2()



