###
# Makes use of day and global day
###

init -50 python:
    
    ## c1I and c2I, which are often used in this class's method arguments, 
    ## are short for "character 1/2 index" respectively
    class Interaction(store.object):
        
        ## rels is short for relations
        def __init__(self, chars, rels = None):
            store.object.__init__(self)
            ## error handling
            if not (False or True or False): ## TODO I clearly have to change this(?)
                raise TypeError("The chars must be a tuple or list of strings!")
            for i in range(0, len(chars)):
                if not isinstance(chars[i], DSC):
                    raise TypeError("Every entry of chars must be of type DSC!")
            if rels != None:
                if not (isinstance(rels, tuple) or isinstance(rels, list) or
                    isinstance(rels, renpy.python.RevertableList)):
                    raise TypeError("The rels must be a 2-dimensional tuple or list of strings!")
                if len(rels) != len(chars):
                    raise ValueError("The length of rels doesn't match with the length of chars!")
                for i in range(0, len(rels)):
                    if not (isinstance(rels[i], tuple) or isinstance(rels[i], list) or
                        isinstance(rels[i], renpy.python.RevertableList)):
                        raise TypeError("The rels must be a 2-dimensional tuple or list of strings!")
                    if len(rels[i]) != len(chars):
                        raise ValueError("An array of rels doesn't match with the length of char!")
                    for j in range(0, len(rels)):
                        if i != j:
                            if not isinstance(rels[i][j], Relation):
                                raise TypeError("Every entry of rels must be of type Relation!")
                            ## the following condition is vital to the structure of Interaction
                            ## and important for Relation, too
                            if not rels[i][j] == rels[j][i]:
                                raise ValueError("Rels is no symmetric matrix!")
                            if not (rels[i][j].Char1 == chars[i] and rels[i][j].Char2 == chars[j]):
                                raise ValueError("rels doesn't match with chars!")
                        elif not rels[i][i] == None:
                            raise ValueError("The main diagonal of rels must be empty!")
            else: ## may build new relation matrix
                rels = []
                for i in range(0, len(chars)):
                    rels.append([])
                    for j in range(0, len(chars)):
                        if i == j:
                            rels[i].append(None)
                        elif i < j:
                            rels[i].append(Relation(chars[i], chars[j]))
                        else: ## i > j
                            rels[i].append(rels[j][i].mirror()) ## symmetry
            ## copy values
            self.__chars = []
            self.__rels = []
            for i in range(0, len(chars)):
                self.__chars.append(chars[i])
                self.__rels.append([])
                for j in range(0, len(chars)):
                    self.__rels[i].append(rels[i][j])
                
        ## getters and friends
            
        def getChar(self, i):
            if i < 0 or i >= len(self.__chars):
                raise IndexError("Index is out of bounds!")
            return self.__chars[i]
            
        def getCharsLen(self):
            return len(self.__chars)
    
        def getRel(self, i, j):
            if i < 0 or i >= len(self.__rels) or j < 0 or j >= len(self.__rels):
                raise IndexError("Index is out of bounds!")
            return self.__rels[i][j]
            
        def getRelsLen(self):
            return len(self.__rels)
            
            
        ##########
        ## "real" interaction methods
        ##########
            
        
        ## returns ERR_CHAR1_NOT_ENOUGH_HP if first character can't spent HP and
        ## ERR_CHAR2_NOT_ENOUGH_HP if first can but second can't, else 0
        def useHP(rel, costs1, costs2):
            if not rel.Char1.canUseHP(costs1):
                return ERR_CHAR1_NOT_ENOUGH_HP
            if not rel.Char2.canUseHP(costs2):
                return ERR_CHAR2_NOT_ENOUGH_HP
            rel.Char1.useHP(costs1)
            rel.Char2.useHP(costs2)
            return 0
            
        useHP = staticmethod(useHP)
        
        ## returns ERR_CHAR1/2_NOT_ENOUGH_HP if character 1/2 doesn't have enough HP,
        ## else (if successful) True
        ## the exp will be calculated on what char2 thinks (possible milestone)
        ## and what is the case (actual milestone). 
        ## Except for special milestones because those should always been shown.
        def talk(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            ## use HP
            #++ here you decide how much HP have to be used for the action
            havePaid = Interaction.useHP(rel, 20, 20)
            if havePaid < 0:
                return havePaid
            ## now the action itself
            milestone2b = rel.getMilestoneForExp()
            exp = 0
            if rel.Milestone in (6,7,8): ## boytoy or bff or shag buddy
                exp = 20
            elif milestone2b in (0,1): ## stranger or new friend
                exp = 10
            elif milestone2b in (2,3): ## good or close friend
                exp = 20
            elif milestone2b in (4,5): ## boyfriend or lover
                exp = 30
            elif milestone2b in (-2,-1): ## jerk or idiot
                exp = 10
            elif milestone2b in (-5,-4,-3): ## arch enemy, enemy, creep
                exp = 5
            rel.raiseExp(exp, True)
            rel.increaseTodaysTalk() ## count the talk, maybe set to BFF
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp, True)
                rel.Mirror.increaseTodaysTalk()
            return True
        
        ## this always succeeds because it is thought to be used for parties only
        def partyDance(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            ## now the action itself
            milestone2b = rel.getMilestoneForExp()
            exp = 0
            if rel.Milestone in (6,7,8): ## boytoy or bff or shag buddy
                exp = 5
            elif milestone2b in (0,1): ## stranger or new friend
                exp = 2
            elif milestone2b in (2,3): ## good or close friend
                exp = 10
            elif milestone2b in (4,5): ## boyfriend or lover
                exp = 20
            elif milestone2b in (-2,-1): ## jerk or idiot
                exp = -5
            elif milestone2b in (-5,-4,-3): ## arch enemy, enemy, creep
                exp = -10
            rel.raiseExp(exp, True)
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp, True)
            return True
            
        ## this always succeeds because it is thought to be used for parties only
        def partyHang(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            ## now the action itself
            milestone2b = rel.getMilestoneForExp()
            exp = 0
            if rel.Milestone in (6,7,8): ## boytoy or bff or shag buddy
                exp = 3
            elif milestone2b in (0,1): ## stranger or new friend
                exp = 1
            elif milestone2b in (2,3): ## good or close friend
                exp = 2
            elif milestone2b in (4,5): ## boyfriend or lover
                exp = 3
            elif milestone2b in (-2,-1): ## jerk or idiot
                exp = -5
            elif milestone2b in (-5,-4,-3): ## arch enemy, enemy, creep
                exp = -10
            rel.raiseExp(exp, True)
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp, True)
            return True
            
        #++ as you may guess, question(...) and answer(...)
        #++ belong together and should only be seperated by the actual question
        
        ## returns ERR_CHAR1/2_NOT_ENOUGH_HP if character 1/2 doesn't have enough HP,
        ## False if question couldn't be asked due to milestones and
        ## True if question could be asked (in this case, no exp change)
        def question(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            havePaid = Interaction.useHP(rel, 10, 10) ## use HP
            if havePaid < 0:
                return havePaid
            ## now the action itself
            if rel.Milestone < 2: ## early or negative relationship
                rel.raiseExp(-10) ## questions are a big no-no
                if rel.Mirror != None:
                    rel.Mirror.raiseExp(-10)
                return False
            return True
            
        ## returns True for continuity
        def answer(self, c1I, c2I, answerLevel):
            if not isinstance(answerLevel, int):
                raise TypeError("answerLevel must be an int!")
            rel = self.getRel(c1I, c2I)
            exp = 0
            if answerLevel == 0:
                exp = -30
            elif answerLevel == 1:
                exp = -10
            elif answerLevel == 2:
                exp = 5
            elif answerLevel == 3:
                exp = 25
            rel.raiseExp(exp, True)
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp, True)
            return True
            
        ## returns True for continuity
        #++ I admit this method is especially for the Pokemon DS
        #++ You can probably just delete it
        def cheer(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            exp = float(rel.Char1.getStatsSum()) / 4 + 10
            rel.raiseExp(exp)
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp)
            return True
            
        ## returns ERR_CHAR1/2_NOT_ENOUGH_HP if character 1/2 doesn't have enough HP,
        ## 0 if character 2 ended the conversation earlier,
        ## False if the character can't be phoned (rejects call) and
        ## True if everything was alright
        #++ we use phone instead of call because call is kind of a key word
        def phone(self, c1I, c2I, amountOfTime):
            if not isinstance(amountOfTime, int):
                raise TypeError("amountOfTime must be an int!")
            if amountOfTime <= 0 or amountOfTime > 50:
                raise ValueError("amountOfTime is off limits!")
            rel = self.getRel(c1I, c2I)
            oldHP = rel.Char1.HP
            havePaid = Interaction.useHP(rel, amountOfTime, amountOfTime) ## use HP
            if not (havePaid < 0 or rel.canBePhoned()):
                rel.raiseExp(-50) ## char2 is shocked over the call ;)
                if rel.Mirror != None:
                    rel.Mirror.raiseExp(-50)
                return False
            reduced = amountOfTime
            ## if char2 has to end conversation earlier, do so
            while (havePaid == -2 and amountOfTime > 0):
                amountOfTime = amountOfTime - 1
                havePaid = Interaction.useHP(rel, amountOfTime, amountOfTime)
            if havePaid < 0:
                return havePaid
            reduced = reduced - amountOfTime ## to check if char2 ended conversation
            ## the calculation of the experience
            exp = math.sqrt(float(oldHP) / rel.Char1.getMaxHP())
            exp *= float(amountOfTime) / (rel.getPhonedToday()+1) # * 1.5
            rel.raiseExp(exp, True)
            rel.increasePhonedToday()
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp, True)
                rel.Mirror.increasePhonedToday()
            if (reduced != 0):
                return 0
            return True
            
        #++ as you may guess, presentGift(...) and giveGift(...)
        #++ belong together and should only be seperated by choosing the gift
        
        ## returns ERR_CHAR1/2_NOT_ENOUGH_HP if character 1/2 doesn't have enough HP,
        ## False if the character can't be gifted (rejects gift) and
        ## True if everything was alright
        def presentGift(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            havePaid = Interaction.useHP(rel, 5, 5) ## use HP
            if havePaid < 0:
                return havePaid
            if not rel.takesGifts():
                rel.raiseExp(-10) ## don't take gifts from strangers!
                return False
            return True
            
        ## returns False if gifting the item wasn't possible and 
        ## True if everythings fine.
        ## everything else has to be cleared with presentGift(...)
        def giveGift(self, c1I, c2I, item, reaction):
            rel = self.getRel(c1I, c2I)
            #reaction = rel.Char2.getGiftReaction(giftIndex)
            ## turns over the item if possible
            if item.give(c1I, c2I) == False: 
                return False
            exp = 0
            cp = 0
            if reaction == 0:
                cp = 55
            elif reaction == 1:
                exp = 50
                cp = 60
            elif reaction == 2:
                exp = 100
                cp = 100
            elif reaction == 3:
                exp = 180
                cp = 150
            rel.raiseExp(exp)
            rel.increaseCorruptionPoints(cp)
            if rel.Mirror != None:
                rel.Mirror.raiseExp(exp)
                rel.Mirror.increaseCorruptionPoints(cp)
            return reaction
            
        ## returns ERR_CHAR1/2_NOT_ENOUGH_HP if character 1/2 doesn't have enough HP,
        ## False if the character can't be kissed (rejects kiss) and
        ## True if everything was alright
        def kiss(self, c1I, c2I):
            rel = self.getRel(c1I, c2I)
            havePaid = Interaction.useHP(rel, 5, 5) ## use HP
            if havePaid < 0:
                return havePaid
            if not rel.canKiss():
                rel.raiseExp(-100) ## big time no-no
                if rel.Mirror != None:
                    rel.Mirror.raiseExp(-100)
                return False
            if rel.enoughKissedToday():
                return -3
            rel.raiseExp(20, True)
            rel.increaseKissedToday()
            if rel.Mirror != None:
                rel.Mirror.raiseExp(20, True)
                rel.Mirror.increaseKissedToday()
            return True
        
        ## returns 1/2 if character 1/2 is in a battle already, 
        ## ERR_CHAR1/2_NOT_ENOUGH_HP if character 1/2 doesn't have enough HP and
        ## the Battle instance if everything was alright
        ## never False, because no trainer can escape a Pokemon fight!    
        def startBattle(self, c1I, c2I):
            ## every char can only have one battle at a time
            for i in range(0, self.getCharsLen()):
                if i != c1I and self.getRel(c1I, i).Battle != None:
                    return 1
                if i != c2I and self.getRel(c2I, i).Battle != None:
                    return 2
            rel = self.getRel(c1I, c2I)
            havePaid = Interaction.useHP(rel, 10, 0) ## use HP
            if havePaid < 0:
                return havePaid
            rel = self.getRel(c1I, c2I)
            rel.Battle = Battle(rel)
            if rel.Mirror != None:
                rel.Mirror.Battle = rel.Battle
            return rel.Battle

        ## returns ERR_CHAR1/2_NOT_ENOUGH_HP if character 1 isn't tough enough for that date,
        ## False if character 1 can't affort the date,
        ## "n" if dchar is occupied on day n, -5 if end of days would be reached
        ## and the Date instance if everything was alright
        def startDate(self, c1I, c2I, location, minHP = 100, 
            days = 2, money = 100, startMood = 0.5, occupied = []):
            ## catch errors:
            if not (isinstance(location, int) and isinstance(minHP, int) and 
                isinstance(days, int) and isinstance(money, int)):
                raise TypeError("location, minHP, days and money " +
                    "must be ints!")
            if not (minHP >= 0 and days >= 0 and money >= 0):
                raise ValueError("minHP, days and money must be non-negative!")
            if not isinstance(startMood, float):
                raise TypeError("startMood must be a float!")
            if startMood < 0.0 or startMood > 1.0:
                raise ValueError("startMood must be between 0.0 and 1.0 inclusive")
            if not (isinstance(occupied, tuple) or isinstance(occupied, list) or
                isinstance(occupied, renpy.python.RevertableList)):
                raise TypeError("occupied must be a tuple or list of ints!")
            for i in occupied:
                if not isinstance(i, int):
                    raise TypeError("occupied must be a tuple or list of ints!")
            ## date starting
            rel = self.getRel(c1I, c2I) ## tests c1I, c2I for validity
            if not rel.Char1.canUseHP(minHP):
                return ERR_CHAR1_NOT_ENOUGH_HP
            if not rel.Char1.canSpendMoney(money):
                return False
            global day
            global MAX_DAYS
            if MAX_DAYS-day <= days:
                return -5
            for i in range(day, day+days+1):
                if i in occupied:
                    if i == day:
                        return "today"
                    elif i == day + 1:
                        return "tomorrow"
                    else:
                        return "in "+str(i-day)+" days"
            rel.Char1.spendMoney(money)
            rel.Date = Date(rel, c1I, c2I, location, days, startMood)
            if rel.Mirror != None:
                rel.Mirror.Date = rel.Date
            return rel.Date
            
        ## returns False if the character hasn't enough money,
        ## -1 if buying would go over the limit of this item and
        ## True if everything was alright
        def buy(self, charIndex, item, canMakeDebt = False):
            if not isinstance(charIndex, int):
                raise TypeError("charIndex must be an int!")
            if charIndex < 0 or charIndex >= self.getCharsLen():
                raise ValueError("charIndex is off bounds!")
            if not isinstance(item, Item):
                raise TypeError("item must be instance of Item!")
            if not isinstance(canMakeDebt, bool):
                raise TypeError("canMakeDebt must be True or False!")
            if not self.getChar(charIndex).canSpendMoney(item.Price, canMakeDebt):
                return False
            if item.addCarrying(charIndex, 1) == -1:
                return -1
            ## else the character now has the item
            self.getChar(charIndex).spendMoney(item.Price, canMakeDebt)
            return True
            
        ## a selling method is still to be implemented
            
        
    ## a class for using Interaction with char1 always being the same
    ## the use of an instance of this class will be enough for most dating sims
    class SingleInteraction(store.object):
        
        def __init__(self, interaction, protaIndex):
            if not isinstance(interaction, Interaction):
                raise TypeError("interaction must be an Interaction!")
            self.__interaction = interaction
            self.__protaIndex = protaIndex
            
        ## getters
        def getInteraction(self):
            return self.__interaction
        Interaction = property(getInteraction)
        def getProtaIndex(self):
            return self.__protaIndex
        ProtaIndex = property(getProtaIndex)
        def getChar(self, i):
            return self.Interaction.getChar(i)
        def getRel(self, i):
            return self.Interaction.getRel(self.ProtaIndex, i)
        def getRelByDSC(self, char):
            for i in range(self.Interaction.getCharsLen()):
                if self.Interaction.getChar(i) == char:
                    return self.getRel(i)
            return None
            
        #def levelUp(self, char):
        #    return self.Interaction.levelUp(self.ProtaIndex, char)
        #def hasChanged(self, char):
        #    return self.Interaction.hasChanged(self.ProtaIndex, char)
            
        ## interactions
        def talk(self, char):
            return self.Interaction.talk(self.ProtaIndex, char)
        def partyDance(self, char):
            return self.Interaction.partyDance(self.ProtaIndex, char)
        def partyHang(self, char):
            return self.Interaction.partyHang(self.ProtaIndex, char)
        def question(self, char):
            return self.Interaction.question(self.ProtaIndex, char)
        def answer(self, char, answerLevel):
            return self.Interaction.answer(self.ProtaIndex, char, answerLevel)
        def cheer(self, char):
            return self.Interaction.cheer(self.ProtaIndex, char)
        def phone(self, char, amountOfTime):
            return self.Interaction.phone(self.ProtaIndex, char, amountOfTime)
        def presentGift(self, char):
            return self.Interaction.presentGift(self.ProtaIndex, char)
        def giveGift(self, char, item, reaction):
            return self.Interaction.giveGift(self.ProtaIndex, char, item, reaction)
        def kiss(self, char):
            return self.Interaction.kiss(self.ProtaIndex, char)
        
        def startBattle(self, char):
            return self.Interaction.startBattle(self.ProtaIndex, char)

        def startDate(self, char, location, minHP = 100, 
            days = 2, money = 100, startMood = 0.5, occupied = []):
            return self.Interaction.startDate(self.ProtaIndex, char, location,
                minHP, days, money, startMood, occupied)
            
        def buy(self, item, canMakeDebt = False):
            return self.Interaction.buy(self.ProtaIndex, item, canMakeDebt)
            
    ## the class for prota - dchar interaction
    ## as thus, we have special return values
    ## but whatever is returned normally, None is (possible additionally) returned
    ## for corrupted parameters
    #class Interaction(store.object): #(object): *

        ## returns 0-4 if everything was okay, -1 if no gift there,
        ## None if invalid parameters, False if gift is not accepted
    #    def giveGiftTo(self, giftNumber, dcharNumber):
    #        if type(dcharNumber) != int or type(giftNumber) != int:
    #            return None
    #        if giftNumber < 0 or giftNumber >= len(inventory) or ( 
    #            #giftNumber > lastGiftable or    
    #             dcharNumber < 0 or dcharNumber >= len(dcharlist)):
    #            return None
    #        if dcharlist[dcharNumber].isTakingGifts() == False:
    #            return False
    #        if inventory[giftNumber].getQuantity() == 0:
    #            return -1
    #        inventory[giftNumber].add(-1)
            
            
        ### The stuff that hasn't to do with dchars directly
            
        ## None if wrong parameters, False if item not
        ## buyable or prota has to less money
    #    def buyItem(self, itemNumber):
    #        if type(itemNumber) != int:
    #            return None
    #        if itemNumber < 0 or itemNumber >= len(inventory):
    #            return None
    #        if inventory[itemNumber].isBuyable() != True:
    #            return False
    #        if prota.spendMoney(inventory[itemNumber].Price, False) == True:
    #            inventory[itemNumber].add(1)
    #            return True
    #        else:
    #            return False
            
    
            
