###
# 
# Here we place certain events.
#
###
    
init python:

    def sumArrayOverDays(array, dayRange = None):
        global day, MAX_DAYS
        if dayRange == None:
            dayRange = MAX_DAYS
        sum = 0
        start = day - dayRange
        if start < 0:
            start = 0
        for i in range(start,day+1):
            sum = sum + array[i]
        return sum
        
    def showStats():
        return (not (introRunning or endingRunning or ( 
            creditsRunning or isSleeping))) and (
            date == None)
        
    def canSave():
        return not (introRunning or endingRunning)
    
    def moneyString(money):
        return "" + str(money / 200) + " Gp " + str(
            (money%200)/10) + " Sp " + str(money % 10) + " Cp"
    
    def moneyStringShort(money):
        result = "";
        gp = money/200;
        if gp != 0:
            result += str(gp) + " Gp"
        sp = (money%200)/10
        if sp != 0:
            if gp != 0:
                result += " "
            result += str(sp) + " Sp"
        cp = money % 10
        if cp != 0:
            if sp != 0 or (sp == 0 and gp != 0):
                result += " "
            result += str(cp) + " Cp"
        return result
        
    def nextDay(gameCanEnd = True):
        global day, MAX_DAYS, isSleeping, BATTLE_HP_INCREASE
        for i in range(0, len(dcharlist)):
            SIA.getRel(i).increaseCorruptionPoints(-50)
            SIA.getRel(i).resetKissedToday()
            SIA.getRel(i).resetPhonedToday()
            dcharlist[i].restoreHP()
            dcharlist[i].restoreBattleHP()
        day = day + 1
        isSleeping = False
        if gameCanEnd == True and day > MAX_DAYS:
            renpy.jump('ending')
            
    def sleepGood():
        global isSleeping
        Prota("Time to got to bed!")
        isSleeping = True ## to fade out status bar
        renpy.transition(fade)
        renpy.show("black")
        Prota("Zzzzz... Zzzzz...")
        prota.restoreHP()
        renpy.transition(fade)
        renpy.hide("black")
        Prota("Ahhh, what a nice sleep!")
        nextDay(True)
        
    def sleepBad():
        global isSleeping
        Prota("Seems I have to sleep {i}here{/i}...")
        isSleeping = True ## to fade out status bar
        renpy.transition(fade)
        renpy.show("black")
        Prota("Zzz... My back... Zzz...")
        prota.restoreHP(10)
        renpy.transition(fade)
        renpy.hide("black")
        Prota("Urgh, what a terrible night...")
        nextDay(True)
        
    def goStairs():
        global eStairs
        eStairs += 1
        if eStairs > 0 and (eStairs) % 50 == 0:
            Prota("Oh My God SO MANY STAIRS!")
            Prota("I'd like to find the guy who invented the stairs and push him down THESE stairs just to show him how stupid stairs are.")
            Prota("And then his legs will be broken and he will no longer be able to climb the stairs anymore.")
            Prota("It'll be ironic and then his wife will leave him and go be with the man who invented the elevator because everybody knows that elevators are much sexier than stairs.")
            prota.raiseStat(STAT_STRENGTH, 1)
            narrator("Your strength got raised by 1!")
        return
            
    def normalKiss():
        narrator("*smotches*")

    def friendlyKiss():
        narrator("You kiss each other on the cheek.")
            
