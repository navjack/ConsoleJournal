#!/usr/bin/env python3

# datetime used for getting the date and time
import datetime

# os used for clearing the console
import os

# readline used to enhance the input function
import readline

# import sys
# import code

# color codes
red = "\033[31m"
dark_red = "\033[31;1m"
green = "\033[32m"
dark_green = "\033[32;1m"
yellow = "\033[33m"
dark_yellow = "\033[33;1m"
blue = "\033[34m"
dark_blue = "\033[34;1m"
magenta = "\033[35m"
dark_magenta = "\033[35;1m"
cyan = "\033[36m"
dark_cyan = "\033[36;1m"
white = "\033[37m"
dark_white = "\033[37;1m"
black = "\033[30m"

# end color code
color = "\033[0m"

# this is the variable you can change that points to your journal file
journal_file = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"

# ask the user the entry and save it into a variable called "new_entry"
new_entry = input(yellow + "What did you accomplish just now?\n" + color)

# if the user presses the enter key without typing anything, the program will exit
if new_entry == "":
    print(red + "You didn't type anything.\n" + color)
    print(green + "Exiting..." + color)
    exit()

# color the variable "new_entry" and save that to another variable called "color_new_entry"
color_new_entry = green + new_entry + color

# get the date and time in 12 hour format and save it into a variable called "date_and_time"
date_and_time = datetime.datetime.now().strftime("%Y/%m/%d - %I:%M:%S %p")

# color the "date_and_time" variable and save it into another variable called "color_date_and_time"
color_date_and_time = red + date_and_time + color

# open the file pointed to by the "journal_file" variable into another variable called "open_journal" and then read each line into an array called "entries"
with open(journal_file, "r") as open_journal:
    entries = open_journal.readlines()

# at the beginning of the "entries" array add a markdown bullet point and combine that with the "date_and_time" and a hyphen and the "new_entry" variable with a line break
entries.insert(0, "* " + date_and_time + " - " + new_entry + "\n")

# clear the console
os.system("cls" if os.name == "nt" else "clear")

# read the file pointed to in the "journal_file" variable into another variable called "open_journal_display" and then read each line into an array called "entries_display" and then reverse the order of the array so that the most recent is at the bottom and then print each line as another variable called "lines" for each line
with open(journal_file, "r") as open_journal_display:
    entries_display = open_journal_display.readlines()
    entries_display.reverse()
    for lines in entries_display:
        print(lines.rstrip())

# print a markdown bullet point and then the "color_date_and_time" variable combined with a hyphen and the "color_new_entry" variable
print("* " + color_date_and_time + " - " + color_new_entry)

# save the updated "open_journal" variable to the file pointed to in the "journal_file" variable using the "entries" array
with open(journal_file, "w") as open_journal:
    open_journal.writelines(entries)
