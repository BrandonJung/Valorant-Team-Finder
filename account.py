from rank import *
class Account:
    def __init__(self, username, rank, accountUsername, password):
        self.username = username
        self.rank = rank
        self.accountUsername = accountUsername
        self.password = password

def makeAccount(username, tier, division, accountUsername, password):
    account = Account(username, makeRank(tier, division), accountUsername, password)
    return account