from account import *
from rank import *
from pathlib import Path
import pickle
import sys

# List of accounts :)
accounts = []
# Difference in divisions you can party with
partyDifference = 3

myFile = Path("accounts.pkl")
if (myFile.exists()):
    with open('accounts.pkl', 'rb') as f:
        accounts = pickle.load(f)

def startUp():
    choice = input("\nWhat do you want to do?" +
    "\n[0] Add Account" + 
    "\n[1] Delete Account" +
    "\n[2] Modify Account" +
    "\n[3] View Accounts" + 
    "\n[4] Find a Team" + 
    "\n[5] Exit" +
    "\n")
    mainMenu(choice)

def mainMenu(numberChoice):
    if (int(numberChoice) == 0):
        addAccount()
    elif (int(numberChoice) == 1):
        deleteAccount()
    elif (int(numberChoice) == 2):
        modifyAccount()
    elif (int(numberChoice) == 3):
        viewAccounts()
    elif (int(numberChoice) == 4):
        findTeam()
    elif (int(numberChoice) == 5):
        exit()
    else:
        print("Please enter a valid number\n")
        startUp()

def addAccount():
    accountUsername = "Not given"
    password = "Not given"
    username = input("\nEnter in game username\n")
    for acc in accounts:
        if(acc.username == username):
            print("Account already added")
            startUp()
    tier = enterTier(username)
    print(tier)
    division = enterDivision(tier)
    choice = input("\nDo you want to store account credentials" +
    "\n[0] Yes" +
    "\n[1] No\n")
    if (choice == "0"):
        accountUsername = enterAccountUsername(username)
        password = enterAccountPassword(username)
    choice = input("\nIs this correct? [0] Yes | [1] No\n" + 
    "\n" + username + " | " + tier + " " + division + "\n")
    if (choice =="0"):
        newAccount = makeAccount(username, tier, division, accountUsername, password)
        newAccount.rank.teamRank = makeTeamRank(tier, division)
        accounts.append(newAccount)
        accounts.sort(key= lambda x: x.rank.teamRank)
    else:
        addAccount()
    startUp()

def deleteAccount():
    index = -1
    username = ""
    tier = ""
    division = ""
    accountUsername = input("\nWhat's the username of the account?\n")
    for acc in accounts:
        if(acc.username == accountUsername):
            index = accounts.index(acc)
            username = acc.username
            tier = acc.rank.tier
            division = acc.rank.division
    if(index == -1):
        print("Account does not exist")
        startUp()
    confirmation = input("\nIs this the right account? [0] Yes [1] No" +
    "\n" + username + " | " + tier + " " + division + "\n")
    if(confirmation == "0"):
        del accounts[index]
    startUp()

def modifyAccount():
    index = -1
    username = input("\nWhat's the username of the account?\n")
    for acc in accounts:
        if(acc.username == username):
            index = accounts.index(acc)
    modify = input("\nWhat do you want to modify?" +
    "\n [0] Username" +
    "\n [1] Rank" + 
    "\n [2] Login ID" +
    "\n [3] Login Password\n")
    if(modify == "0"):
        modifyUsername(index)
    elif(modify == "1"):
        modifyRank(index)
    elif(modify == "2"):
        modifyID(index)
    elif(modify == "3"):
        modifyPassword(index)
    startUp()

def modifyUsername(index):
    account = accounts[index]
    print("\nThis is the current username: " + account.username)
    newUsername = input("\nWhat do you want to change it to?\n")
    account.username = newUsername
    print("Username has been changed to " + account.username + "!\n")
    startUp()

def modifyRank(index):
    account = accounts[index]
    tier = account.rank.tier
    division = account.rank.division
    print("\nThis is the current rank: " + tier + " " + division)
    newTier = enterTier(account.username)
    account.rank.tier = newTier
    if(newTier != "Radiant"):
        newDivision = enterDivision(newTier)
        account.rank.division = newDivision
        division = newDivision
    print("\nRank has been changed to " + newTier + " " + division + "\n")


def modifyID(index):
    account = accounts[index]
    accountID = account.accountUsername
    print("\nThis is the current ID: " + accountID)
    newID = enterAccountUsername(account.username)
    accountID = newID
    print("\nAccount ID has been changed to " + accountID + "\n")

def modifyPassword(index):
    account = accounts[index]
    accountPassword = account.password
    print("\nThis is the current Password: " + accountPassword)
    newPassword = enterAccountPassword(account.username)
    accountPassword = newPassword
    print("\nAccount password has been changed to " + accountPassword + "\n")

def viewAccounts():
    if (len(accounts) < 1):
        print("No accounts added")
        startUp()
    print("")
    for acc in accounts:
        username = acc.username
        tier = acc.rank.tier
        division = acc.rank.division
        print("Username: " + username + " | Rank: " + tier + " " + str(division))
    print("")
    startUp()

