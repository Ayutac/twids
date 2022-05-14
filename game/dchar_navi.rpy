###
# Navigation of the dateable characters 
# Created on 16.10.2012 by Sebastian Koch
### 

## dchar is short for dateable character
### A reminder of the string arrays:
# linesTalking[dchar][milestone][random line]
# linesAsking[dchar][milestone][random question][1 = question]/[2][(possible answers, points)] ## no sayDialogInputs
# linesAnswerReaction[dchar][answerValue] ## value between 0 and 3 inclusive
# linesNextMilestoneReady[dchar][toNewState] ## from New Friend to Lover
# linesNextMilestoneAccomplished[dchar][toWhatState] ## from New Friend to BFF
# linesNotEnoughHP[dchar]
# lines|NoGiftTaken, NoGiftGiven, AcceptGifts[dchar]
# linesGifting[dchar][giftValue] ## value between 0 and 4 inclusive
# lines|BattleAccepted, BattleDeclined, BattleWon, BattleLost, BattleTie[dchar]
# lines|NoKissYet, NoKissNow, DateDeclined, DateAccepted[dchar]
# linesDateEnough|Talk, Questions, Gifts, Photos[dchar]
# linesDate|NoPhotoYet, PhotoSuccess, NoFirstKiss, NoKiss[dchar]
# the elements of the respective arrays are things to be said by sayDialog in adse_char_data.rpy
###

label endMeeting:
    $ resultVal = dchar
    $ dchar = CHAR_NONE
    $ CIQ = None
    $ RIQ = None
    $ date = None
    $ invMode = INV_TO_USE
    if location == LOC_DORM:
        $ sayDialog((resultVal, "Okay, bye!"))
    jump worldReturn

label meetMisty:
    $ dchar = CHAR_MISTY
    jump meetDchar

label meetSapphire:
    $ dchar = CHAR_SAPPHIRE
    jump meetDchar

label meetIris:
    $ dchar = CHAR_IRIS
    jump meetDchar

label meetCynthia:
    $ dchar = CHAR_CYNTHIA
    jump meetDchar

label meetJoy:
    $ dchar = CHAR_JOY
    jump meetDchar

label meetJenny:
    $ dchar = CHAR_JENNY
    jump meetDchar

#label meetChuu:
#    $ dchar = CHAR_CHUU
#    jump meetDchar


label meetDchar:
    $ date = None ## if attempt to date did not succeed
    $ CIQ = dcharlist[dchar] ## short for "(dateable) character in question"
    $ RIQ = SIA.getRel(dchar) ## short for "relation in question"
    $ invMode = INV_TO_GIFT ## for proper inventory use
    $ renpy.show(CIQ.Name.lower(), at_list=[right])
    
    if RIQ.Exp < 0:
        $ RIQ.levelUp()
    if RIQ.hasChanged() == True:
        if RIQ.Milestone > MS_STRANGER:
            $ CIQ.meet()
        if RIQ.Milestone in range(MS_BOYFRIEND, MS_LOVER+1):
            $ renpy.show(CIQ.Name.lower() + " flirty")
        "Congratulation, now you are [CIQ.ShortDisplayNameS] [RIQ.MilestoneName]!"            
    if RIQ.Milestone == MS_LOVER and inventory[LEN_ITEM-ITEMS_FOR_EACH_GIRL*LEN_CHAR_GIRLS+dchar].hasWith(dchar):
        Dcharlist[dchar] "Here is the spare key for my apartment."
        $ renpy.show(CIQ.Name.lower() + " wink")
        "She winks at you."
        $ inventory[LEN_ITEM-ITEMS_FOR_EACH_GIRL*LEN_CHAR_GIRLS+dchar].give(dchar, CHAR_PROTA)

    $ renpy.show(CIQ.Name.lower())
                                                     
    menu:
        Prota "How should I approach [CIQ.PronounG]?"
        
        "speak (20 HP)":
            call speakDchar
        
        "ask (10 HP?)":
            call askDchar
        
        "battle (10 HP)":
            call battleDchar
        
        "give a gift... (5 HP)":
            call giftDchar
            
        "kiss (5 HP)":
            call kissDchar
        
        "date...":
            jump dateDchar
            
        "leave":
            jump endMeeting

    jump meetDchar
    

