import pyautogui
print(pyautogui.size())
width, height = pyautogui.size()
print(width)
print(pyautogui.position())

#pyautogui.moveTo(10, 10)
pyautogui.moveTo(10, 10, duration=1.5)
pyautogui.moveRel(200, 0, duration=2)


# @ python terminal session, import pyautogui
# then pyautogui.displayMousePosition() and 
# as you move the mouse the coordinates will show
