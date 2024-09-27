import pyautogui
import time
import keyboard

#program for autoclicker mouse
def click1():
    pyautogui.click(button = "left", interval = 1)

def mouse_clicker1():
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
            click1()
        else:
            pass

def mouse_clicker2():
    time.sleep(2)
    #number of clicks, just change While True to like for i in range(50) or something
    status = 0
    number_of_clicks = input("Number of clicks: ")
    for i in range(0, number_of_clicks):
        click1()


#program for autoclicker keyboard
def click2():
    pyautogui.press("e", interval = 2.5)

def keyboard_clicker():
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

#For User
user = input("What Autoclicker do you want to use (mouse1, mouse2, or keyboard): ").upper

if user == "MOUSE1":
    mouse_clicker1()
elif user == "MOUSE2":
    mouse_clicker2()
elif user == "KEYBOARD":
    keyboard_clicker()
else:
    print("""
Sorry, I dont understand your input. We only accept these 3 inputs:
mouse1 = mouse autoclicker 
mouse2 --> clicks the mouse 50 times
keyboard --> press the e button on the keyboard repeatedly
""")