label speakDchar:
    python:
        resultVal = SIA.talk(dchar) ## raises exp if possible
        if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
             sayDialog(linesNotEnoughHP[dchar])
        elif resultVal == ERR_CHAR2_NOT_ENOUGH_HP: ## not enough HP in dateable character left
             sayDialog(linesNotEnoughHP2[dchar])
        elif resultVal == True:
            milestone = RIQ.getMilestone();
        
            ## speaking depends on milestones
            levelUpLine = False;
            for i in range(MS_FIRST_NON_BAD, MS_LAST_NORMAL_GOOD):
                if milestone == i and RIQ.getMilestoneForExp() > i:
                    levelUpLine = True
            if levelUpLine:
                 sayDialog(linesNextMilestoneReady[dchar][milestone+1])
            else:
                sayDialog(linesTalking[dchar][milestone][
                    random.randint(0, len(linesTalking[dchar][milestone])-1)])
                ## this one lets the dchar-th dateable character say something randomly chosen,
                ## on the basis on the other self and his/her milestone
    return
    
    
label askDchar:
    python:
        if RIQ.levelUp() == True: ## levels dateable character up if possible
            sayDialog(linesNextMilestoneAccomplished[dchar][RIQ.Milestone])
            renpy.return_statement()
        resultVal = SIA.question(dchar)
        if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
            sayDialog(linesNotEnoughHP[dchar])
            renpy.return_statement()
        elif resultVal == ERR_CHAR2_NOT_ENOUGH_HP: ## not enough HP in dateable character left
            sayDialog(linesNotEnoughHP2[dchar])
            renpy.return_statement()
        if resultVal == False or ( ## no questions allowed or
            len(linesAsking[dchar][RIQ.Milestone]) == 0): ## no questions written
            sayDialog(linesNoQuestions[dchar])
            renpy.return_statement()
        rnd = random.randint(0, len(linesAsking[dchar][RIQ.Milestone])-1)
        ## because of the choice menu, we don't use sayDialog here
        Dcharlist[dchar](linesAsking[dchar][RIQ.Milestone][rnd][0], interact = False)
        resultVal = menu(linesAsking[dchar][RIQ.Milestone][rnd][1])
        SIA.answer(dchar, resultVal)
        sayDialog(linesAnswerReaction[dchar][resultVal])
    return


label battleDchar: 
    python:
        if prota.BattleHP == 0:
            Prota("I'm too exhausted.")
            renpy.return_statement()
        elif CIQ.BattleHP == 0:
            sayDialog(linesBattleDeclined[dchar])
            renpy.return_statement()
        battle = SIA.startBattle(dchar)
        if battle < 0: ## not enough HP
            sayDialog(linesNotEnoughHP[dchar])
            renpy.return_statement()
        #playMusic('trainer_appears_girl.ogg', 0)
        help = lastMusic
        sayDialog(linesBattleAccepted[dchar])
        
        #playMusic('battle.ogg', 0)
        resultVal = "continue"
        while not isinstance(resultVal, int):
            bo = []
            bo.append(("Brute", "br"))
            if prota.getStat(STAT_INTELLIGENCE) > 5:
                bo.append(("Feint", "fe"))
                bo.append(("Observe", "ob"))
            bo.append(("Focus", "foc"))
            bo.append(("Distract", "dis"))
            narrator("Choose your tactic.", interact = False)
            atk1 = menu(bo)
            atk2 = random.choice(["br","fe","ob","foc","dis"])
            resultVal = battle.turn(atk1, atk2)
            narrator("Your Battle HP: "+str(prota.BattleHP)+"\n"+CIQ.NameS+" Battle HP:    "+str(CIQ.BattleHP))
            
        if resultVal == 1:
            #playMusic('battle_win.ogg', 0, False) ## don't loop
            narrator("You won!")
            sayDialog(linesBattleLost[dchar])
        elif resultVal == -1:
            #playMusic('battle_lost.ogg', 0, False) ## don't loop
            narrator("You lost...")
            sayDialog(linesBattleWon[dchar])
        else:
            #playMusic('battle_lost.ogg', 0, False) ## don't loop
            narrator("You got a tie.")
            sayDialog(linesBattleTie[dchar])
        battle = None
        #playMusic(help, fullName = True)
    return


