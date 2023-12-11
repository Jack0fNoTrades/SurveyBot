import random
import pyautogui
import time


def click(x, y, x_factor_upper, y_factor_upper, x_factor_lower=0, y_factor_lower=0):
    # The values of the first 4 parameters corresponds exactly to the attributes of a box object
    # The last 2 parameters are only used if we don't want to start at the top left corner
    x_randomizer = random.randint(x_factor_lower, x_factor_upper)
    y_randomizer = random.randint(y_factor_lower, y_factor_upper)
    x += x_randomizer
    y += y_randomizer
    # moveTo() avoids cursor teleporting and makes it more like human behavior.
    pyautogui.moveTo(x, y, duration=0.2)
    img = pyautogui.screenshot()
    # perform the click
    pyautogui.mouseDown(x, y)
    time.sleep(0.3)
    pyautogui.mouseUp(x, y)


# utility function for finding the returned coordinates of objects on screen
def print_position():
    while True:
        time.sleep(1)
        print(pyautogui.position())

