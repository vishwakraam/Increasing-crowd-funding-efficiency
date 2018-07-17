'''
Author - Ayoola Ogunsola
Date - December 18, 2016

P4DS Final Project - Increasing Crowdfunding Efficiency - 1
Group 8: Ayoola Ogunsola, Sameer Vinayak, Malvika Tripathi, Edwin Mercado
'''

import datetime

class Campaign:
    ''' All campaigns '''
    campaignCount = 0

    def __init__(self, idnum, name, blurb, goal, state, country, deadline,
                 launched_at, staff_pick, backers_count, usd_pledged,
                 spotlight):
        self.idnum = idnum
        self.name = name
        self.blurb = blurb
        self.goal = float(goal)
        self.state = state
        self.country = country
        self.deadline = deadline
        self.launched_at = launched_at
        self.staff_pick = staff_pick
        self.backers_count = int(backers_count)
        self.usd_pledged = float(usd_pledged)
        self.spotlight = spotlight
        
        Campaign.campaignCount += 1


    def calcBlurbLength(self):
        ''' Get length of blurb '''
        return len(self.blurb)

    def calcNameLength(self):
        ''' Get length of campaign name '''
        return len(self.name)

    def getGoal(self):
        ''' Get goal '''
        return int(self.goal)

    def getState(self):
        ''' Get state '''
        return self.state

    def getIdNum(self):
        ''' Get Id '''
        return self.idnum

    def getDeadline(self):
        ''' Get deadline '''
        return self.deadline

    def getLaunchedAt(self):
        ''' Get launch date '''
        return self.launched_at

    def getUsdPledged(self):
        ''' Get US Dollars pledged '''
        return self.usd_pledged

    def calcCampaignLength(self):
        ''' Get length of campaign in hours'''
        days = self.deadline - self.launched_at
        hours = days.total_seconds() / 3600
        return hours

    def isStaffPick(self):
        ''' Was this a Staff Pick? '''
        if self.staff_pick == "TRUE":
            return True
        else:
            return False

    def isSpotlight(self):
        ''' Was this a Spotlight campaign? '''
        if self.spotlight == "TRUE":
            return True
        else:
            return False

    def percentFunded(self):
        ''' Percentage of the goal that has been raised, in USD '''
        amt = (self.usd_pledged / self.goal) * 100            
        return amt


class Successful(Campaign):
    ''' All campaigns with state = successful '''
    successCount = 0
    
    def __init__(self, idnum, name, blurb, goal, state, country, deadline,
                 launched_at, staff_pick, backers_count, usd_pledged, spotlight):
        Campaign.__init__(self, idnum, name, blurb, goal, state, country,
                          deadline, launched_at, staff_pick, backers_count,
                          usd_pledged, spotlight)

        Successful.successCount += 1

    def calcExcessFunds(self):
        ''' If fully funded, how much excess is available (USD)? '''
        if self.usd_pledged > self.goal:
            excess = self.usd_pledged - self.goal
            #excess = round(excess, 2)   # Round to 2 decimal places
        else:
            excess = 0
        return excess


class Live(Campaign):
    ''' All campaigns with state = live '''
    liveCount = 0

    def __init__(self, idnum, name, blurb, goal, state, country, deadline,
                 launched_at, staff_pick, backers_count, usd_pledged, spotlight):
        Campaign.__init__(self, idnum, name, blurb, goal, state, country,
                          deadline, launched_at, staff_pick, backers_count,
                          usd_pledged, spotlight)

        Live.liveCount += 1
        


class Unsuccessful(Campaign):
    ''' All campaigns with state = canceled, failed, suspended '''
    unsuccessCount = 0

    def __init__(self, idnum, name, blurb, goal, state, country,
                 deadline, launched_at, staff_pick, backers_count, usd_pledged,
                 spotlight):
        Campaign.__init__(self, idnum, name, blurb, goal, state,
                          country, deadline, launched_at, staff_pick,
                          backers_count, usd_pledged, spotlight)

        Unsuccessful.unsuccessCount += 1

    def calcDeficientFunds(self):
        ''' If not fully funded, how much remains to be raised (USD)? '''
        if self.usd_pledged > self.goal:
            deficient = 0
        else:
            deficient = self.goal - self.usd_pledged
            #deficient = round(deficient, 2)    # Round to 2 decimal places
        return deficient
            


    
    

    
    
