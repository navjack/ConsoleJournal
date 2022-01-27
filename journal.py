import datetime

# read each line of the file "journal.md" into a list of strings as a variable called "existing_entries"
with open("journal.md", "r") as EXISTING_JOURNAL_FILE:
    existing_entries = EXISTING_JOURNAL_FILE.readlines()

# ask the user "What did you accomplish just now?" and save the answer as a variable called "new_entry"
new_entry = input("What did you accomplish just now?\n")

# get the current date and time and save it as a variable called "date_and_time" (YEAR/MONTH/DAY - HOUR:MINUTE:SECOND AM/PM)
date_and_time = datetime.datetime.now().strftime("%Y/%m/%d - %I:%M:%S %p")

# append the new entry to the start of the list of existing entries
existing_entries.insert(0, "* " + date_and_time + " - " + new_entry + "\n")

# write the updated list of entries to the file "journal.md"
with open("journal.md", "w") as EXISTING_JOURNAL_FILE:
    EXISTING_JOURNAL_FILE.writelines(existing_entries)

# print "journal.md" to the screen
with open("journal.md", "r") as EXISTING_JOURNAL_FILE:
    print(EXISTING_JOURNAL_FILE.read())
