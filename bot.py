import pyautogui
import time
import random
import string

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


def click(x, y, x_factor_upper, y_factor_upper, x_factor_lower=0, y_factor_lower=0):
    x_randomizer = random.randint(x_factor_lower, x_factor_upper)
    y_randomizer = random.randint(y_factor_lower, y_factor_upper)
    x += x_randomizer
    y += y_randomizer
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
    box = pyautogui.locateOnScreen('ans_box.png', minSearchTime=0, confidence=0.7)
    x = box[0]
    y = box[1]
    x_randomizer = box[2]
    y_randomizer = box[3]
    click(x, y, x_randomizer, y_randomizer)
    # sleep some more to simulate human behavior
    interval = random.randint(0, 2)
    time.sleep(interval)
    # write to text box
    pyautogui.write(ans)


def testing_ground():
    time.sleep(1)
    x, y = pyautogui.position()
    # use write(msg) to input text, need to call click() in the right spot first
    # pyautogui.write("test")
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
