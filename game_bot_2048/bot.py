import time
import pyautogui
import random
from util.util import click

movement_list = ["left", "right", "up", "down"]
desired_x_start_1 = 740
desired_y_start_1 = 760
# desired_x_end_1 = 790
# desired_y_end_1 = 820
x_factor_1 = 50
y_factor_1 = 30
desired_x_start_2 = 690
desired_y_start_2 = 665
# desired_x_end_2 = 770
# desired_y_end_2 = 675
x_factor_2 = 80
y_factor_2 = 10


def play2048():
    # start game
    click(desired_x_start_1, desired_y_start_1, x_factor_1, y_factor_1)
    # select and press arrow keys at random until the game shows the game over page
    while pyautogui.locateOnScreen("game_over.png", grayscale=True, confidence=0.8) is None:
        choice = random.randint(0, 3)
        pyautogui.press(movement_list[choice])


# sleep for 3 seconds to allow time to manually bring game window in focus
def execute():
    time.sleep(3)
    counter = 0
    # we only need 3 successful games per run
    while counter < 3:
        play2048()
        # detect if the most recent game is successful
        if pyautogui.locateOnScreen("2SB.png", confidence=0.8) is not None:
            counter += 1
        # reload game
        click(desired_x_start_2, desired_y_start_2, x_factor_2, y_factor_2)
        # sleep some time to wait for the game to reload
        sleep_time = random.randint(5, 7)
        time.sleep(sleep_time)


# execute()


