import datetime
import os
import readline
import sys
import code

journal_file = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"

new_entry = input("What did you accomplish just now?\n")
color_new_entry = "\033[32m" + new_entry + "\033[0m"

date_and_time = datetime.datetime.now().strftime("%Y/%m/%d - %I:%M:%S %p")
color_date_and_time = "\033[31m" + date_and_time + "\033[0m"

with open(journal_file, "r") as open_journal:
    entries = open_journal.readlines()

entries.insert(0, "* " + date_and_time + " - " + new_entry + "\n")

with open(journal_file, "w") as open_journal:
    open_journal.writelines(entries)

os.system("cls" if os.name == "nt" else "clear")

with open(journal_file, "r") as open_journal:
    entries = open_journal.readlines()
    entries.reverse()
    for lines in entries:
        print(lines.rstrip())

print("* " + color_date_and_time + " - " + color_new_entry)