label giftDchar:
    python:
        resultVal = SIA.presentGift(dchar)
        if resultVal == -1:
            sayDialog(linesNotEnoughHP[dchar])
            renpy.return_statement()
        elif resultVal == -2: ## = not enough HP in dateable character left
            sayDialog(linesNotEnoughHP2[dchar])
            renpy.return_statement()
        Prota("I have a little present for you.")
        if resultVal == False: ## does not accept gifts
            sayDialog(linesNoGiftTaken[dchar])
            renpy.return_statement()
        sayDialog(linesAcceptGifts[dchar])
        ## returns from inventory with the chosen item in variable item
        if Item.hasItemsOfWith(CHAR_PROTA, inventory) > 0:
            renpy.call_screen('inventory')
            ## gives the exp and removes the gift from the player
            resultVal = SIA.giveGift(dchar, inventory[item], dcharGiftEffect[dchar][item])
        else: ## no inventory
            resultVal = False
        ## make reaction visible
        if resultVal == False:
            Prota("Actually, I have nothing for you...")
            sayDialog(linesNoGiftGiven[dchar])
        else:
            sayDialog(linesGifting[dchar][dcharGiftEffect[dchar][item]])
            if dcharGiftEffect[dchar][item] == GIFT_DERP or item == ITEM_FOREST_MAP:
                inventory[item].store(dchar, 1)
        item = ITEM_NONE
    return
    
    
label kissDchar:
    python:
        resultVal = SIA.kiss(dchar)
        if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
            sayDialog(linesNotEnoughHP[dchar])
        elif resultVal == ERR_CHAR2_NOT_ENOUGH_HP:
            sayDialog(linesNotEnoughHP2[dchar])
        elif resultVal == -3:
            sayDialog(linesNoKissNow[dchar])
        elif resultVal == True:
            if SIA.getRel(dchar).Milestone in range(MS_FIRST_SPECIAL_GOOD, MS_LAST_SPECIAL_GOOD+1):
                friendlyKiss()
            else:
                normalKiss()
        else:
            if RIQ.canKiss():
                sayDialog(linesNoKissNow[dchar])
            else:
                sayDialog(linesNoKissYet[dchar])
    return


