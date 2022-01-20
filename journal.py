import datetime, sys, getopt

# read each line of the file "journal.md" into a list of strings as a variable called "existing_entries"
with open("journal.md", "r") as file:
    existing_entries = file.readlines()

# ask the user "What did you accomplish just now?" and save the answer as a variable called "new_entry"
new_entry = input("What did you accomplish just now?\n")

# get the current date and save it as a variable called "date_date" (YEAR/MONTH/DAY)
date_date = datetime.datetime.now().strftime("%Y/%m/%d")

# get the current time in 12-hour format (Hr:Min:Sec AM/PM) and save it as a variable called "time_time"
time_time = datetime.datetime.now().strftime("%I:%M:%S %p")

# append the new entry to the start of the list of existing entries
existing_entries.insert(0, "* # " + date_date + " - " + time_time + " - " + new_entry + "\n")

# write the updated list of entries to the file "journal.md"
with open("journal.md", "w") as file:
    file.writelines(existing_entries)

# print "journal.md" to the screen
with open("journal.md", "r") as file:
    print(file.read())
