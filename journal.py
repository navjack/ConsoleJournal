#!/usr/bin/env python3

# Datetime used for getting the date and time
import datetime

# Readline used to enhance the input function
import readline

import sys

# color codes
RED = "\033[31m"
# dark_red = "\033[31;1m"
GREEN = "\033[32m"
# dark_green = "\033[32;1m"
YELLOW = "\033[33m"
# DARK_YELLOW = "\033[33;1m"
# BLUE = "\033[34m"
# DARK_BLUE = "\033[34;1m"
# MAGENTA = "\033[35m"
# DARK_MAGENTA = "\033[35;1m"
# CYAN = "\033[36m"
# DARK_CYAN = "\033[36;1m"
# WHITE = "\033[37m"
# DARK_WHITE = "\033[37;1m"
# BLACK = "\033[30m"

# End color code
COLOR = "\033[0m"

# Variable setup
WHATDID = "What did you accomplish just now?\n"
YOUDIDNT = "You didn't type anything.\n"
EXITING = "Exiting..."
MDBULLET = "* "
SPCHYPHEN = " - "
NEWLINE = "\n"

# This is the variable you can change that points to your journal file
JOURNAL_FILE = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"

# Open the file pointed to by the "journal_file" variable into another variable
# called "open_journal" and then read each line into a list called "entries"
# and then reuse the "entries" list to build the "entries_display" list
# and then reverse the order of the list so that the most recent is at
# the bottom
with open(JOURNAL_FILE, mode='r', encoding='utf8') as OPEN_JOURNAL:
    ENTRIES = OPEN_JOURNAL.readlines()
    ENTRIES_DISPLAY = list((ENTRIES))
    ENTRIES_DISPLAY.reverse()

# Ask the user the entry and save it into a variable called "new_entry"
NEW_ENTRY = input(f"{YELLOW}{WHATDID}{COLOR}")

# If the user presses the enter key without typing anything, the program
# will exit
if NEW_ENTRY == "":
    print(f"{RED}{YOUDIDNT}{COLOR}")
    print(f"{GREEN}{EXITING}{COLOR}")
    sys.exit()

# Color the variable "new_entry" and save that to another variable called
# "color_new_entry"
COLOR_NEW_ENTRY = f"{GREEN}{NEW_ENTRY}{COLOR}"

# Get the date and time in 12 hour format and save it into a variable called
# "date_and_time"
DATE_AND_TIME = datetime.datetime.now().strftime("%Y/%m/%d - %I:%M:%S %p")

# Color the "date_and_time" variable and save it into another variable called
# "color_date_and_time"
COLOR_DATE_AND_TIME = f"{RED}{DATE_AND_TIME}{COLOR}"

# At the beginning of the "entries" list add a markdown bullet point and
# combine that with the "date_and_time" and a hyphen and the "new_entry"
# variable with a line break
ENTRIES.insert(0, f"{MDBULLET}{DATE_AND_TIME}{SPCHYPHEN}{NEW_ENTRY}{NEWLINE}")

# Print the "entries_display" list in reverse order to the screen
for lines in ENTRIES_DISPLAY:
    print(lines.rstrip())

# Print a markdown bullet point and then the "color_date_and_time" variable
# combined with a hyphen and the "color_new_entry" variable
print(f"{MDBULLET}{COLOR_DATE_AND_TIME}{SPCHYPHEN}{COLOR_NEW_ENTRY}")

# Save the updated "open_journal" variable to the file pointed to in the
# "journal_file" variable using the "entries" list
with open(JOURNAL_FILE, mode='w', encoding='utf8') as OPEN_JOURNAL:
    OPEN_JOURNAL.writelines(ENTRIES)
