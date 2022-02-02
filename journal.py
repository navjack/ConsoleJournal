import datetime
import os
import readline
import sys
import code

journal_file = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"

new_entry = input("What did you accomplish just now?\n")

date_and_time = datetime.datetime.now().strftime("%Y/%m/%d - %I:%M:%S %p")

with open(journal_file, "r") as open_journal:
    existing_entries = open_journal.readlines()

existing_entries.insert(0, "* " + date_and_time + " - " + new_entry + "\n")

with open(journal_file, "w") as open_journal:
    open_journal.writelines(existing_entries)

os.system("cls" if os.name == "nt" else "clear")

with open(journal_file, "r") as open_journal:
    entries = open_journal.readlines()
    entries.reverse()
    for entry in entries:
        print(entry.rstrip())
