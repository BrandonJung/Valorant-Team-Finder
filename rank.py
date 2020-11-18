class Rank:
    def __init__(self, tier, division):
        self.tier = tier
        self.division = division
        self.teamRank = -123

def makeRank(tier, division):
    rank = Rank(tier, division)
    rank.teamRank = makeTeamRank(tier, division)
    return rank

def makeTeamRank(tier, division):
    if(tier == "Iron"):
        return int(division)
    elif(tier == "Bronze"):
        return int(division) + 3
    elif(tier == "Silver"):
        return int(division) + 6
    elif(tier == "Gold"):
        return int(division) + 9
    elif(tier == "Platinum"):
        return int(division) + 12
    elif(tier == "Diamond"):
        return int(division) + 15
    elif(tier == "Immortal"):
        return int(division) + 18
    elif(tier == "Radiant"):
        return 22