def exit():
    confirmation = input("\nAre you sure?" + 
    "\n[0] Yes" + 
    "\n[1] No\n")
    if(confirmation == "0"):
        with open('accounts.pkl', 'wb') as f:
            pickle.dump(accounts, f)
        sys.exit()
    else:
        startUp()

def enterTier(username):
    tier = input("\nWhat tier is " + username + "?" + 
    "\n[0] Iron" + 
    "\n[1] Bronze" + 
    "\n[2] Silver" +
    "\n[3] Gold" +
    "\n[4] Platinum" + 
    "\n[5] Diamond" +
    "\n[6] Immortal" +
    "\n[7] Radiant\n")
    if(tier == "0"):
        return "Iron"
    elif(tier == "1"):
        return "Bronze"
    elif(tier == "2"):
        return "Silver"
    elif(tier == "3"):
        return "Gold"
    elif(tier == "4"):
        return "Platinum"
    elif(tier == "5"):
        return "Diamond"
    elif(tier == "6"):
        return "Immortal"
    elif(tier == "7"):
        return "Radiant"
    else:
        enterTier(username)


def enterDivision(tier):
    if(tier != "Radiant"):
        return input("\n" + tier + " [1], [2], or [3]?\n")

def enterAccountUsername(username):
    accountUsername = input("\nWhat is the account ID for " + username + "\n")
    return accountUsername

def enterAccountPassword(username):
    accountPassword = input("\nWhat is the password for " + username + "\n")
    return accountPassword

def findTeam():
    rankOrAccount = input("\nFind team for [0] Account or a [1] Rank?\n")
    if(rankOrAccount == "0"):
        findTeamAccount()
    elif(rankOrAccount == "1"):
        findTeamRank()
    else:
        startUp()

def findTeamRank():
    teamRankTier = -123
    validAccounts = []
    outputTier = ""
    tier = input("\nWhat is the tier?" + 
    "\n[0] Iron" + 
    "\n[1] Bronze" + 
    "\n[2] Silver" +
    "\n[3] Gold" +
    "\n[4] Platinum" + 
    "\n[5] Diamond" +
    "\n[6] Immortal" +
    "\n[7] Radiant\n")
    if(tier == "0"):
        teamRankTier = "Iron"
        outputTier = "Iron"
    elif(tier == "1"):
        teamRankTier = "Bronze"
        outputTier = "Bronze"
    elif(tier == "2"):
        teamRankTier = "Silver"
        outputTier = "Silver"
    elif(tier == "3"):
        teamRankTier = "Gold"
        outputTier = "Gold"
    elif(tier == "4"):
        teamRankTier = "Platinum"
        outputTier = "Platinum"
    elif(tier == "5"):
        teamRankTier = "Diamond"
        outputTier = "Diamond"
    elif(tier == "6"):
        teamRankTier = "Immortal"
        outputTier = "Immortal"
    elif(tier == "7"):
        teamRankTier = "Radiant"
        outputTier = "Radiant"
    else:
        print("Re-enter tier")
        findTeamRank()
    division = input("\n" + teamRankTier + " [1], [2], or [3]?\n")
    teamRankTier = makeTeamRank(teamRankTier, division)
    for acc in accounts:
        if(abs(acc.rank.teamRank - teamRankTier) <= partyDifference):
            validAccounts.append(acc)
    # TODO SORT BY RANKING
    if(len(validAccounts) > 0):
        print("\nThese are the accounts that can play with " + outputTier + " " + division + ":\n")
        for validAcc in validAccounts:
            print(validAcc.username + " | " + validAcc.rank.tier + " " + validAcc.rank.division)
    else:
        print("\nNo accounts can play with " + outputTier + " " + division + " sadly")
    startUp()

def findTeamAccount():
    index = -1
    validAccounts = []
    accountUsername = input("\nWhat is the username of the account?")
    for acc in accounts:
        if(accountUsername == acc.username):
            index = accounts.index(acc)
    if(index == -1):
        print("Account does not exist")
        startUp()
    account = accounts[index]
    accountTeamRank = account.rank.teamRank
    for acc in accounts:
        if(abs(acc.rank.teamRank - accountTeamRank) <= partyDifference and acc.username != accountUsername):
            validAccounts.append(acc)
    #TODO SORT BY RANKING
    if(len(validAccounts) > 0):
        print("\nThese are the accounts that can play with " + accountUsername + ":\n")
        for validAcc in validAccounts:
            print(validAcc.username + " | " + validAcc.rank.tier + " " + validAcc.rank.division)
    else:
        print("\nNo accounts can play with " + accountUsername + " sadly")
    startUp()
    
startUp()