import time
from datetime import datetime

from auto_search.auto_search import auto_search, chrome, safari
from game_bot_2048.bot import execute
from util.util import click

# Integrates previously implemented scripts so that we can automate multiple tasks with only 1 execution.
# Especially helpful for AFKing overnight.

# Set Safari browser icon position
safari_icon = [290, 1065]
chrome_icon = [250, 1065]
scheduled_hour = 4


def main():
    execute()
    click(425, 60, 2, 2)
    time.sleep(0.2)
    auto_search(7, 10, chrome)
    time.sleep(0.25)
    click(safari_icon[0], safari_icon[1], 3, 3)
    time.sleep(0.2)
    auto_search(3, 5, safari)
    time.sleep(1)
    click(chrome_icon[0], chrome_icon[1], 3, 3)
    time.sleep(0.7)
    click(1230, 180, 5, 5)
    time.sleep(3)
    auto_search(3, 5, chrome)


# execute the series of automations on a hardcoded delay of 24 hours in the rare cases
# where we are away for between 24 and 48 hours
for _ in range(24):
    for _ in range(60):
        time.sleep(60)

main()