label dateDchar:
    python:
        if RIQ.isGoingOnDates() == False:
            sayDialog(linesDateDeclined[dchar])
            renpy.jump('meetDchar')
        sayDialog(linesDateAccepted[dchar])
        dLD = dateLocationData
        
        ## now this looks more complicated than it is:
        dateChoiceSelection = []
        dateChoiceSelection.append(("shopping mall (" + str(dLD[DATE_LOC_SHOPPING_MALL][1]) + "HP, " +
            str(dLD[DATE_LOC_SHOPPING_MALL][2]) + " days, $ " + str(dLD[DATE_LOC_SHOPPING_MALL][3]) + ")", DATE_LOC_SHOPPING_MALL))
        if eSecretBeachDiscovered == False:
            dateChoiceSelection.append(("ONLY beach (" + str(dLD[DATE_LOC_BEACH_CASUAL][1]) + "HP, " +
                str(dLD[DATE_LOC_BEACH_CASUAL][2]) + " days, $ " + str(dLD[DATE_LOC_BEACH_CASUAL][3]) + ")", DATE_LOC_BEACH_CASUAL))
        else:
            dateChoiceSelection.append(("casual beach (" + str(dLD[DATE_LOC_BEACH_CASUAL][1]) + 
                "HP, " + str(dLD[DATE_LOC_BEACH_CASUAL][2]) + " days, $ " + str(dLD[DATE_LOC_BEACH_CASUAL][3]) + ")", DATE_LOC_BEACH_CASUAL))
            dateChoiceSelection.append(("secret beach (" + str(dLD[DATE_LOC_BEACH_SECRET][1]) + 
                "HP, " + str(dLD[DATE_LOC_BEACH_SECRET][2]) + " days, $ " + str(dLD[DATE_LOC_BEACH_SECRET][3]) + ")", DATE_LOC_BEACH_SECRET))
        dateChoiceSelection.append(("mountain (" + str(dLD[DATE_LOC_MOUNTAIN][1]) + "HP, " +
            str(dLD[DATE_LOC_MOUNTAIN][2]) + " days, $ " + str(dLD[DATE_LOC_MOUNTAIN][3]) + ")", DATE_LOC_MOUNTAIN))
        dateChoiceSelection.append(("forest (" + str(dLD[DATE_LOC_FOREST][1]) + "HP, " +
            str(dLD[DATE_LOC_FOREST][2]) + " days, $ " + str(dLD[DATE_LOC_FOREST][3]) + ")", DATE_LOC_FOREST))
        ## dateLocationData[locationNumber / 10 - 1][0][dcharNumber]
        narrator("Where do you want to go?", interact = False)
        ## but we are just building up the menu for the date selection, nothing to worry about
        ## however, new locations must be added here
        
        resultVal = menu(dateChoiceSelection)
        if resultVal == DATE_LOC_FOREST and not compass.hasWithD(): ## compass/forest cockblock
            narrator("Don't you think it would be a bad idea to go into the woods with a lady but no compass?")
            renpy.jump('meetDchar')
        date = SIA.startDate(dchar, DATE_LOC_LOCATION[resultVal], dLD[resultVal][1], dLD[resultVal][2], 
            dLD[resultVal][3], dLD[resultVal][0][dchar], occupied = tournamentDays[dchar])
        if date == ERR_CHAR1_NOT_ENOUGH_HP:
            sayDialog(linesDateExhausted[dchar])
            renpy.jump('meetDchar')
        if date == -5:
            sayDialog(linesDateExpired[dchar])
            renpy.jump('meetDchar')
        if isinstance(date, str):
            sayDialog(linesDateTournament[dchar])
            renpy.jump('meetDchar')
        if dLD[resultVal][2]+day == MAX_DAY:
            sayDialog(linesDateLastDay[dchar])
        if date == False:
            narrator("You can't pay for this date!")
            renpy.jump('meetDchar')
        if date.Location == DATE_LOC_SHOPPING_MALL:
            #playMusic('pewter_city.ogg')
            renpy.scene()
            renpy.transition(fade)
            renpy.show('bg shoppingMall')
        elif date.Location == DATE_LOC_BEACH_CASUAL:
            #playMusic('surfing.ogg')
            renpy.scene()
            renpy.transition(fade)
            renpy.show('bg beach')
        elif date.Location == DATE_LOC_BEACH_SECRET:
            #playMusic('surfing.ogg')
            renpy.scene()
            renpy.transition(fade)
            renpy.show('bg secretBeach')
        elif date.Location == DATE_LOC_MOUNTAIN:
            #playMusic('mt_moon.ogg')
            renpy.scene()
            renpy.transition(fade)
            renpy.show('bg mountain')
        elif date.Location == DATE_LOC_FOREST:
            #playMusic('viridian_forest.ogg')
            renpy.scene()
            renpy.transition(fade)
            renpy.show('bg forest2')
        renpy.jump('dateMain')
    jump meetDchar
    
    
label dateMain:
    $ renpy.show(CIQ.Name.lower(), at_list=[right]) 
    menu:
        "Mood: [date.Mood]"
        
        "speak":
            jump dateSpeak
        
        "ask":
            jump dateAsk
        
        "give a gift":
            jump dateGift
        
        "take a picture":
            jump datePhoto
        
        "kiss her":
            jump dateKiss
            
        "leave":
            jump dateEnd

    jump dateEnd


label dateSpeak:
    python:
        if date.speak() == False:
            sayDialog(linesDateEnoughTalk[dchar])
        else:
            sayDialog("Nice weather we're having today...")
    jump dateMain


label dateAsk:
    python:
        resultVal = date.question()
        if resultVal == False:
            sayDialog(linesDateEnoughQuestions[dchar])
            renpy.jump('dateMain')
        resultVal = 3 ## for now, we take the close friend questions
        if len(linesAsking[dchar][resultVal]) == 0:
            sayDialog(linesDateEnoughQuestions[dchar])
            renpy.jump('dateMain')
        rnd = random.randint(0, len(linesAsking[dchar][resultVal])-1)
        sayDialog(linesAsking[dchar][resultVal][rnd][0], interact = False)
        resultVal = menu(linesAsking[dchar][resultVal][rnd][1])
        date.answer(resultVal)
        sayDialog(linesAnswerReaction[dchar][resultVal])
    jump dateMain

    
