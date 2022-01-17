// this program will allow the user to save a daily journal entry from the terminal in markdown formatting and save it
// save the journal file "N:/journal/journal.md" to a variable called journalFile
// open and read each line of journalFile to an array called journalArray
// get the current date and save it to a variable called currentDate
// get the current time and save it to a variable called currentTime
// ask the user "What did you accomplish today?" and save it to a variable called userInput
// append "* # currentDate - currentTime" to the userInput and save it to a variable called newJournalEntry
// add newJournalEntry to the start of journalArray and save it to a variable called newJournal
// write newJournal to "N:/journal/journal.md"
// print "Journal entry saved"
// print newJournal

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <ctime>
#include <cstdlib>

using namespace std;

class SetupVars
{
public:
    string journalFile = "N:/journal/journal.md";
    string currentDate;
    string currentTime;
    string userInput;
    string newJournalEntry;
    string newJournal;
    string journalArray[1290];
    vector < string > newJournalArray;
    ifstream journal;
    int i = 0;
    time_t t = time(0);
    ofstream newJournalFile;
    struct tm* now = localtime(&t);
private:

};

int main() 
{
    class SetupVars  ( SetupVars );
    SetupVars.journal.open(SetupVars.journalFile);
    SetupVars.currentDate = to_string(SetupVars.now -> tm_year + 1900) + "/" + to_string(SetupVars.now -> tm_mon + 1) + "/" + to_string(SetupVars.now -> tm_mday);
    SetupVars.currentTime = to_string(SetupVars.now -> tm_hour) + ":" + to_string(SetupVars.now -> tm_min) + ":" + to_string(SetupVars.now -> tm_sec);
    cout << "What did you accomplish today?" << endl;
    getline(cin, SetupVars.userInput);
    SetupVars.newJournalEntry = "* # " + SetupVars.currentDate + " - " + SetupVars.currentTime + " - " + SetupVars.userInput;
    SetupVars.journalArray[SetupVars.i] = SetupVars.newJournalEntry;
    SetupVars.i++;
    while (getline(SetupVars.journal, SetupVars.journalArray[SetupVars.i])) 
    {
        SetupVars.newJournalArray.push_back(SetupVars.journalArray[SetupVars.i]);
        SetupVars.i++;
    }
    SetupVars.newJournalArray.insert(SetupVars.newJournalArray.begin(), SetupVars.newJournalEntry);
    for (int j = 0; j < SetupVars.newJournalArray.size(); j++) 
    {
        SetupVars.newJournal += SetupVars.newJournalArray[j] + "\n";
    }
    SetupVars.newJournalFile.open(SetupVars.journalFile);
    SetupVars.newJournalFile << SetupVars.newJournal;
    SetupVars.newJournalFile.close();
    cout << "Journal entry saved" << endl;
    cout << SetupVars.newJournal;
    cin.get();
    return 0;
}
