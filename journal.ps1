# PowerShell ConsoleJournal

# Variable Setup.
$WHATDID = "What did you accomplish just now"
$YOUDIDNT = "You didn't type anything."
$EXITING = "Exiting..."
$MDBULLET = "* "
$SPCHYPHEN = " - "

# Change this variable to the location of your journal file.
$JOURNAL_FILE = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"

# Open the file pointed to by the variable $JOURNAL_FILE into another variable
# called $OPEN_JOURNAL and then count the number of lines in the file
# into a variable called $LENGTH.
$OPEN_JOURNAL = Get-Content -Path $JOURNAL_FILE
$LENGTH = $OPEN_JOURNAL.count

# Set the variable $LINE to 1.
$LINE = 1

# Set the variable $ENTRIES_DISPLAY to the reversed version of the
# variable $OPEN_JOURNAL.
$ENTRIES_DISPLAY = 1..$LENGTH | ForEach-Object {$OPEN_JOURNAL[-$LINE]; $LINE++}

# Ask the user for input and store the input in a variable called $NEW_ENTRY.
Write-Host "$WHATDID" -ForegroundColor yellow
$NEW_ENTRY = Read-Host "?"

# If the user enters nothing, display a message and quit.
if ($NEW_ENTRY -eq "") {
    Write-Host $YOUDIDNT -ForegroundColor Red
    Write-Host $EXITING -ForegroundColor Green
    exit
}

# Get the date and time in 12 hour format and store it in a variable called
# $DATE_AND_TIME.
$DATE_AND_TIME = Get-Date -Format "yyyy/MM/dd - hh:mm:ss tt"

# Display the variable $ENTRIES_DISPLAY.
$ENTRIES_DISPLAY

# Add a new line to the variable $ENTRIES_DISPLAY using the new entry and some
# predefined formatting strings.
$ENTRIES_DISPLAY += "$MDBULLET$DATE_AND_TIME$SPCHYPHEN$NEW_ENTRY"

# Display to the console the date and time along with a markdown bullet
# and do this with the text colored red and without breaking a new line out.
Write-Host $MDBULLET$DATE_AND_TIME -NoNewline -ForegroundColor Red

# Display to the console a hyphen and the new entry in the color green
# along with a new line.
Write-Host $SPCHYPHEN$NEW_ENTRY -ForegroundColor Green

# Reverse the variable $ENTRIES_DISPLAY again for saving.
$LENGTH = $ENTRIES_DISPLAY.count
$LINE = 1
$ENTRIES_DISPLAY = 1..$LENGTH | ForEach-Object {$ENTRIES_DISPLAY[-$LINE]; $LINE++}

# Save the updated journal to the file pointed to by the variable $JOURNAL_FILE.
Set-Content -Path $JOURNAL_FILE -Value $ENTRIES_DISPLAY