label dateGift:
    python:
        resultVal = date.presentGift()
        if resultVal == False:
            sayDialog(linesDateEnoughGifts[dchar])
            renpy.jump('dateMain')
        renpy.call_screen('inventory')
        ## returns from inventory with the chosen item in variable item
        renpy.call_screen('inventory')
        ## gives the exp and removes the gift from the player
        resultVal = date.giveGift(inventory[item], dcharGiftEffect[dchar][item]) 
        ## make reaction visible
        if resultVal == False:
            sayDialog(linesNoGiftGiven[dchar])
        elif resultVal >= 0 and resultVal <= 4:
            sayDialog(linesGifting[dchar][resultVal])
        sayDialog(linesGifting[dchar][resultVal])
    jump dateMain


label datePhoto:
    python:
        resultVal = date.photo()
        if resultVal == -1:
            sayDialog(linesDateNoPhotoYet[dchar])
        elif resultVal == True:
            sayDialog(linesDatePhotoSuccess[dchar])
        elif resultVal == False:
            sayDialog(linesDateEnoughPhotos[dchar])
    jump dateMain


label dateKiss:
    python:
        if date.kiss() == True:
            normalKiss()
            renpy.jump('dateEnd')
        else:
            if SIA.getRel(dchar).canKiss() == True:
                sayDialog(linesDateNoKiss[dchar])
            else:
                sayDialog(linesDateNoFirstKiss[dchar])
    jump dateMain


label dateEnd:
    python:
        resultVal = date.finish()
        date = None
        renpy.scene()
        renpy.transition(fade)
        if resultVal == True: ## ended with kiss
            if location == 15:
                #playMusic('pewter_city.ogg')
                renpy.show('bg shoppingMall')
            elif location == 20:
                #playMusic('surfing.ogg')
                renpy.show('bg beach')
            elif location == 30:
                #playMusic('surfing.ogg')
                renpy.show('bg secretBeach')
            elif location == 40:
                #playMusic('mt_moon.ogg')
                renpy.show('bg mountain')
            elif location == 50:
                #playMusic('viridian_forest.ogg')
                renpy.show('bg forest2')
            renpy.show(CIQ.Name.lower(), at_list=[right])
            sayDialog("This was a lot of fun, let's do that sometime again!")
            Prota("Sure!")
            narrator("[CIQ.PronounC] smiles at you.")
            renpy.jump('meetDchar')
        else: ## ended with Prota leaving
            #playMusic('pewter_city.ogg')
            renpy.show('bg apartment')
            Prota("Damn, I blew it...")
            renpy.jump('apartment')
    
    
## please note the labels below do not require the dateable character to be present,
## thus CIQ is not used


label callDchar:
    python:
        callDcharChoiceSelection = []
        callDcharChoiceSelection.append(("nobody", CHAR_NONE))
        for i in range(0, len(dcharlist)):
            if SIA.getRel(i).canBePhoned(): # strangers can't be phoned
                callDcharChoiceSelection.append((dcharlist[i].Name, i))
        Prota("Who should I call?", interact = False)
        resultVal = menu(callDcharChoiceSelection)
        if resultVal == CHAR_NONE:
            narrator("You call nobody...")
            narrator("'cause you have no friends!")
        else:
            sDcharname = dcharlist[resultVal].Name
            resultVal = SIA.phone(i, 
                int(renpy.input("How much time (HP) to spend? (1-50)"))
                )
            if resultVal == False:
                narrator("[sDcharname] rejected the call.")
            elif resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                narrator("You can't spend this amount of HP!")
            elif resultVal == ERR_CHAR2_NOT_ENOUGH_HP:
                narrator("[sDcharname] hadn't time for you!")
            elif resultVal == 0:
                narrator("You and [sDcharname] talked over the phone, but she " +
                    "ended the call earlier than you anticipated.")
            elif resultVal == True:
                narrator("[sDcharname] and you have a nice talk over the phone. "
                    + "You feel your relationship increased.")
    jump apartment
