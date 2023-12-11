import pyautogui
import time
import random
from util.util import click

# coordinates are hideout, chrome maximized window without full screen
try:
    while True:
        if pyautogui.locateOnScreen("video_interrupted_1.png", grayscale=True, confidence=0.8) is not None:
            click(610, 470, 10, 10)
            # Wait for pages to load to avoid pyautogui detecting the same interruption twice
            time.sleep(random.randint(2, 5))
        if pyautogui.locateOnScreen("video_interrupted_2.png", grayscale=True, confidence=0.8) is not None:
            click(725, 540, 5, 5)
            time.sleep(random.randint(3, 5))
            click(828, 643, 5, 5)
            # Wait for pages to load to avoid pyautogui detecting the same interruption twice
            time.sleep(random.randint(5, 10))
except KeyboardInterrupt:
    pass
