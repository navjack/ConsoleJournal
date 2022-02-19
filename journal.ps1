# PowerShell ConsoleJournal
# Ask the user for input and store the input in a variable called $TODO_NEW_ENTRY.
function ToDo {
    # Variable Setup.
    $WHATDID = "What did you accomplish just now"
    $MDBULLET = "* "
    $SPCHYPHEN = " - "
    $YOUDIDNT = "You didn't type anything."
    $EXITING = "Exiting..."
    # Change this variable to the location of your journal file.
    $JOURNAL_FILE = "/Volumes/ext/journal-gitea/NavJack/To Do/Untracked To Do.md"
    # Open the file pointed to by the variable $JOURNAL_FILE into another variable
    # called $OPEN_JOURNAL and then count the number of lines in the file
    # into a variable called $LENGTH.
    $OPEN_JOURNAL = Get-Content -Path $JOURNAL_FILE
    $JOURNALLENGTH = $OPEN_JOURNAL.count
    # Set the variable $LINE to 1.
    $LINE = 1
    # Set the variable $JOURNAL_ENTRIES_DISPLAY to the reversed version of the
    # variable $OPEN_JOURNAL.
    $JOURNAL_ENTRIES_DISPLAY = 1..$JOURNALLENGTH | ForEach-Object {$OPEN_JOURNAL[-$LINE]; $LINE++}
    Write-Host "$WHATDID" -ForegroundColor Yellow
    $TODO_NEW_ENTRY = Read-Host "?"
    # If the user enters nothing, display a message and quit.
    if ($TODO_NEW_ENTRY -eq "") {
        Write-Host $YOUDIDNT -ForegroundColor Red
        Write-Host $EXITING -ForegroundColor Green
    exit
    }
    # Get the date and time in 12 hour format and store it in a variable called
    # $DATE_AND_TIME.
    $DATE_AND_TIME = Get-Date -Format "yyyy/MM/dd - hh:mm:ss tt"
    # Display the variable $JOURNAL_ENTRIES_DISPLAY.
    $JOURNAL_ENTRIES_DISPLAY
    # Add a new line to the variable $JOURNAL_ENTRIES_DISPLAY using the new entry and some
    # predefined formatting strings.
    $JOURNAL_ENTRIES_DISPLAY += "$MDBULLET$DATE_AND_TIME$SPCHYPHEN$TODO_NEW_ENTRY"
    # Display to the console the date and time along with a markdown bullet
    # and do this with the text colored red and without breaking a new line out.
    Write-Host $MDBULLET$DATE_AND_TIME -NoNewline -ForegroundColor Red
    # Display to the console a hyphen and the new entry in the color green
    # along with a new line.
    Write-Host $SPCHYPHEN$TODO_NEW_ENTRY -ForegroundColor Green
    # Reverse the variable $JOURNAL_ENTRIES_DISPLAY again for saving.
    $JOURNALLENGTH = $JOURNAL_ENTRIES_DISPLAY.count
    $LINE = 1
    $JOURNAL_ENTRIES_DISPLAY = 1..$JOURNALLENGTH | ForEach-Object {$JOURNAL_ENTRIES_DISPLAY[-$LINE]; $LINE++}
    # Save the updated journal to the file pointed to by the variable $JOURNAL_FILE.
    Set-Content -Path $JOURNAL_FILE -Value $JOURNAL_ENTRIES_DISPLAY
    exit
}
# Ask the user for input and store the input in a variable called $IDEA_NEW_ENTRY.
function Idea {
    # Variable Setup.
    $WHATIDEA = "What is your new idea?"
    $MDBULLET = "* "
    $SPCHYPHEN = " - "
    $YOUDIDNT = "You didn't type anything."
    $EXITING = "Exiting..."
    # Change this variable to the location of your journal file.
    $IDEA_FILE = "/Volumes/ext/journal-gitea/NavJack/To Do/Ideas.md"
    # Open the file pointed to by the variable $IDEA_FILE into another variable
    # called $OPEN_IDEA and then count the number of lines in the file
    # into a variable called $LENGTH.
    $OPEN_IDEA = Get-Content -Path $IDEA_FILE
    $IDEALENGTH = $OPEN_IDEA.count
    # Set the variable $LINE to 1.
    $LINE = 1
    # Set the variable $IDEA_ENTRIES_DISPLAY to the reversed version of the
    # variable $OPEN_IDEA.
    $IDEA_ENTRIES_DISPLAY = 1..$IDEALENGTH | ForEach-Object {$OPEN_IDEA[-$LINE]; $LINE++}
    Write-Host "$WHATIDEA" -ForegroundColor Yellow
    $IDEA_NEW_ENTRY = Read-Host "?"
    # If the user enters nothing, display a message and quit.
    if ($IDEA_NEW_ENTRY -eq "") {
        Write-Host $YOUDIDNT -ForegroundColor Red
        Write-Host $EXITING -ForegroundColor Green
    exit
    }
    # Get the date and time in 12 hour format and store it in a variable called
    # $DATE_AND_TIME.
    $DATE_AND_TIME = Get-Date -Format "yyyy/MM/dd - hh:mm:ss tt"
    # Display the variable $IDEA_ENTRIES_DISPLAY.
    $IDEA_ENTRIES_DISPLAY
    # Add a new line to the variable $IDEA_ENTRIES_DISPLAY using the new entry and some
    # predefined formatting strings.
    $IDEA_ENTRIES_DISPLAY += "$MDBULLET$DATE_AND_TIME$SPCHYPHEN$IDEA_NEW_ENTRY"
    # Display to the console the date and time along with a markdown bullet
    # and do this with the text colored red and without breaking a new line out.
    Write-Host $MDBULLET$DATE_AND_TIME -NoNewline -ForegroundColor Red
    # Display to the console a hyphen and the new entry in the color green
    # along with a new line.
    Write-Host $SPCHYPHEN$IDEA_NEW_ENTRY -ForegroundColor Green
    # Reverse the variable $IDEA_ENTRIES_DISPLAY again for saving.
    $IDEALENGTH = $IDEA_ENTRIES_DISPLAY.count
    $LINE = 1
    $IDEA_ENTRIES_DISPLAY = 1..$IDEALENGTH | ForEach-Object {$IDEA_ENTRIES_DISPLAY[-$LINE]; $LINE++}
    # Save the updated journal to the file pointed to by the variable $IDEA_FILE.
    Set-Content -Path $IDEA_FILE -Value $IDEA_ENTRIES_DISPLAY
    exit
}
# Variable Setup.
$ISTHIS = "Is this a completed task or is it an idea?"
$WHATDID = "What did you accomplish just now"
$YOUDIDNT = "You didn't type anything."
$EXITING = "Exiting..."
# Ask the user what kind of entry they want to make.
Write-Host "$ISTHIS" -ForegroundColor Yellow
$ENTRY_TYPE = Read-Host "?"
if ($ENTRY_TYPE -eq "t" -or $ENTRY_TYPE -eq "T") {ToDo}
elseif ($ENTRY_TYPE -eq "i" -or $ENTRY_TYPE -eq "I") {Idea}
else {Write-Host "$YOUDIDNT$EXITING"; Exit}
