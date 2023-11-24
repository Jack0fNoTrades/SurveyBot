import pyautogui
import time
import random
from util.util import click

chrome = [540, 500]
safari = [540, 465]


# Although there are numerous front end applications that does this, they are not able to detect
# events that are happening on screen, and some of them may not even have the option of randomized
# refresh intervals.
def auto_search(low, high, browser):
    while pyautogui.locateOnScreen("search_hit.png", grayscale=True, confidence=0.8) is None:
        pyautogui.keyDown("command")
        pyautogui.keyDown("r")
        time.sleep(0.2)
        pyautogui.keyUp("command")
        pyautogui.keyUp("r")
        # wait a bit between searches
        time.sleep(random.randint(low, high))
    click(browser[0], browser[1], 5, 5)


auto_search(5, 8, chrome)
