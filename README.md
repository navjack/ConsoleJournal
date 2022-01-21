# ConsoleJournal

## What?

First of all, I dont know how to program.

Second of all, this was written mainly by me wrangling around GitHub CoPilot to do my bidding.

My goal with this is to make a simple console based "Journal". I'm unsure of the scope I want from it but simplicity is key. I imagine just pulling up a console window and being like ``journal today i did blah blah blah`` and it saves it into a file with the date and time and simple markdown bullet point formatting. So far it does exactly this.

To describe it another way

> org mode or orgzly or obsidian or anything like that is too formal for what i want. i want a dumb as shit thing almost to the point of "this could just be you opening notepad, why aren't you just doing this manually in notepad?"

The journal.md file in this repo is an example of what it outputs.

If you want to add this as an alias you can do similar to what I'm doing. ``alias journal="(cd /Volumes/ext/journal; python3 "/Volumes/ext/journal/journal.py")"``. to explain this it just makes it so when you type ``journal`` in the terminal it will go to the directory that the python script lives in and then it will run the python script, but it does all of this in a subshell which allows it to return to the previous place as if you never changed directory at all. Otherwise, the script would use your current directory as the working directory and it will make a ``journal.md`` file where ever you are.

## Did

* It's python now instead of C++
