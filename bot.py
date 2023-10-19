import pyautogui
import time
import random
import string
import numpy as np
import pytesseract
import cv2

# put/change desired x, y ranges, factors here
desired_x_start_1 = 370
desired_y_start_1 = 430
x_factor_1 = 90
y_factor_1 = 30
desired_x_start_2 = 780
desired_y_start_2 = 1000
x_factor_2 = 100
y_factor_2 = 10
keywords = ["Ontario", "English", "I understand"]


def execute():
    # sleep 10 seconds to allow enough time to switch to IDE or terminal and shut down the program
    time.sleep(10)
    # This click and the one immediately after automates the main screen
    click(desired_x_start_1, desired_y_start_1, x_factor_1, y_factor_1)
    # A pause to simulate human reflexes.
    random_sleep_time = random.random() + 0.3
    time.sleep(random_sleep_time)
    click(desired_x_start_2, desired_y_start_2, x_factor_2, y_factor_2)
    # take screenshot of current screen
    img = pyautogui.screenshot()
    while pyautogui.locateOnScreen(img, minSearchTime=0, confidence=0.8) is not None:
        for keyword in keywords:
            if find_coordinates_text(keyword) is not None:
                x, y = find_coordinates_text(keyword)
                click(x, y, 5, 5)
            else:
                click_random_choice()
        pass


def click(x, y, x_factor_upper, y_factor_upper, x_factor_lower=0, y_factor_lower=0):
    # The values of the first 4 parameters corresponds exactly to the attributes of a box object
    # The last 2 parameters are only used if we don't want to start at the top left corner
    x_randomizer = random.randint(x_factor_lower, x_factor_upper)
    y_randomizer = random.randint(y_factor_lower, y_factor_upper)
    x += x_randomizer
    y += y_randomizer
    # moveTo() avoids cursor teleporting and makes it more like human behavior.
    pyautogui.moveTo(x, y, duration=0.1)
    print(x, y)
    pyautogui.click(x, y)


def write_answer():
    # sleep a certain amount of time to simulate human behavior
    interval = random.randint(0, 3)
    time.sleep(interval)
    # generate the response
    ans = ""
    word_randomizer = random.randint(0, 5)
    word_count = 10 + word_randomizer
    for i in range(word_count):
        word_len = random.randint(3, 15)
        for j in range(word_len):
            ans += random.choice(string.ascii_letters)
        ans += " "
    if len(ans) < 50:
        ans += " very good. Therefore I chose this response."
    # locate text box
    box = list(pyautogui.locateOnScreen("ans_box.png", minSearchTime=0.0, grayscale=True, confidence=0.7))
    # The first two parameters of box is the coordinates of the top left corner
    # the 3rd parameter is the width, the 4th parameter is the height.
    # These parameters have the exact values needed for click().
    # [385, 1160, 1222, 174]
    # it's actually 408 575 ish
    # pyautogui locate functions always return incorrect coordinates, so workarounds are required.
    click((box[0]+box[2])/2-50, box[1]/2, 50, box[3]/2)
    # sleep some more to simulate human behavior
    interval = random.randint(0, 2)
    time.sleep(interval)
    # write to text box
    pyautogui.write(ans)


def find_coordinates_text(text, lang='en'):
    # Take a screenshot of the main screen
    screen = pyautogui.screenshot()

    # Convert the screenshot to grayscale
    img = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2GRAY)

    # Find the provided text (text) on the grayscale screenshot
    # using the provided language (lang)
    data = pytesseract.image_to_data(img, lang=lang, output_type='data.frame')

    # Find the coordinates of the provided text (text)
    try:
        x, y = data[data['text'] ==
                    text]['left'].iloc[0], data[data['text'] == text]['top'].iloc[0]

    except IndexError:
        # The text was not found on the screen
        return None

    # Text was found, return the coordinates
    return x, y


def click_random_choice():
    match_list = list(pyautogui.locateAllOnScreen("choice.png", confidence=0.75))
    choice = random.randint(0, len(match_list) - 1)
    location = match_list[choice]
    click(location[0], location[1], location[2], location[3])


# execute()
# while True:
#     time.sleep(1)
#     print(pyautogui.position())
# 996, 1247
# 720 /2
# 1709, 1106
# 408, 1030
# print(pyautogui.locateCenterOnScreen("ans_box.png", minSearchTime=0.0, grayscale=True, confidence=0.7))
time.sleep(2)
write_answer()

# "main executable" of the bot
# while True:
#     try:
#         # execute()
#         time.sleep(1)
#     # keyboard library would've been better but doesn't work on macOS
#     except KeyboardInterrupt:
#         break
