import pyautogui
import time
time.sleep(5)
x,y = pyautogui.position()
print(x,y)
r,g,b = pyautogui.pixel(x,y)
print(r,g,b)