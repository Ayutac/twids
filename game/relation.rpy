###
# Contains the classes Battle, Date and Relation in this order, 
# but the first two need a Relation object as input parameter
###

init -75 python:
    
    class Battle(store.object):
        
        def __init__(self, rel):
            if not isinstance(rel, Relation):
                raise TypeError("rel is no Relation!")
            self.__rel = rel
            self.__rel.Battle = self
            self.al={}
            self.ata={}
            self.nowrite =[] #list of attacks that will not be written
            ##Pairings are attacker defender. and set them to the apropriate multiplier 
            #attacker -> defender
            #maybe in an extra file?
            self.al["br"]={}
            self.al["fe"]={}
            self.al["ob"]={}
            self.al["id"]={}
            ##brute
            #blindly attaks, no regard for strategy
            self.ata["br"]="atk"
            self.al["br"]["br"]=0.5 #brute -> brute
            self.al["br"]["fe"]=1 #brute -> feint
            self.al["br"]["ob"]=0 #brute -> observe
            self.al["br"]["id"]=1 #brute -> Idle 
            ##feint
            #orders a fake attack, and then an attack to discount
            self.ata["fe"]="int"
            self.al["fe"]["fe"]=0.5 # feint -> feint 
            self.al["fe"]["br"]=0 # feint -> brute
            self.al["fe"]["ob"]= 1 # feint -> observe
            self.al["fe"]["id"] = 1 # feint -> idle
            ##observe
            #trainer observes what the enemy does and reacts accordingly
            self.ata["ob"] = "int"
            self.al["ob"]["br"] = 1 # observe -> brute
            self.al["ob"]["fe"] = 0 # observe -> feint
            self.al["ob"]["ob"]= 0 # observe -> observe ##debatable... could self.also be 0.5 likeö 
            self.al["ob"]["id"] = 0 #observe -> idle
            ##idle
            #never does damage.
            #change any stat changing move after the use to idle
            self.ata["id"] = "atk"
            self.al["id"]["id"] = 0
            self.al["id"]["br"] = 0
            self.al["id"]["fe"] = 0
            self.al["id"]["ob"] = 0
            self.nowrite.append("id")
            self.dis1 = 0
            self.dis2 = 0
            self.foc1 = 0
            self.foc2 = 0
            self.lastAtk1 = "br"
            self.lastAtk2 = "br"
            self.power1 ={}
            self.power1["atk"] = (self.Rel.Char1.getStat(STAT_STRENGTH)
                + rel.Char1.getStat(STAT_SKILLS))/2
            self.power1["int"] = self.Rel.Char1.getStat(STAT_INTELLIGENCE)
            self.power2 ={}
            self.power2["atk"] = (self.Rel.Char2.getStat(STAT_STRENGTH)
                + rel.Char1.getStat(STAT_SKILLS))/2
            self.power2["int"] = self.Rel.Char2.getStat(STAT_INTELLIGENCE)
            
        def getRel(self):
            return self.__rel
        Rel = property(getRel)
            
        #++ here you can modify the battle system
        def turn(self, attack1, attack2):
            if not ((isinstance(attack1, str) or isinstance(attack1, unicode)) and
                (isinstance(attack2, str) or isinstance(attack2, unicode))):
                raise TypeError("attack must be a string!")
                
            d1=0
            d2=0
            
            ## BEGIN special effects
    
            ## distraction
            if attack1 == "dis": ##if distract
                self.dis2 += 1 ## set distract enemy +1
                attack1 = self.lastAtk1 ## and change the command to the actual last one
            if attack2 == "dis":
                self.dis1 += 1
                attack2 = self.lastAtk2
                
            ## focus
            if attack1 == "foc": ## if focus
                self.foc1+= 1 ## set focus player +1
                attack1 = self.lastAtk1 ## and change the command to the actual last one
            if attack2 == "foc":
                self.foc2+= 1
                attack2 = self.lastAtk2
            ## END special Effects
            
            d1=self.power1[self.ata[attack1]]
            d2=self.power2[self.ata[attack2]]
            d1 *= self.al[attack1][attack2]
            d2 *= self.al[attack2][attack1]
            
            ##BEGIN Attack modifiers
            ##distraction
            if self.dis1>0:
                self.dis1 -= 1
                if self.dis2>0:
                    d1 *=0.6 #both are distracted
                    d2 *=0.6
                    self.dis2 -= 1
                else:
                    d1 *=0.5
            elif self.dis2 > 0:
                d2 *= 0.5
                self.dis2 -= 1
                
            ##focus
            if self.foc1 >0:
                self.foc1 -= 1
                if self.foc2>0:
                    d1*=1.5 #both are focused
                    d2*=1.5
                    self.foc2 -= 1
                else:
                    d1 *= 2
            elif self.foc2>0:
                d2 *= 2
                self.foc2 -= 1
            ##END Attack Modifiers
            self.Rel.Char1.BattleHP -= (int)(d2)
            self.Rel.Char2.BattleHP -= (int)(d1)
            if attack1 not in self.nowrite :
                self.lastAtk1 = attack1
            if attack2 not in self.nowrite :
                self.lastAtk2 = attack2
            return self.end()
        
        ## the code of this method is written this way because
        ## after one turn the outcome is clear.
        def end(self):
            if self.Rel.Char1.BattleHP > 0 and self.Rel.Char2.BattleHP > 0:
                return "continue"
            if self.Rel.Char1.BattleHP > self.Rel.Char2.BattleHP:
                result = BATTLE_CHAR1_WON
                self.Rel.increaseBattlesWon()
                if self.Rel.Mirror != None:
                    self.Rel.Mirror.increaseBattlesLost()
            elif self.Rel.Char1.BattleHP < self.Rel.Char2.BattleHP:
                result = BATTLE_CHAR2_WON
                self.Rel.increaseBattlesLost()
                if self.Rel.Mirror != None:
                    self.Rel.Mirror.increaseBattlesWon()
            else:
                result = BATTLE_TIE
                self.Rel.increaseBattlesTie()
                if self.Rel.Mirror != None:
                    self.Rel.Mirror.increaseBattlesTie()
            self.Rel.Battle = None
            if self.Rel.Mirror != None:
                self.Rel.Mirror.Battle = None
            return result
            
            
    
    class Date(store.object): ## Date is reserved (?)
        
        ## location is currently not needed here, from now on it is a iDL
        def __init__(self, rel, c1I, c2I, location, days = 2, startMood = 0.5):
            if not isinstance(rel, Relation):
                raise TypeError("rel is no Relation!")
            if not (isinstance(c1I, int) and isinstance(c2I, int)):
                raise TypeError("The indices must be ints!")
            if not (isinstance(location, int) and isinstance(days, int)):
                raise TypeError("location and days must be ints!")
            if not isinstance(startMood, float):
                raise TypeError("startMood must be a float!")
            if startMood < 0.0 or startMood > 1.0:
                raise ValueError("startMood must be between 0.0 and 1.0 inclusive")
            self.__rel = rel
            self.__rel.Date = self
            self.__c = (c1I, c2I)
            self.__location = location
            self.__days = days
            self.__mood = startMood
            self.__cSpeak = 0
            self.__cAsk = 0
            self.__cGift = 0
            self.__cPhoto = 0
            self.__cKiss = 0
        
        ## getters and setters
        def getRel(self):
            return self.__rel
        Rel = property(getRel)
        def getLocation(self):
            return self.__location
        Location = property(getLocation)
        def getDays(self):
            return self.__days
        Days = property(getDays)
        def getMood(self):
            return self.__mood
        def setMood(self, mood):
            if not isinstance(mood, float):
                raise TypeError("mood must be float!")
            if mood < 0.0:
                self.__mood = 0.0
            elif mood > 1.0:
                self.__mood = 1.0
            else:
                self.__mood = mood
        Mood = property(getMood, setMood)
        def getCSpeak(self):
            return self.__cSpeak
        CSpeak = property(getCSpeak)
        def increaseCSpeak(self):
            self.__cSpeak += 1
        def getCAsk(self):
            return self.__cAsk
        CAsk = property(getCAsk)
        def increaseCAsk(self):
            self.__cAsk += 1
        def getCGift(self):
            return self.__cGift
        CGift = property(getCGift)
        def increaseCGift(self):
            self.__cGift += 1
        def getCPhoto(self):
            return self.__cPhoto
        CPhoto = property(getCPhoto)
        def increaseCPhoto(self):
            self.__cPhoto += 1
        def getCKiss(self):
            return self.__cKiss
        CKiss = property(getCKiss)
        def increaseCKiss(self):
            self.__cKiss += 1
            
        ## returns False if to much talking,
        ## else True
        def speak(self):
            self.increaseCSpeak()
            if self.CSpeak > 3:
                if self.CSpeak > 4:
                    self.Mood -= 0.03
                return False
            else:
                self.Mood += 0.03
                return True
                
        ## returns False if to much asking, else True
        def question(self):
            self.increaseCAsk()
            if self.CAsk > 4:
                if self.CAsk > 5:
                    self.Mood -= 0.03
                return False
            return True
        
        ## returns True for continuity
        def answer(self, answerLevel):
            if not isinstance(answerLevel, int):
                raise TypeError("answerLevel must be an int!")
            if answerLevel == 0:
                self.Mood -= 0.07
            elif answerLevel == 1:
                self.Mood -= 0.03
            elif answerLevel == 2:
                self.Mood += 0.02
            elif answerLevel == 3:
                self.Mood += 0.06
            return True
        
        ## returns False if overgifting,
        ## else True
        def presentGift(self):
            self.increaseCGift()
            if self.CGift > 2:
                if self.CGift > 3:
                    self.Mood -= 0.02
                return False
            return True
            
        ## returns False if gifting wasn't possible and 
        ## if everything was fine the reaction level to the gift.
        ## everything else has to be cleared with presentGift(...)
        def giveGift(self, item, reaction):
            #reaction = self.Rel.Char2.getGiftReaction(giftIndex)
            if item.give(self.__c[0], self.__c[1]) == False: ## turns over the item
                return False
            if reaction == 0:
                self.Mood -= 0.07
            elif reaction == 1:
                self.Mood += 0.07
            elif reaction == 2:
                self.Mood += 0.1
            elif reaction == 3:
                self.Mood += 0.13
            else:
                reaction = 0
            #inventory[giftIndex].add(-1) ## do not substract if not accepted
            return reaction
        
        ## returns False if over-photographing,
        ## -1 if not ready yet and True if everything is self.alright
        def photo(self):
            self.increaseCPhoto()
            if self.CPhoto > 1:
                if self.CPhoto > 2:
                    self.Mood -= 0.1
                    return False
            elif self.Mood < 0.7:
                self.Mood -= 0.05
                self.__cPhoto -= 1
                return -1
            else:
                self.Mood += 0.1
                return True
                
        ## returns True if kiss successful, else False 
        def kiss(self):
            self.increaseCKiss()
            if self.Mood > 1.0 - 0.05:
                self.Mood += 0.1
                self.increaseCKiss()
                return True
            self.Mood -= 0.1
            return False
        
        ## ends the date and skips the days
        #++ therefore, a nextDay() method is needed
        def finish(self):
            global day
            if self.CKiss > 0:
                resultVal = True
                self.Rel.goodDateDone()
                if self.Rel.Mirror != None:
                    self.Rel.Mirror.goodDateDone()
            else:
                resultVal = False
                self.Rel.badDateDone()
                if self.Rel.Mirror != None:
                    self.Rel.Mirror.badDateDone()
            if self.Rel.Milestone == MS_CLOSE_FRIEND:
                self.Rel.levelUp()
                if self.Rel.Mirror != None:
                    self.Rel.Mirror.levelUp()
            i = 0
            while i < self.Days - 2:
                nextDay(False)
                i = i + 1
            self.Rel.Char1.HP = 0
            self.Rel.Char2.HP = 0
            self.Rel.Date = None
            if self.Rel.Mirror != None:
                self.Rel.Mirror.Date = None
            nextDay(True)
            return resultVal
    
    ## if relation is changed to be a one-way, checkCorruption/BFF must be worked over
    #++ self.also, the methods of main interest are setMilestone, getMilestoneForExp,
    #++ checkCorruption and checkBFF
    class Relation(store.object):
    
        ## you can extend or change this list, but DO NOT change its current order
        ## (first positive milestones (up), then specials, then negative milestones (down))
        #++ here you can change/delete the special milestones, too
        #++ but please: if you REPLACE one special milestone, change the rest
        #++ of this code, too (whenever the milestone cause special things)
        __milestones = ["Stranger", "New Friend", "Good Friend", "Close Friend",
                        "Boyfriend", "Lover", "Boytoy", "Best Friend FOREVER",
                        "Shag Buddy", "Arch Enemy", "Enemy", "Creep", "Jerk", 
                        "Idiot"]
        
        def getNameOfMilestone(i):
            if i < -len(Relation.__milestones) or (
                i > len(Relation.__milestones) - 1):
                raise IndexError("Index is ridiculous!")
            return Relation.__milestones[i]
    
        getNameOfMilestone = staticmethod(getNameOfMilestone)
        
        ## dSGA is short for "days Since Gifting Allowed"
        ## dSOTA is short for "day Since OverTalking self.allowed"
        def __init__(self, char1, char2, mirror = None, exp = 0, milestone = 0,    
            dSGA = None, corruptionPoints = 0, corrupted = False, dSOTA = None,    
            bff = False, criminalPoints = 0, dates = 0, successfulDates = 0, 
            firstKiss = None, kissedToday = 0, phonedToday = 0, shaggedToday = 0,
            battlesWon = 0, battlesLost = 0, battlesTie = 0):
            store.object.__init__(self)
            ## error handling
            if not (isinstance(char1, DSC) and isinstance(char2, DSC)):
                raise TypeException("Characters must be of type DSC!")
            if not (isinstance(exp, int) and isinstance(milestone, int) and    
                isinstance(corruptionPoints, int) and    
                isinstance(criminalPoints, int) and 
                isinstance(dates, int) and isinstance(successfulDates, int) and
                isinstance(kissedToday, int) and isinstance(phonedToday, int) and
                isinstance(shaggedToday, int) and isinstance(battlesWon, int) and
                isinstance(battlesLost, int) and isinstance(battlesTie, int)):
                raise TypeError("exp, milestone, corruptionPoints, " +
                    "criminalPoints, dates, successfulDates, kissedToday, phonedToday, " +
                    "shaggedToday, battleWon, battlesLost and battlesTie must be ints!")
            if not (mirror == None or isinstance(mirror, Relation)):
                raise TypeError("mirror must be a Relation or None!")
            if not ((firstKiss == None or instance(firstKiss, int)) and (
                dSGA == None or isinstance(dSGA, int)) and (
                dSOTA == None or isinstance(dSOTA, int))):
                raise TypeError("firstKiss, dSGA and dSOTA must be ints or None!")
            Relation.getNameOfMilestone(milestone) ## throws exception
            if (dates < successfulDates):
                raise ValueError("One can't have more successful dates than dates!")
            if corruptionPoints < 0 or criminalPoints < 0 or dates < 0 or (
                successfulDates < 0 or phonedToday < 0 or battlesWon < 0) or (
                battlesLost < 0 or battlesTie < 0 or shaggedToday < 0):
                raise ValueError("corruptionPoints, criminalPoints, dates, " +
                    "successfulDates, phonedToday, shaggedToday, battlesWon, battlesLost " +
                    "and battlesTie must be non-negative!")
            #++ here we check if dSGA matches with the milestones
            if milestone > 1 and (dSGA == None or dSGA > day):
                raise ValueError("Gifting is possible, but dSGA doesn't match!")
            #++ same with corrupted
            if (milestone == MS_BOYTOY and not corrupted) or (milestone != MS_BOYTOY and corrupted):
                raise ValueError("milestone doesn't match corrupted!")
            #++ same with bff
            if (milestone == MS_BFF and not bff) or (milestone != MS_BFF and bff):
                raise ValueError("milestone doesn't match bff!")
            if milestone < -len(Relation.__milestones) or milestone >= len(Relation.__milestones):
                raise ValueError("Milestone is ridiculous!")
            ## now copy values
            self.__char1 = char1
            self.__char2 = char2
            if char1.Gender == "female":
                self.__milestones[MS_BOYFRIEND] = "Girlfriend"
            self.__mirror = mirror
            self.__exp = exp
            self.__milestone = milestone
            self.__dSGA = dSGA
            self.__corruptionPoints = corruptionPoints
            self.__corrupted = corrupted
            self.__criminalPoints = criminalPoints
            ## set the talkingDays array with "number of days" zeros
            self.__talkingDays = []
            for i in range(0,MAX_DAYS+1):
                self.__talkingDays += [0]
            self.__dSOTA = dSOTA
            self.__bff = bff
            self.__dates = dates ## like "number of dates"
            self.__date = None ## like "date attending now"
            self.__successfulDates = successfulDates
            self.__firstKiss = firstKiss
            self.__kissedToday = kissedToday
            ## please note the issue weither the two characters can have a phone chat
            ## is decided in the method "canBeCalled" below
            self.__phonedToday = phonedToday
            self.__shaggedToday = shaggedToday
            self.__battlesWon = battlesWon
            self.__battlesLost = battlesLost
            self.__battlesTie = battlesTie
            self.__battle = None ## like "battle attending now"
            self.__changed = False ## a flag to see if milestone changed
        
        ## the charmfactor to be multiplied with the base exp for actions
        #++ if you do not want such a thing, simple change the return value to 1
        def getCharmfactor(self):
            c1 = self.Char1.StatRef.getIndex("Charm")
            c2 = self.Char2.StatRef.getIndex("Charm")
            ## if at least one character doesn't have a charm stat, 
            ## no factor will be calculated
            if not (c1 != -1 and c2 != -1):
                return 1
            c1 = self.Char1.getStat(c1)
            c2 = self.Char2.getStat(c2)
            ## for now, only the charm of the "attacker" will be used for this
            if c1 < 10: ## c1 == 0 => no exp at self.all *trollface*
                return 0.1316*sqrt(c1)
            return 0.0125*c1 + 0.875
    
        ## getters, setters and friends
        
        def getChar1(self):
            return self.__char1
        Char1 = property(getChar1)
        def getChar2(self):
            return self.__char2
        Char2 = property(getChar2)
        def getMirror(self):
            return self.__mirror
        Mirror = property(getMirror)
            
        def getExp(self):
            return self.__exp
        def setExp(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            self.__exp = val
            ## let's see how this will be implemented later
            #if self.getMilestoneForExp() == 5 and self.__milestone == 3:
            #    self.setBFF(True)
        Exp = property(getExp, setExp)
        
        def raiseExp(self, val, useCharmFactor = False):
            if not isinstance(useCharmFactor, bool):
                raise TypeException("useCharmFactor must be True or False!")
            if useCharmFactor:
                self.Exp = self.Exp + int(math.floor(val*self.getCharmfactor()))
            else:
                self.Exp = self.Exp + int(math.floor(val));
        def swapExp(self):
            self.Exp = -self.Exp
    
        ## to set someone to Boytoy, please self.always use "setCorrupted",
        ## for BFF please self.always use "setBFF"
        def setMilestone(self, milestone):
            if not isinstance(milestone, int):
                raise TypeError("milestone must be an int!")
            if milestone < -len(Relation.__milestones) or milestone >= len(Relation.__milestones):
                raise ValueError("Milestone is ridiculous!")
            if self.__milestone != milestone:
                self.__changed = True ## change the changed-flag |D
            #++ here the flags for the 2 special milestones are changed
            #++ if you just want to remove them, do it above
            if milestone == 6:
                self.__corrupted = True
            else:
                self.__corrupted = False
            if milestone == 7:
                self.__bff = True
            else:
                self.__bff = False
            #++ end of special milestones
            #++ the following line decides the day since when gifting
            #++ when adding negative milestones or changing them in
            #++ any other way you may want to adjust this
            if milestone > 1 and self.__dSGA == None:
                self.__dSGA = day
            self.__milestone = milestone
            return
            
        def getMilestone(self):
            return self.__milestone
        Milestone = property(getMilestone, setMilestone)
        def getMilestoneName(self):
            return Relation.getNameOfMilestone(self.Milestone)
        MilestoneName = property(getMilestoneName)
    
        ## will return the highest milestone to archive with the current
        ## relationship points (Exp), without special milestones
        ## (and currently no negative ones, because they don't exist)
        ## Negative milestones are given with negative numbers
        def getMilestoneForExp(self):
            if self.__exp >= 2250: # lover = 1.5*boyfriend
                return MS_LOVER
            elif self.__exp >= 1500: ## boyfriend = 2*close friend
                return MS_BOYFRIEND
            elif self.__exp >= 750: ## close friend = 2.5*good friend
                return MS_CLOSE_FRIEND
            elif self.__exp >= 300: ## good friend = 3*new friend
                ## when changing this, self.also change hadSheToLessTalk()
                return MS_GOOD_FRIEND
            elif self.__exp >= 100: ## new friend 
                return MS_NEW_FRIEND
            ## negative ones
            elif self.__exp <= -2250: ## arch enemy
                return MS_ARCH_ENEMY
            elif self.__exp <= -1500: ## enemy
                return MS_ENEMY
            elif self.__exp <= -750: ## creep
                return MS_CREEP
            elif self.__exp <= -300: ## jerk
                return MS_JERK
            elif self.__exp <= -100: ## idiot
                return MS_IDIOT
            else: # stranger
                return MS_STRANGER
        
        ## levels a relationship up EXCEPT for special milestones.
        ## Returns False if not leveled, else True.
        ## Characters will not be leveled if they have a special milestone.
        ## (what a special milestone is has to specified here nonetheless)
        #++ This doesn't prevent you to set a dchar's milestone
        #++ to a specific one. It is just to make everything easier.
        ## (this self.also levels down to negative milestones)
        def levelUp(self):
            if self.Milestone in (MS_BOYTOY, MS_BFF, MS_SEX_FRIEND):
                return False
            bestMilestone = self.getMilestoneForExp()
            if bestMilestone == self.Milestone:
                return False
            ## will level up to everything until close friend
            ## this code self.allows milestone jumps (e.g. Stranger => Good Friend)
            if bestMilestone in range(MS_NEW_FRIEND, MS_CLOSE_FRIEND+1) and bestMilestone > self.Milestone:
                self.Milestone = bestMilestone
                return True
            ## will level up to boyfriend or lover
            ## this code self.allows milestone jumps (Close Friend => Lover)
            if bestMilestone in (MS_BOYFRIEND, MS_LOVER) and self.SuccessfulDates > 0:
                self.Milestone = bestMilestone
                return True
            ## will level down to everything until creep
            ## this code self.allows milestone jumps (e.g. Stranger => Jerk)
            if bestMilestone in range(MS_CREEP, MS_IDIOT+1) and bestMilestone < self.Milestone:
                self.Milestone = bestMilestone
                return True
            return False
                
            
        ##########
        ## what follows are the properties especially concerning gifting
        ##########
        
        
        def getDSGA(self):
            return self.__dSGA
        DSGA = property(getDSGA) 
        def takesGifts(self):
            return self.DSGA != None
        
        def getGiftProtection(self):
            if self.DSGA == None:
                return False
            else:
                return (self.DSGA - day) <= 2
        GiftProtection = property(getGiftProtection)
    
        def setCorruptionPoints(self, val):
            if not isinstance(val, int):
                raise TypeError("The new value must be an int!")
            if val < 0: ## corruption Points can't be less than 0
                self.__corruptionPoints = 0
            else:
                self.__corruptionPoints = val
            self.checkCorruption()
                
        def getCorruptionPoints(self):
            return self.__corruptionPoints
        CorruptionPoints = property(getCorruptionPoints, setCorruptionPoints)
        def increaseCorruptionPoints(self, val):
            self.CorruptionPoints = self.CorruptionPoints + val
        
        ## this is an unnecessary way to decrease the direct use of milestones
        def corrupt(self):
            self.Milestone = MS_BOYTOY
        
        def isCorrupted(self):
            return self.__corrupted
        Corrupted = property(isCorrupted)
        
        ## checks the corruption of the relationship (if too high or too low)
        def checkCorruption(self):
            if not (self.Milestone in (6, 7, 8) or self.GiftProtection):
                ## here comes the limit for the gifting
                ## if relation is changed to be a one-way, this method must be worked over
                if (self.Char1.checkGiftBounds(self.CorruptionPoints) == 1) or (
                    self.Char2.checkGiftBounds(self.CorruptionPoints) == 1): 
                    self.corrupt()
            ## there is nothing to happen if the limits are under a certain value, at least for now
                
            
        ##########
        ## what follows are the properties especially concerning criminal activities
        ##########
                
    
        def setCriminalPoints(self, val):
            if not isinstance(val, int):
                raise TypeError("The new value must be an int!")
            if val < 0: ## criminal Points can't be less than 0
                self.__criminalPoints = 0
            else:
                self.__criminalPoints = val
                
        def getCriminalPoints(self):
            return self.__criminalPoints
        CriminalPoints = property(getCriminalPoints, setCriminalPoints)
        def increaseCriminalPoints(self, val):
            self.CriminalPoints = self.CriminalPoints + val
        
            
        ##########
        ## what follows are the properties especially concerning talking
        ##########
        
        
        def getDSOTA(self):
            return self.__dSOTA
        DSOTA = property(getDSOTA) 
        
        def getTalkProtection(self):
            if self.DSOTA == None:
                return False
            else:
                return (self.DSOTA - day) <= 2
        TalkProtection = property(getTalkProtection)
    
        def getRecentTalk(self, longer = True):
            talk = 0
            tdr = 0
            if (self.Char1.TalkDayRange > self.Char2.TalkDayRange) == longer:
                tdr = self.Char1.TalkDayRange
            else:
                tdr = self.Char2.TalkDayRange
            for i in self.__talkingDays[day-tdr+1:day+1]:
                talk += i
            return talk
        RecentTalk = property(getRecentTalk)
        
        def increaseTodaysTalk(self):
            self.__talkingDays[day] += 1
            self.checkBFF() 
        
        ## this is an unnecessary way to decrease the direct use of milestones
        def befriend(self):
            self.Milestone = MS_BFF

        def isBFF(self):
            return self.__bff
        BFF = property(isBFF)
        
        def checkBFF(self):
            rt = self.RecentTalk
            if (self.Char1.checkTalkBounds(rt) == 1) or (
                self.Char2.checkTalkBounds(rt) == 1): 
                if self.Milestone in (MS_GOOD_FRIEND,MS_CLOSE_FRIEND) and not self.TalkProtection:
                    self.befriend()
                    
        def checkBreakupTalk(self):
            rt = self.RecentTalk
            if (self.Char1.checkTalkBounds(rt) == -1) or (
                self.Char2.checkTalkBounds(rt) == -1):
                if self.Milestone in (MS_BOYFRIEND, MS_LOVER):
                    self.Exp = 300
                    self.Milestone = 2
                    return True
            return False
        
            
        ##########
        ## coming now: going on dates
        ##########
        
        def isGoingOnDates(self):
            return self.__milestone in (3, 4, 5)
        def getDates(self):
            return self.__dates
        Dates = property(getDates)
        def getSuccessfulDates(self):
            return self.__successfulDates
        SuccessfulDates = property(getSuccessfulDates)
        
        def getFirstKiss(self):
            return self.__firstKiss
        FirstKiss = property(getFirstKiss)
        
        def canKiss(self):
            return self.Milestone in range(MS_BOYFRIEND, MS_BFF+1)
            
        def getKissedToday(self):
            return self.__kissedToday
        KissedToday = property(getKissedToday)
        def increaseKissedToday(self):
            self.__kissedToday += 1
        def resetKissedToday(self):
            self.__kissedToday = 0
        def enoughKissedToday(self):
            if self.Milestone == MS_BOYFRIEND:
                return self.KissedToday >= 3
            elif self.Milestone == MS_LOVER:
                return self.KissedToday >= 5
            elif self.Milestone in range(MS_BOYTOY, MS_BFF+1):
                return self.KissedToday >= 2
            return True
        
        def addDate(self, successful):
            if not isinstance(successful, bool):
                raise TypeError("successful must be a boolean!")
            self.__dates += 1
            if successful:
                self.__successfulDates += 1
                self.raiseExp(300)
            if self.__successfulDates > 0 and self.__firstKiss == None:
                self.__firstDate = day
    
        def goodDateDone(self):
            self.addDate(True)
        
        def badDateDone(self):
            self.addDate(False)
            
        def getDate(self):
            return self.__date
        def setDate(self, date):
            if not (date == None or isinstance(date, Date)):
                raise TypeError("date must be of type Date or None!")
            self.__date = date
        Date = property(getDate, setDate)
            
        
        ##########
        ## the last things are calling and battling
        ##########
        
        
        def canBePhoned(self):
            return self.Milestone > 1
        def getPhonedToday(self):
            return self.__phonedToday
        PhonedToday = property(getPhonedToday)
        def increasePhonedToday(self):
            self.__phonedToday += 1
        def resetPhonedToday(self):
            self.__phonedToday = 0
        
        def getBattlesWon(self):
            return self.__battlesWon
        BattlesWon = property(getBattlesWon)
        def increaseBattlesWon(self):
            self.__battlesWon += 1
        def getBattlesLost(self):
            return self.__battlesLost
        BattlesLost = property(getBattlesLost)
        def increaseBattlesLost(self):
            self.__battlesLost += 1
        def getBattlesTie(self):
            return self.__battlesTie
        BattlesTie = property(getBattlesTie)
        def increaseBattlesTie(self):
            self.__battlesTie += 1
        def getBattles(self):
            return self.__battlesWon + self.__battlesLost + self.__battlesTie
        Battles = property(getBattles)
            
        def getBattle(self):
            return self.__battle
        def setBattle(self, battle):
            if not (battle == None or isinstance(battle, Battle)):
                raise TypeError("battle must be of type Battle or None!")
            self.__battle = battle
        Battle = property(getBattle, setBattle)
        
        ## the flag will be removed after asking for it
        def hasChanged(self):
            if self.__changed:
                self.__changed = False
                return True
            else:
                return False
            
        
        ##########
        ## some additional functionality
        ##########
        
        def mirror(self):
            mirrorRel = Relation(self.Char2, self.Char1, self, self.Exp, 
                self.Milestone, self.DSGA, self.CorruptionPoints, 
                self.Corrupted, self.DSOTA, self.BFF, self.CriminalPoints, 
                self.Dates, self.SuccessfulDates, self.FirstKiss, self.PhonedToday,
                self.BattlesLost, self.BattlesWon, self.BattlesTie)
            ## note we actually mirrored chars and battles won/lost
            mirrorRel.__changed = self.__changed
            for i in range(0,MAX_DAYS+1):
                mirrorRel.__talkingDays[i] = self.__talkingDays[i]
            self.__mirror = mirrorRel
            return mirrorRel
