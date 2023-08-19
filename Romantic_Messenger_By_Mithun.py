import pyautogui
import time
message = 100
# while true:
while message > 0:
    time.sleep(0)
    pyautogui.typewrite('I love you right up to the moon and back my lifeeee.')
    time.sleep(0)
    pyautogui.press('enter')
    message = message - 1
