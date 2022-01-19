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
    string userJournalEntry;
    string newJournalEntry;
    string newJournal;
    string journalArray[1290];
    vector < string > newJournalArray;
    ifstream journal;
    int i = 0;
    time_t t = time(0);
    ofstream newJournalFile;
    struct tm* now = localtime(&t);
    string workingDirectory;
private:

};

void askuserworkingdirectory();
void theJournal();

int main()
{
    SetupVars vars;
    askuserworkingdirectory();
    theJournal();
    return 0;
}

void askuserworkingdirectory()
{
    class SetupVars  ( SetupVars );
    cout << "What folder would you like to save the journal file to?" << endl;
    //string workingDirectory;
    getline(cin, SetupVars.workingDirectory);
    string journalFile = SetupVars.workingDirectory + "/journal.md";
    //ifstream journal;
    SetupVars.journal.open(journalFile);
    if (SetupVars.journal.is_open()) 
    {
        cout << "journal.md file already exists in this folder" << endl;
    }
    else 
    {
        //ofstream newJournalFile;
        SetupVars.newJournalFile.open(journalFile);
        SetupVars.newJournalFile << "";
        SetupVars.newJournalFile.close();
    }
}

void theJournal()
{
    class SetupVars  ( SetupVars );
    SetupVars.journal.open(SetupVars.journalFile);
    SetupVars.currentDate = to_string(SetupVars.now -> tm_year + 1900) + "/" + to_string(SetupVars.now -> tm_mon + 1) + "/" + to_string(SetupVars.now -> tm_mday);
    SetupVars.currentTime = to_string(SetupVars.now -> tm_hour) + ":" + to_string(SetupVars.now -> tm_min) + ":" + to_string(SetupVars.now -> tm_sec);
    cout << "What did you accomplish today?" << endl;
    getline(cin, SetupVars.userJournalEntry);
    SetupVars.newJournalEntry = "* # " + SetupVars.currentDate + " - " + SetupVars.currentTime + " - " + SetupVars.userJournalEntry;
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
}
