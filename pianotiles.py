from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel(518, 500)[0] == 0:
        click(518, 500)
    if pyautogui.pixel(626, 500)[0] == 0:
        click(626, 500)
    if pyautogui.pixel(727, 500)[0] == 0:
        click(727, 500)
    if pyautogui.pixel(830, 500)[0] == 0:
        click(830, 500)