import time
from datetime import datetime

from auto_search.auto_search import auto_search, chrome, safari
from game_bot_2048.bot import execute
from util.util import click

# Integrates previously implemented scripts so that we can automate multiple tasks with only 1 execution.
# Especially helpful for AFKing overnight.

# Set Safari browser icon position
icon = [290, 1065]
scheduled_hour = 4


def main():
    execute()
    click(425, 60, 2, 2)
    auto_search(7, 10, chrome)
    click(icon[0], icon[1], 3, 3)
    auto_search(3, 5, safari)


# The schedule library runs the program immediately when it is not supposed to,
# and solutions are not available. Furthermore, our needs differ slightly from
# simple periodic execution. Therefore, we write our own scheduler.
def get_hour():
    current_time = str(datetime.now().strftime("%H:%M:%S"))
    return int(current_time[0:2])


hour = get_hour()
while hour < scheduled_hour:
    time.sleep(60 * 60)
    hour = get_hour()
main()
