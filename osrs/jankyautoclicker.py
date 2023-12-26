import pyautogui
import random
import time

# simple autoclicker for grinding spades for starting capital
time.sleep(4)
while pyautogui.locateOnScreen("max_inventory.png", grayscale=True, confidence=0.95) is None:
    pyautogui.click()
    time.sleep(random.random() * 10)
