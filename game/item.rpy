###
# 
# Created on 18.03.2012 by Sebastian Koch
###

# When testing in Renpy, make it Renpy-runable (marked with *) 

init -100 python:
    
    class Item(store.object):
        
        def hasItemsOfWith(char, itemSelection):
            ## TODO needs proper initializing
            if not isinstance(char, int):
                raise TypeError("char must be an int!")
            if not (isinstance(itemSelection, tuple) or isinstance(itemSelection, list) or
                isinstance(itemSelection, renpy.python.RevertableList)):
                raise TypeError("itemSelection must be a tuple or list of ints!")
            for i in range(0, len(itemSelection)):
                if not isinstance(itemSelection[i], Item):
                    raise TypeError("itemSelection must be a tuple or list of items!")
            count = 0
            for item in itemSelection:
                count += item.getCarrying(char)
            return count
        
        hasItemsOfWith = staticmethod(hasItemsOfWith)
        
        ## about the copy-paste here see getCarrying() below
        
        def hasItemsOfStored(char, itemSelection):
            ## TODO needs proper initializing
            if not isinstance(char, int):
                raise TypeError("char must be an int!")
            if not (isinstance(itemSelection, tuple) or isinstance(itemSelection, list) or
                isinstance(itemSelection, renpy.python.RevertableList)):
                raise TypeError("itemSelection must be a tuple or list of ints!")
            for i in range(0, len(itemSelection)):
                if not isinstance(itemSelection[i], int):
                    raise TypeError("itemSelection must be a tuple or list of ints!")
            count = 0
            for item in itemSelection:
                count += item.getStored(char)
            return count
        
        hasItemsOfStored = staticmethod(hasItemsOfStored)
        
        __numberOfCharacters = 1
        
        __defaultChar = 1
        
        def initialize(numberOfCharacters, defaultChar):
            if not (isinstance(numberOfCharacters, int) and isinstance(defaultChar, int)):
                raise TypeError("numberOfCharacters and defaultChar must be ints!")
            if defaultChar < 0 or defaultChar >= numberOfCharacters:
                raise ValueError("defaultChar is off bounds!")
            Item.__numberOfCharacters = numberOfCharacters
            Item.__defaultChar = defaultChar
        initialize = staticmethod(initialize)
        
        def getNumberOfCharacters():
            return Item.__numberOfCharacters
        getNumberOfCharacters = staticmethod(getNumberOfCharacters)
        def getDefaultChar():
            return Item.__defaultChar
        getDefaultChar = staticmethod(getDefaultChar)
        def setDefaultChar(defaultChar):
            if not isinstance(defaultChar, int):
                raise TypeError("defaultChar must be an int!")
            if defaultChar < 0 or defaultChar >= Item.getNumberOfCharacters():
                raise ValueError("defaultChar is off bounds!")
            Item.__defaultChar = defaultChar
        setDefaultChar = staticmethod(setDefaultChar)
    
        
        def __init__(self, name, undArt="a", ## undefined article
            limit = None, price = 0, sell = 0.5, mass = 0.0, volume = 0.0, 
            arrangement = ((True,),), angle = 0.0, equipPlace = None):
            store.object.__init__(self)
            ## error handling
            if not (isinstance(name, str) or isinstance(name, unicode)):
                raise TypeError("The name must be a string!")
            if not (isinstance(undArt, str) or isinstance(undArt, unicode)):
                raise TypeError("The undefined article must be a string!")
            if not isinstance(price, int):
                raise TypeError("price must be an int!")
            if not (isinstance(mass, float) and
                isinstance(volume, float) and isinstance(angle, float)):
                raise TypeError("mass, volume and angle must be floats!")
            if mass < 0 or volume < 0:
                raise ValueError("mass and volume must be non-negative!")
            if not (limit == None or (isinstance(limit, int) and limit >= 0)):
                raise ValueError("limit must be None or a non-negative int!")
            if not (sell == None or (isinstance(sell, float) and sell >= 0)):
                raise ValueError("sell must be None or a non-negative float!")
            if not isinstance(arrangement, tuple):
                raise TypeError("Arrangement must be a 2-dimensional tuple of booleans!")
            if len(arrangement) == 0:
                raise ValueError("Item must take 2-dimensional space!")
            if not isinstance(arrangement[0], tuple):
                raise TypeError("Arrangement must be a 2-dimensional tuple of booleans!")
            len2 = len(arrangement[0])
            for i in range(1, len(arrangement)):
                if not isinstance(arrangement[i], tuple):
                    raise TypeError("Arrangement must be a 2-dimensional tuple of booleans!")
                if len(arrangement[i]) != len2:
                    raise TypeError("Arrangement isn't a rectangularly tuple!")
                for j in range(0, len2):
                    if not isinstance(arrangement[i][j], bool):
                        raise TypeError("Arrangement must be a 2-dimensional tuple of booleans!")
            ## copying values
            self.__name = name
            self.__undArt = undArt
            self.__limit = limit
            self.__price = price
            self.__sell = sell
            self.__mass = mass
            self.__volume = volume
            self.__arrangement = ()
            #for i in range(0, len(arrangement)):
            #    self.__arrangement.append(1 * arrangement[i])
            self.__angle = angle % 360
            self.__equipPlace = equipPlace ## due to poor implementation no type check or whatever
            ## arrays so we can store the information into every character
            self.__carrying = []
            self.__stored = []
            self.__equipped = []
            for i in range(0, Item.getNumberOfCharacters()):
                self.__carrying.append(0)
                self.__stored.append(0)
                self.__equipped.append(0)
                
        ## getters and friends
        
        def checkBounds(self, char):
            if (config.developer == True) and (
                (roomOfDchar == CHAR_NONE and Item.getDefaultChar() != CHAR_PROTA) or 
                Item.getNumberOfCharacters() != LEN_CHAR):
                raise ValueError("THIS ERROR SHOULD NOT OCCUR!\n defChar="+str(Item.getDefaultChar())+", charProta="+str(CHAR_PROTA)+", numChar="+str(Item.getNumberOfCharacters())+", lenChar="+str(LEN_CHAR))
            if char < 0 or char >= Item.getNumberOfCharacters():
                raise ValueError("char is off bounds!")

        def getName(self):
            return self.__name
        def setName(self, name):
            if not isinstance(name, str):
                raise TypeError("New name must be string!")
        Name = property(getName, setName)
        
        def getUndArt(self):
            return self.__undArt
        UndArt = property(getUndArt)
        
        def getNameWithArt(self):
            return self.UndArt + " " + self.Name
        NameWithArt = property(getNameWithArt)
        
        def getLimit(self):
            return self.__limit
        Limit = property(getLimit)
        
        def getPrice(self):
            return self.__price
        Price = property(getPrice)
        def isBuyable(self):
            return self.Price > 0
        def getSell(self):
            return self.__sell
        Sell = property(getSell)
        def isSellable(self):
            return self.getSell() != None
        def getSellPrice(self):
            if not self.isSellable():
                return None
            return Math.floor(self.getPrice()*self.getSell())
        
        def getMass(self):
            return self.__mass
        Mass = property(getMass)
        def getVolume(self):
            return self.__volume
        Volume = property(getVolume)
        
        def getArrangement(self):
            arr = 1 * self.__arrangement
            for i in range(0, len(self.__arrangement)):
                arr[i] = 1 * self.__arrangement[i]
            return arr
        Arrangement = property(getArrangement)
        def getWidth(self):
            return len(self.__arrangement)
        Width = property(getWidth)
        def getHeight(self):
            return len(self.__arrangement[0])
        Height = property(getHeight)
        def getAngle(self):
            return self.__angle
        Angle = property(getAngle)
        
        def getEquipPlace(self):
            return self.__equipPlace
        EquipPlace = property(getEquipPlace)
        def getEquipped(self, char):
            self.checkBounds(char)
            return self.__equipped[char]
        def getEquippedD(self):
            return self.getEquipped(Item.getDefaultChar())
        EquippedD = property(getEquippedD)
        
        ## more important getters and other methods:
        
        ## you will notice the methods concerning carrying and stored
        ## are pretty identical. In fact one could create more than two stacks
        ## for items per character, but this generalization really seemed 
        ## unnecessary to me
            
        def getCarrying(self, char):
            self.checkBounds(char)
            return self.__carrying[char]
        def hasCarrying(self, char):
            return self.getCarrying(char) > 0
        def getCarryingD(self):
            return self.getCarrying(Item.getDefaultChar())
        def hasCarryingD(self):
            return self.getCarryingD() > 0
        
        ## returns -1 if the change would go over limits,
        ## False if the new value would be negative and
        ## True if everything was alright
        def setCarrying(self, char, val):
            self.checkBounds(char)
            if not isinstance(val, int):
                raise TypeError("val must be an int!")
            if val < 0:
                return False
            if self.Limit != None:
                sum = 0
                for i in range(0, Item.getNumberOfCharacters()):
                    sum += self.getCarrying(i) + self.getStored(i)
                if sum + val > self.Limit:
                    return -1
            self.__carrying[char] = val
            return True
        
        ## same goes for addCarrying
        def addCarrying(self, char, val=1):
            return self.setCarrying(char, self.getCarrying(char) + val)
        def addCarryingD(self, val=1):
            return self.addCarrying(Item.getDefaultChar(), val)
        
        def getStored(self, char):
            self.checkBounds(char)
            return self.__stored[char]
        def hasStored(self, char):
            return self.getStored(char) > 0
        def getStoredD(self):
            return self.getStored(Item.getDefaultChar())
        def hasStoredD(self):
            return self.getStoredD() > 0
        
        ## returns -1 if the change would go over limits,
        ## False if the new value would be negative and
        ## True if everything was alright
        def setStored(self, char, val):
            self.checkBounds(char)
            if not isinstance(val, int):
                raise TypeError("val must be an int!")
            if val < 0:
                return False
            if self.Limit != None:
                sum = 0
                for i in range(0, Item.getNumberOfCharacters()):
                    sum += self.getCarrying(i) + self.getStored(i)
                if sum + val > self.Limit:
                    return -1
            self.__stored[char] = val
            return True
        
        ## same goes for addStored
        def addStored(self, char, val=1):
            return self.setStored(char, self.getStored(char) + val)
        def addStoredD(self, val=1):
            return self.addStored(Item.getDefaultChar(), val)
        
        ## simple checks if items are available for characters
        def hasWith(self, char):
            return self.getCarrying(char) > 0
        def hasWithD(self):
            return self.hasWith(Item.getDefaultChar())
        def hasStored(self, char):
            return self.getStored(char) > 0
        def hasStoredD(self):
            return self.hasStored(Item.getDefaultChar())
        def has(self, char):
            return self.hasWith(char) or self.hasStored(char)
        def hasD(self):
            return self.has(Item.getDefaultChar())
            
        ## returns an array with all characters who have this item
        ## if that is known, one can check by oneself if it is
        ## carried around or stored
        def ownedBy(self):
            allOwners = []
            for i in range(0, Item.getNumberOfCharacters()):
                if self.has(i):
                    allOwners.append(i)
            return allOwners

        ## returns False if the number of items to store were impossible
        ## and True if everything was alright
        def store(self, char, howMany):
            if not isinstance(howMany, int):
                raise TypeError("howMany must be an int!")
            if howMany < 0 or howMany > self.getCarrying(char):
                return False
            self.addCarrying(char, -howMany)
            self.addStored(char, howMany)
            return True
        def storeD(self, howMany):
            return self.store(Item.getDefaultChar(), howMany)
            
        ## returns False if the number of items to store were impossible
        ## and True if everything was alright
        def take(self, char, howMany):
            if not isinstance(howMany, int):
                raise TypeError("howMany must be an int!")
            if howMany < 0 or howMany > self.getStored(char):
                return False
            self.addStored(char, -howMany)
            self.addCarrying(char, howMany)
            return True
        def takeD(self, howMany):
            return self.take(Item.getDefaultChar(), howMany)
            
        ## returns True if gifting was possible,
        ## else False
        def give(self, char1, char2, stored1 = False, stored2 = False):
            if not (isinstance(stored1, bool) and isinstance(stored2, bool)):
                raise TypeError("stored1/2 must be boolean!")
            if stored1:
                if self.addStored(char1, -1) == False:
                    return False
            else:
                if self.addCarrying(char1, -1) == False:
                    return False
            if stored2:
                if self.addStored(char2, 1) == False:
                    return False
            else:
                if self.addCarrying(char2, 1) == False:
                    return False
            return True
