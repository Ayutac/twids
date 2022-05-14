init -100 python:
    
    
    ## contains the stats that can be of interest in a game
    class Stats(store.object):
    
        ## initializes the stats
        ## min/max tell the range of the stats including None 
        ## if there's no limit in one or both directions
        def __init__(self, names, min = 0, max = 50, base = None, defaultsTo = None):
            store.object.__init__(self)
            ## error handling
            if not isinstance(names, (tuple, list, renpy.python.RevertableList)):
                raise TypeError("The names must be a tuple or list of strings!")
            for i in range(0, len(names)):
                if not isinstance(names[i], (str, unicode)):
                    raise TypeError("Name "+i+" is a "+type(names[i])+" instead of a string!")
            if not ((isinstance(min, int) or min == None) and (
                isinstance(max, int) or max == None)):
                raise TypeError("The limits must be ints or None!")
            if min != None and max != None and min > max:
                raise ValueError("min must be smaller than or equal to max!")
            if not (isinstance(defaultsTo, (tuple, list, renpy.python.RevertableList)) or defaultsTo == None):
                raise TypeError("The defaults must be a tuple or list or None!")
            if base <> None:
                if len(names) <> len(base):
                    raise TypeError("The base must be of the same length as the names!")
                for i in range(0, len(base)):
                    if not isinstance(base[i], int):
                        raise TypeError("Default "+i+" is a "+type(base[i])+" instead of an int!")
            if not (isinstance(base, (tuple, list, renpy.python.RevertableList)) or base == None):
                raise TypeError("The defaults must be a tuple or list or None!")
            if defaultsTo <> None:
                if len(names) <> len(defaultsTo):
                    raise TypeError("The defaults must be of the same length as the names!")
                for i in range(0, len(defaultsTo)):
                    if not isinstance(defaultsTo[i], int):
                        raise TypeError("Default "+i+" is a "+type(defaultsTo[i])+" instead of an int!")
            ## copy values
            self.__names = 1 * names
            self.__min = min
            self.__max = max
            if base <> None :
                self.__base = 1 * base
            else:
                self._base = None
            if defaultsTo <> None :
                self.__defaultsTo = 1 * defaultsTo
            else:
                self._defaultsTo = None
    
        ## getters and properties:
        
        def getName(self, index):
            self.checkIndexBounds(index)
            return self.__names[index] ## throws TypeError
            
        def getNames(self):
            return 1* self.__names
            
        ## returns the index of a given name or ERR_STAT_NOT_FOUND if
        ## the name represents no stat
        def getIndex(self, name):
            if not isinstance(name, (str, unicode)):
                raise TypeError("name must be a string!")
            for i in range(0, len(self.__names)):
                if name == self.__names[i]:
                    return i
            return ERR_STAT_NOT_FOUND
        
        def getLength(self):
            return len(self.__names)
        Length = property(getLength)
        
        def getMin(self):
            return self.__min
        Min = property(getMin)
        
        def getMax(self):
            return self.__max
        Max = property(getMax)
        
        ## tells if a value is out of bounds
        ## STAT_BELOW_MIN if too small, STAT_WITHIN_RANGE if right, STAT_ABOVE_MAX if too big
        def checkBounds(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if self.Min != None and val < self.Min:
                return STAT_BELOW_MIN
            if self.Max != None and val > self.Max:
                return STAT_ABOVE_MAX
            return STAT_WITHIN_RANGE
            
        def checkIndexBounds(self, index):
            if index < 0 or index >= len(self.__names):
                raise IndexError("index is out of bounds!")
            
    
    
    ## the class for Dating Sim Characters (boys, girls and protagonists alike)
    ## it is implied here that HP and battleHP must be >= 0
    ## unname is short for unknown name
    class DSC(store.object): ## DSC is short for Dating Sim Character
        
        def __init__(self, statRef, name, stats, genS = "'s", gender = "female", 
            HP = 0, battleHP = 0, battleBonus = 0, maxBattleBonus = 50, 
            money = 0, giftMin = None, giftMax = None,talkMin = 3, talkMax = 10, 
            talkDayRange = 4, giftReaction = [], crypt7 = None, crypt6 = None,    
            crypt5 = None, crypt4 = None, crypt3 = None,
            unname ="???", shortUnname="???", hasMet=False):
        
            ## error handling
            if not isinstance(statRef, Stats):
                raise TypeError("statRef must be of type Stats!")
            if not ((isinstance(name, str) or isinstance(name, unicode)) and 
                (isinstance(genS, str) or isinstance(genS, unicode))):
                raise TypeError("The name must be a string!")
            if not (isinstance(gender, str) or isinstance(gender, unicode)):
                raise TypeError("The gender must be a string!")
            if not (isinstance(unname, str) or isinstance(unname, unicode)):
                raise TypeError("The unknown name must be a string!")
            if not (isinstance(shortUnname, str) or isinstance(shortUnname, unicode)):
                raise TypeError("The short unknown name must be a string!")
            if not (len(name) > 0):
                raise TypeError("Character needs a real name!")
            if not (isinstance(stats, tuple) or isinstance(stats, list) or
                isinstance(stats, renpy.python.RevertableList)):
                raise TypeError("The stats must be a tuple or list of ints!")
            if len(stats) != statRef.Length:
                raise ValueError("The number of given stats doesn't match the number of existing stats!")
            for i in range(0, len(stats)):
                if statRef.checkBounds(stats[i]) != 0: ## throws non-int exceptions
                    raise ValueError("At least one stat is out of bounds!")
            if not (isinstance(HP, int) and isinstance(battleHP, int) and 
                isinstance(battleBonus, int) and isinstance(maxBattleBonus, int) and
                isinstance(money, int)):
                raise TypeError("HP, battleHP, battleBonus, maxBattleBonus, and money must be ints!")
            if HP < 0 or battleHP < 0 or battleBonus < 0 or maxBattleBonus < 0: ## here is the non-negativity
                raise ValueError("HP, battleHP, battleBonus and maxBattleBonus must be non-negative!")
            #++ the following variables are the caps for the special milestones Boytoy and BFF
            #++ if you don't want to use it, do not change it here but in interaction.rpy
            if not (isinstance(talkDayRange, int) and (
                isinstance(giftMin, int) or giftMin == None) and (
                isinstance(giftMax, int) or giftMax == None) and (
                isinstance(talkMin, int) or talkMin == None) and (
                isinstance(talkMax, int) or talkMax == None)):
                raise TypeError("The limits must be ints or None!")
            if (giftMin != None and giftMax != None and giftMin > giftMax) or (
                talkMin != None and talkMax != None and talkMin > talkMax):
                raise ValueError("mins must be smaller than or equal to maxs!")
            if not (isinstance(giftReaction, tuple) or isinstance(giftReaction, list) or
                isinstance(giftReaction, renpy.python.RevertableList)):
                raise TypeError("giftReaction must be a tuple or list of ints!")
            for i in range(0, len(giftReaction)):
                if not isinstance(giftReaction[i], int):
                    raise TypeError("At least one entry of giftReaction is no int!")
            if not ((isinstance(crypt7, (str, unicode)) or crypt7 == None) and (
                isinstance(crypt6, (str, unicode)) or crypt6 == None) and (
                isinstance(crypt5, (str, unicode)) or crypt5 == None) and (
                isinstance(crypt4, (str, unicode)) or crypt4 == None) and (
                isinstance(crypt3, (str, unicode)) or crypt3 == None)):
                raise TypeError("The crypting names must be strings or None!")
            if (crypt7 != None and len(crypt7) != 7) or (
                crypt6 != None and len(crypt6) != 6) or (
                crypt5 != None and len(crypt5) != 5) or (
                crypt4 != None and len(crypt4) != 4) or (
                crypt3 != None and len(crypt3) != 3):
                raise ValueError("The crypting names must have their indicated lenght!")
            if not isinstance(hasMet, bool):
                raise TypeError("hasMet must be a bool!")
                
            ## copy values
            self.__statRef = statRef
            self.__name = name
            self.__genS = genS
            self.__unname = unname
            self.__shortUnname = shortUnname
            self.__hasMet = hasMet
            self.__gender = gender
            self.__stats = []
            for i in range(0, len(stats)):
                self.__stats.append(stats[i])
            self.__HP = HP
            self.__battleHP = battleHP
            self.__maxBattleBonus = maxBattleBonus
            if battleBonus > maxBattleBonus:
                self.__battleBonus = maxBattleBonus
            else:
                self.__battleBonus = battleBonus
            self.__money = money
            self.__giftMin = giftMin
            self.__giftMax = giftMax
            self.__talkMin = talkMin
            self.__talkMax = talkMax
            self.__talkDayRange = talkDayRange
            self.__giftReaction = 1 * giftReaction
            s = self.__name.lower()
            ## create crypt names
            if crypt7 == None:
                crypt7 = ''
                i = 0
                while len(crypt7) < 7:
                    crypt7 += s[i]
                    i += 1
                    if i == len(s):
                        i = 0
            self.__crypt7 = crypt7
            if crypt6 == None:
                crypt6 = ''
                i = 0
                while len(crypt6) < 6:
                    crypt6 += s[i]
                    i += 1
                    if i == len(s):
                        i = 0
            self.__crypt6 = crypt6
            if crypt5 == None:
                crypt5 = ''
                i = 0
                while len(crypt5) < 5:
                    crypt5 += s[i]
                    i += 1
                    if i == len(s):
                        i = 0
            self.__crypt5 = crypt5
            if crypt4 == None:
                crypt4 = ''
                i = 0
                while len(crypt4) < 4:
                    crypt4 += s[i]
                    i += 1
                    if i == len(s):
                        i = 0
            self.__crypt4 = crypt4
            if crypt3 == None:
                crypt3 = ''
                i = 0
                while len(crypt3) < 3:
                    crypt3 += s[i]
                    i += 1
                    if i == len(s):
                        i = 0
            self.__crypt3 = crypt3
    
        ## getters and properties:
        ## (yes, at the end of the class is something else)
        
        def getStatRef(self):
            return self.__statRef
        StatRef = property(getStatRef)
        
        def hasMet(self):
            return self.__hasMet
        def meet(self):
            self.__hasMet = True
        
        def getUnname(self):
            return self.__unname
        def setUnname(self, unname):
            if not (isinstance(unname, str) or isinstance(unname, unicode)):
                raise TypeError("New unname must be string!")
            self.__unname = unname
        Unname = property(getUnname, setUnname)
        
        def getShortUnname(self):
            return self.__shortUnname
        def setShortUnname(self, shortUnname):
            if not (isinstance(shortUnname, str) or isinstance(shortUnname, unicode)):
                raise TypeError("New shortUnname must be string!")
            self.__shortUnname = shortUnname
        ShortUnname = property(getShortUnname, setShortUnname)
        
        def getName(self):
            return self.__name
        def setName(self, name):
            if not (isinstance(name, str) or isinstance(name, unicode)):
                raise TypeError("New name must be string!")
            self.__name = name
        Name = property(getName, setName)
        
        def getDisplayName(self):
            if self.__hasMet:
                return self.__name
            else:
                return self.__unname
        DisplayName = property(getDisplayName)
        
        def getShortDisplayName(self):
            if self.__hasMet:
                return self.__name
            else:
                return self.__shortUnname
        ShortDisplayName = property(getShortDisplayName)
        
        def getShortDisplayNameS(self):
            if self.__hasMet:
                return self.NameS
            else:
                return self.ShortUnname
        ShortDisplayNameS = property(getShortDisplayNameS)
        
        def getGenS(self):
            return self.__genS
        def setGenS(self, genS):
            if not (isinstance(genS, str) or isinstance(genS, unicode)):
                raise TypeError("Genitive must be string!")
            self.__genS = genS
        GenS = property(getGenS, setGenS)
        
        def getNameS(self):
            return self.Name + self.__genS
        NameS = property(getNameS)
        
        def getGender(self):
            return self.__gender
        def setGender(self, gender):
            if not (isinstance(genS, str) or isinstance(genS, unicode)):
                raise TypeError("Gender must be string!")
            self.__gender = gender
        Gender = property(getGender, setGender)
        
        def getPronoun(self):
            if self.__gender == "female":
                return "she"
            elif self.__gender == "male":
                return "he"
            else:
                return "they"
        Pronoun = property(getPronoun)
        
        def getPronounC(self):
            if self.__gender == "female":
                return "She"
            elif self.__gender == "male":
                return "He"
            else:
                return "They"
        PronounC = property(getPronounC)
        
        def getPronounG(self):
            if self.__gender == "female":
                return "her"
            elif self.__gender == "male":
                return "his"
            else:
                return "their"
        PronounG = property(getPronounG)
        
        def getPronounGC(self):
            if self.__gender == "female":
                return "Her"
            elif self.__gender == "male":
                return "His"
            else:
                return "Their"
        PronounGC = property(getPronounGC)
        
        def getStat(self, index):
            self.StatRef.checkIndexBounds(index)
            return self.__stats[index]
            
        def getStats(self):
            return 1 * self.__stats
            
        def setStat(self, index, val):
            self.StatRef.checkIndexBounds(index)
            bounded = self.StatRef.checkBounds(val)
            if bounded == -1:
                self.__stats[index] = self.StatRef.Min
                ## this never becomes None
            elif bounded == 1:
                self.__stats[index] = self.StatRef.Max
                ## this never becomes None
            else:
                self.__stats[index] = val
                
        def raiseStat(self, index, val):
            self.setStat(index, self.getStat(index) + val)
            ## manages all error handling :)
            
        def getStatsSum(self):
            sum = 0
            for stat in self.__stats:
                sum = sum + stat
            return sum
            
        ## The main difference between the setter of HP and battleHP
        ## is that in case the new value is below 0, then HP doesn't react,
        ## because probably someone is trying to use more HP than possible,
        ## but battleHP goes to 0 because someone finished this character of!
            
        def getHP(self):
            return self.__HP
        def setHP(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if val < 0:
                return
            else:
                self.__HP = val
        HP = property(getHP, setHP)
            
        #++ if you want to let battleHP be the same thing as HP,
        #++ comment the following code out:
        def getBattleHP(self):
            return self.__battleHP
        def setBattleHP(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if val < 0:
                self.__battleHP = 0
            else:
                self.__battleHP = val
        #++ and comment the following in:
        #def getBattleHP(self):
        #    return self.__HP
        #def setBattleHP(self, val):
        #    if not isinstance(val, int):
        #        raise TypeError("The value must be an int!")
        #    if val < 0:
        #        self.__HP = 0
        #    else:
        #        self.__HP = val
        #++ this code will still act as I said before (only the setter
        #++ of battleHP sets the HP to 0 if they are too low)
        BattleHP = property(getBattleHP, setBattleHP)
        
        def getBattleBonus(self):
            return self.__battleBonus
        def setBattleBonus(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if val < 0:
                raise ValueError("Value must be non-negative!")
            if val > self.MaxBattleBonus:
                self.__battleBonus = self.MaxBattleBonus
            else:
                self.__battleBonus = val
        BattleBonus = property(getBattleBonus, setBattleBonus)
            
        def getMaxBattleBonus(self):
            return self.__maxBattleBonus
        def setMaxBattleBonus(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if val < 0:
                raise ValueError("Value must be non-negative!")
            self.__maxBattleBonus = val
            self.BattleBonus = self.BattleBonus ## calls set and may reduce the BB due to smaller max
        MaxBattleBonus = property(getMaxBattleBonus, setMaxBattleBonus)
            
        ## returns True if the HP could be used, else False
        def canUseHP(self, amount):
            if not isinstance(amount, int):
                raise TypeError("The value must be an int!")
            if amount <= 0:
                return True
            if self.HP - amount < 0:
                return False
            return True
        
        ## uses HP if possible, returns True if successful, else False
        def useHP(self, amount):
            able = self.canUseHP(amount)
            if able:
                self.HP = self.HP - amount
            return able
    
        ## tells the maximal health points the character can get
        #++ in this example, every character will get the same amount
        #++ of health points based on a linear formula.
        #++ however, we use the first stat for that, knowing in our
        #++ Pokemon Sim Date it is Strength
        def getMaxHP(self):
            strength = self.getStat(0)
            return int(math.ceil(3.75*strength + 62.25))
        #++ changing this is only necessary if the HP of someone
        #++ else than the playable characters matter
        #++ if you want individual health points for all characters,
        #++ just sort them by their name, e.g.
        #def getMaxHP(self):
        #    if self.Name == "Brock":
        #        return int(math.ceil(3.75*self.Strength + 62.25))
        #    elif self.Name == "Nerd":
        #        return 42*day
        #    else:
        #        return 100
        #++ if you do that, you have to watch out the names used here
        #++ match the one you're actually give the guys when creating them
        
        ## this method restores health points just like useHP(-val), with the
        ## difference that this method forbids to exceed maxHP
        ## this also can reduce the points if the character has more HP + val
        ## than maxHP
        def restoreHP(self, val = None):
            if val == None:
                self.HP = self.getMaxHP()
                return
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            maxHP = self.getMaxHP()
            if self.HP + val > maxHP:
                self.HP = maxHP
            else:
                self.HP = self.HP + val
    
        ## looses battle HP, this always works
        ## again, with a negative value the battleHP 
        ## can be increased
        def looseBattleHP(self, val):
            self.BattleHP = self.BattleHP - val
    
        ## since the day variable is critical in every Dating Sim, I allow
        ## myself to use this global here. Else it would be bad style
        #++ if you want battleHP the same as HP,
        #++ comment this out:
        def getMaxBattleHP(self):
            if day >= BATTLE_HP_INCREASE_4:
                return self.BattleBonus + BATTLE_HP_AMOUNT_4
            elif day >= BATTLE_HP_INCREASE_3:
                return self.BattleBonus + BATTLE_HP_AMOUNT_3
            elif day >= BATTLE_HP_INCREASE_2:
                return self.BattleBonus + BATTLE_HP_AMOUNT_2
            elif day >= BATTLE_HP_INCREASE_1:
                return self.BattleBonus + BATTLE_HP_AMOUNT_1
            else:
                return self.BattleBonus + BATTLE_HP_AMOUNT_0
            #++ and this in:
        #def getMaxBattleHP(self):
        #    return self.getMaxHP()
    
        ## works exactly the same as restoreHP
        def restoreBattleHP(self, val = None):
            if val == None:
                self.BattleHP = self.getMaxBattleHP()
                return
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            maxHP = self.getMaxBattleHP()
            if self.BattleHP + val > maxHP:
                self.BattleHP = maxHP
            else:
                self.BattleHP = self.BattleHP + val
        
        def getMoney(self):
            return self.__money
        def setMoney(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            self.__money = val
        Money = property(getMoney, setMoney)
        
        ## returns True if the money could be spent, else False
        ## (says nothing about making debts!)
        def canSpendMoney(self, amount, canMakeDebt = False):
            if amount == 0:
                return True
            if not isinstance(amount, int):
                raise TypeError("The value must be an int!")
            if not isinstance(canMakeDebt, bool):
                raise TypeError("canMakeDebt must be True or False!")
            if amount > 0 and self.Money - amount < 0 and not canMakeDebt:
                return False
            return True
        
        ## spends money if possible, returns True if successful, else False
        def spendMoney(self, amount, canMakeDebt = False):
            able = self.canSpendMoney(amount, canMakeDebt)
            if able:
                self.Money = self.Money - amount
            return able
            
        ## the previous 2 methods were divided in such way because
        ## sometimes more conditions than being able to spend money
        ## must been checked
            
        def increaseMoney(self, money):
            return self.spendMoney(-money, False)
        
        def getGiftMin(self):
            return self.__giftMin
        GiftMin = property(getGiftMin)
        def getGiftMax(self):
            return self.__giftMax                    
        GiftMax = property(getGiftMax)
        
        ## tells if a value is out of bounds
        ## -1 if too small, 0 if right, 1 if too big
        def checkGiftBounds(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if self.GiftMin != None and val < self.GiftMin:
                return -1
            if self.GiftMax != None and val > self.GiftMax:
                return 1
            return 0
        
        def getTalkMin(self):
            return self.__talkMin
        TalkMin = property(getTalkMin)
        def getTalkMax(self):
            return self.__talkMax
        TalkMax = property(getTalkMax)
        def getTalkDayRange(self):
            return self.__talkDayRange
        TalkDayRange = property(getTalkDayRange)
        
        ## tells if a value is out of bounds
        ## -1 if too small, 0 if right, 1 if too big
        def checkTalkBounds(self, val):
            if not isinstance(val, int):
                raise TypeError("The value must be an int!")
            if self.TalkMin != None and val < self.TalkMin:
                return -1
            if self.TalkMax != None and val > self.TalkMax:
                return 1
            return 0
            
        def getGiftReaction(self, index):
            if i < 0 or i >= len(self.__giftReaction):
                raise IndexError("index is out of bounds!")
            return self.__giftReaction[index]
        
        
        def getCrypt7(self):
            return self.__crypt7
        Crypt7 = property(getCrypt7)
        def getCrypt6(self):
            return self.__crypt6
        Crypt6 = property(getCrypt6)
        def getCrypt5(self):
            return self.__crypt5
        Crypt5 = property(getCrypt5)
        def getCrypt4(self):
            return self.__crypt4
        Crypt4 = property(getCrypt4)
        def getCrypt3(self):
            return self.__crypt3
        Crypt3 = property(getCrypt3)
            
            
        ##########
        ## now something different from getters and friends
        ##########
            
        
        ## returns the earned money or ERR_CHAR1_NOT_ENOUGH_HP if not enough HP.
        #++ the basic idea is that only stats influence the money earned
        #++ and you can control which stats inluences the income how
        #++ including 0.0 (not at all) or even negative values!
        def work(self, hp, statFactors):
            ## error handling
            if not (isinstance(statFactors, tuple) or isinstance(statFactors, list)):
                raise TypeError("statFactors must be a tuple or list of ints!")
            if len(statFactors) != self.StatRef.Length:
                raise ValueError("The number of given stat factors doesn't match the number of existing stats!")
            for i in range(0, len(statFactors)):
                if not isinstance(statFactors[i], float):
                    raise TypeError("The factors must be floats!")
            ## tribute costs
            if not self.useHP(hp):
                return ERR_CHAR1_NOT_ENOUGH_HP
            ## actual function
            #++ basically a weight sum function, change out with anything you like
            money = 0
            for i in range(0, len(statFactors)):
                money = money + self.getStat(i)*statFactors[i]
            money = int(math.floor(money))
            self.increaseMoney(money) ## could also decrease money
            return money
            
        ## returns a list / tuple with the increased stats in proper order or
        ## -1 if not enough HP or False if too less money
        ## basically makes raising stats easier
        def train(self, hp, stats, costs = 0):
            ## error handling
            if not (isinstance(stats, tuple) or isinstance(stats, list)):
                raise TypeError("The stats must be a tuple or list of ints!")
            if len(stats) != self.StatRef.Length:
                raise ValueError("The number of given stats doesn't match the number of existing stats!")
            for i in range(0, len(stats)):
                if self.StatRef.checkBounds(stats[i]) != 0:
                    raise ValueError("At least one stat is out of bounds!")
            ## tribute costs
            if not self.canSpendMoney(costs, False):
                return False
            if not self.useHP(hp):
                return -1
            self.spendMoney(costs, False)
            ## raise stats
            oldStats = self.getStats()
            increase = []
            for i in range(0, len(stats)):
                self.raiseStat(i, stats[i])
                increase.append(self.getStat(i) - oldStats[i])
            return increase
