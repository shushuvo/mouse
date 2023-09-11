import pyautogui
pyautogui.FAILSAFE = False
print(pyautogui.position())
pyautogui.moveRel(-100,-100, duration=5)
     
