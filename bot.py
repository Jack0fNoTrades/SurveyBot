import pyautogui
import time
import random

# put/change desired x, y ranges, factors here
desired_x_start_1 = 370
desired_y_start_1 = 430
x_factor_1 = 90
y_factor_1 = 30
desired_x_start_2 = 780
desired_y_start_2 = 1000
x_factor_2 = 100
y_factor_2 = 10


def execute():
    # sleep 10 seconds to allow enough time to switch to IDE or terminal and shut down the program
    time.sleep(10)
    click(desired_x_start_1, desired_y_start_1, x_factor_1, y_factor_1)
    random_sleep_time = random.random() + 0.3
    time.sleep(random_sleep_time)
    click(desired_x_start_2, desired_y_start_2, x_factor_2, y_factor_2)


def click(x, y, x_factor, y_factor):
    x_randomizer = random.randint(0, x_factor)
    y_randomizer = random.randint(0, y_factor)
    x += x_randomizer
    y += y_randomizer
    pyautogui.click(x, y)


def testing_ground():
    time.sleep(1)
    x, y = pyautogui.position()
    # use typewrite(msg) to input text, need to call click() in the right spot first
    # pyautogui.typewrite("test")
    print("x = " + str(x) + ", y = " + str(y))


execute()
# while True:
#     # do later
#     try:
#         # execute()
#         testing_ground()
#         time.sleep(1)
#     # keyboard library would've been better but doesn't work on macOS
#     except KeyboardInterrupt:
#         break
