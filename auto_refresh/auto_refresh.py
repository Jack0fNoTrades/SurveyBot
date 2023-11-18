import pyautogui
import time
import random


# Although there are numerous front end applications that does this, they are not able to detect
# events that are happening on screen, and some of them may not even have the option of randomized
# refresh intervals.
def auto_refresh():
    while pyautogui.locateOnScreen("search_hit.png", grayscale=True, confidence=0.8) is None:
        pyautogui.keyDown("command")
        pyautogui.keyDown("r")
        time.sleep(0.2)
        pyautogui.keyUp("command")
        pyautogui.keyUp("r")
        # wait a bit between searches
        time.sleep(random.randint(180, 600))


auto_refresh()
