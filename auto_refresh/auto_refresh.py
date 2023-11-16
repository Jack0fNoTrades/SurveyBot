import pyautogui
import time
import random
from util.util import click

safari = [1183, 60]
chrome = [82, 97]


# automatically refresh the page for the specified browser
def auto_refresh(browser):
    while pyautogui.locateOnScreen("search_hit.png", grayscale=True, confidence=0.8) is None:
        click(browser[0], browser[1], 4, 4)
        # wait a bit between searches
        time.sleep(random.randint(600, 2600))


auto_refresh(safari)
