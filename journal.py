#!/usr/bin/env python3

# Datetime used for getting the date and time
import datetime

# Os used for clearing the console
import os

# Readline used to enhance the input function
import readline

# import sys
# import code

# color codes
red = "\033[31m"
# dark_red = "\033[31;1m"
green = "\033[32m"
# dark_green = "\033[32;1m"
yellow = "\033[33m"
# dark_yellow = "\033[33;1m"
# blue = "\033[34m"
# dark_blue = "\033[34;1m"
# magenta = "\033[35m"
# dark_magenta = "\033[35;1m"
# cyan = "\033[36m"
# dark_cyan = "\033[36;1m"
# white = "\033[37m"
# dark_white = "\033[37;1m"
# black = "\033[30m"

# End color code
color = "\033[0m"

# Variable setup
whatdid = "What did you accomplish just now?\n"
youdidnt = "You didn't type anything.\n"
exiting = "Exiting..."
mdbullet = "* "
spchyphen = " - "
newline = "\n"

# This is the variable you can change that points to your journal file
journal_file = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"

# Open the file pointed to by the "journal_file" variable into another variable
# called "open_journal" and then read each line into a list called "entries"
# and then reuse the "entries" list to build the "entries_display" list
# and then reverse the order of the list so that the most recent is at
# the bottom
with open(journal_file, "r") as open_journal:
    entries = open_journal.readlines()
    entries_display = list((entries))
    entries_display.reverse()

# Ask the user the entry and save it into a variable called "new_entry"
new_entry = input(f"{yellow}{whatdid}{color}")

# If the user presses the enter key without typing anything, the program
# will exit
if new_entry == "":
    print(f"{red}{youdidnt}{color}")
    print(f"{green}{exiting}{color}")
    exit()

# Color the variable "new_entry" and save that to another variable called
# "color_new_entry"
color_new_entry = f"{green}{new_entry}{color}"

# Get the date and time in 12 hour format and save it into a variable called
# "date_and_time"
date_and_time = datetime.datetime.now().strftime("%Y/%m/%d - %I:%M:%S %p")

# Color the "date_and_time" variable and save it into another variable called
# "color_date_and_time"
color_date_and_time = f"{red}{date_and_time}{color}"

# At the beginning of the "entries" list add a markdown bullet point and
# combine that with the "date_and_time" and a hyphen and the "new_entry"
# variable with a line break
entries.insert(0,f"{mdbullet}{date_and_time}{spchyphen}{new_entry}{newline}")

# Clear the console
os.system("cls" if os.name == "nt" else "clear")

# Print the "entries_display" list in reverse order to the screen
for lines in entries_display:
    print(lines.rstrip())

# Print a markdown bullet point and then the "color_date_and_time" variable
# combined with a hyphen and the "color_new_entry" variable
print(f"{mdbullet}{color_date_and_time}{spchyphen}{color_new_entry}")

# Save the updated "open_journal" variable to the file pointed to in the
# "journal_file" variable using the "entries" array
with open(journal_file, "w") as open_journal:
    open_journal.writelines(entries)
