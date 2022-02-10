# This is the variable you can change that points to your journal file
$JOURNAL_FILE = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"
$WHATDID = "What did you accomplish just now"
$YOUDIDNT = "You didn't type anything."
$EXITING = "Exiting..."
$MDBULLET = "* "
$SPCHYPHEN = " - "
$NEWLINE = "\n"
# Open the file pointed to by the "journal_file" variable into another variable
# called "open_journal" and then read each line into a list called "entries"
# and then reuse the "entries" list to build the "entries_display" list
# and then reverse the order of the list so that the most recent is at
# the bottom
$OPEN_JOURNAL = Get-Content -Path $JOURNAL_FILE
$ENTRIES = $OPEN_JOURNAL
$LENGTH = $OPEN_JOURNAL.count
$LINE = 1
$ENTRIES_DISPLAY = 1..$LENGTH | ForEach-Object {$OPEN_JOURNAL[-$LINE]; $LINE++}
# Ask the user the entry and save it into a variable called "new_entry"
Write-Host "$WHATDID" -ForegroundColor yellow
$NEW_ENTRY = Read-Host "?"
# If the user presses the enter key without typing anything, the program
# will exit
if ($NEW_ENTRY -eq "") {
    Write-Host $YOUDIDNT -ForegroundColor Red
    Write-Host $EXITING -ForegroundColor Green
    exit
}
# Color the variable "new_entry" and save that to another variable called
# "color_new_entry"
$COLOR_NEW_ENTRY = $NEW_ENTRY
# Get the date and time in 12 hour format and save it into a variable called
# "date_and_time"
$DATE_AND_TIME = Get-Date -Format "yyyy/MM/dd - hh:mm:ss tt"
# Color the "date_and_time" variable and save it into another variable called
# "color_date_and_time"
$COLOR_DATE_AND_TIME = $DATE_AND_TIME
# At the beginning of the "entries" list add a markdown bullet point and
# combine that with the "date_and_time" and a hyphen and the "new_entry"
# variable with a line break
#ENTRIES.insert $MDBULLET $DATE_AND_TIME $SPCHYPHEN $NEW_ENTRY $NEWLINE
$ENTRIES_DISPLAY
$ENTRIES_DISPLAY += "$MDBULLET$DATE_AND_TIME$SPCHYPHEN$NEW_ENTRY"
Write-Host $MDBULLET$DATE_AND_TIME -NoNewline -ForegroundColor Red
Write-Host $SPCHYPHEN$NEW_ENTRY -ForegroundColor Green
$LENGTH = $ENTRIES_DISPLAY.count
$LINE = 1
$ENTRIES_DISPLAY = 1..$LENGTH | ForEach-Object {$ENTRIES_DISPLAY[-$LINE]; $LINE++}
Set-Content -Path $JOURNAL_FILE -Value $ENTRIES_DISPLAY
