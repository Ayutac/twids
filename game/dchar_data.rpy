###
# Data of the dchars, mostly their lines. 
### 

init python:

    ## says different expressions, including a list of those
    ## however, lists can't be recursive, that's what control is for
    def sayDialog(what, control = None, interact = True):
        global dchar
        if isinstance(what, str) or isinstance(what, unicode):
            ## "text"
            ## one simple text line, will be spoken by the active dchar
            Dcharlist[dchar](what, interact = interact)
            return
        if isinstance(what, tuple):
            if len(what) == 1:
                if isinstance(what[0], str) or isinstance(what[0], unicode):
                    ## ("text")
                    ## one simple text line, will be spoken by the active dchar
                    Dcharlist[dchar](what[0], interact = interact)
                    return
            if len(what) == 2:
                if isinstance(what[1], str) or isinstance(what[1], unicode):
                    if isinstance(what[0], int):
                        ## (index, "text")
                        ## indexed character will speak text
                        Charlist[what[0]](what[1], interact = interact)
                        return
                    if isinstance(what[0], str) or isinstance(what[0], unicode):
                        ## ("text", "emotion")
                        ## let the current dchar say text with a given expression
                        renpy.show(dcharlist[dchar].Name.lower() + " " + what[1])
                        Dcharlist[dchar](what[0], interact = interact)
                        return
            if len(what) == 3:
                if isinstance(what[0], int) and ( 
                    isinstance(what[1], str) or isinstance(what[1], unicode)) and (
                    isinstance(what[2], str) or isinstance(what[2], unicode)):
                    ## (index, "text", "emotion")
                    ## let the indexed character say text with emotion
                    renpy.show(charlist[what[0]].Name.lower() + " " + what[2])
                    Charlist[what[0]](what[1], interact = interact)
                    return
            if len(what) == 4:
                if isinstance(what[0], int) and ( 
                    isinstance(what[1], str) or isinstance(what[1], unicode)) and (
                    isinstance(what[2], str) or isinstance(what[2], unicode)) and (
                    isinstance(what[3], list) or isinstance(what[3], renpy.python.RevertableList)):
                    ## (index, "text", "emotion", [direction, ...])
                    ## let the indexed character say text with emotion on position
                    renpy.show(charlist[what[0]].Name.lower() + " " + what[2], at_list=what[3])
                    Charlist[what[0]](what[1], interact = interact)
                    return
        if (isinstance(what, list) or
            isinstance(what, renpy.python.RevertableList)) and control == None:
            for element in what:
                sayDialog(element, control = 0) ## ignores interact
            return
        raise ArgumentError("Dialog is messed up!")


init -5 python:
    

    linesTalking = []
    linesAsking = []
    linesNextMilestoneReady = []
    linesNextMilestoneAccomplished = []
    
    linesAnswerReaction = []
    
    linesNoQuestions = []
    linesNotEnoughHP = []
    linesNotEnoughHP2 = []
    linesNoGiftTaken = []
    linesNoGiftGiven = []
    linesAcceptGifts = []
    linesCheeredOn = []
    
    linesGifting = []
    
    linesBattleAccepted = []
    linesBattleDeclined = []
    linesBattleWon = []
    linesBattleLost = []
    linesBattleTie = []
    
    linesNoKissYet = []
    linesNoKissNow = []
    linesDateDeclined = []
    linesDateAccepted = []
    linesDateExhausted = []
    linesDateExpired = []
    linesDateEnoughTalk = []
    linesDateEnoughQuestions = []
    linesDateEnoughGifts = []
    linesDateNoPhotoYet = []
    linesDatePhotoSuccess = []
    linesDateEnoughPhotos = []
    linesDateNoFirstKiss = []
    linesDateNoKiss = []
    linesDateTournament = []
    linesDateLastDay = []
    
    linesRoomNoEntry = []
    linesRoomBadSleep = []
    
    tournamentDays = []
    roomAvailability = []
    
    for i in range(LEN_CHAR_DCHARS): ## all dchars
        
        linesTalking += [[]]
        linesAsking += [[]]
        linesNextMilestoneReady += [[]]
        linesNextMilestoneAccomplished += [[]]
        for j in range(LEN_MS): ## all milestones
            linesTalking[i] += [[]]
            linesAsking[i] += [[]]
            linesNextMilestoneReady[i] += [None]
            linesNextMilestoneAccomplished[i] += [None]
        
        linesAnswerReaction += [[]]
        for j in range(LEN_AL): ## all answer levels
            linesAnswerReaction[i] += [None]
        
        linesNoQuestions += [None]
        linesNotEnoughHP += [None]
        linesNotEnoughHP2 += [None]
        linesNoGiftTaken += [None]
        linesNoGiftGiven += [None]
        linesAcceptGifts += [None]
        linesCheeredOn += [None]
        
        linesGifting += [[]]
        for j in range(LEN_GIFT): ## all gift levels
            linesGifting[i] += [None]
        
        linesBattleAccepted += [None]
        linesBattleDeclined += [None]
        linesBattleWon += [None]
        linesBattleLost += [None]
        linesBattleTie += [None]
        linesNoKissYet += [None]
        linesNoKissNow += [None]
        linesDateDeclined += [None]
        linesDateAccepted += [None]
        linesDateExhausted += [None]
        linesDateExpired += [None]
        linesDateEnoughTalk += [None]
        linesDateEnoughQuestions += [None]
        linesDateEnoughGifts += [None]
        linesDateNoPhotoYet += [None]
        linesDatePhotoSuccess += [None]
        linesDateEnoughPhotos += [None]
        linesDateNoFirstKiss += [None]
        linesDateNoKiss += [None]
        linesDateTournament += [None]
        linesDateLastDay += [None]
        
        linesRoomNoEntry += [None]
        linesRoomBadSleep += [None]
        
        tournamentDays += [[]]
        roomAvailability += [[]]
        
    dcharGiftEffect = []
    for i in range(LEN_CHAR_DCHARS):
        dcharGiftEffect += [[]]
        for j in range(LEN_ITEM):
            dcharGiftEffect[i] += [GIFT_DERP]
    
    ## tells the start mood of a dateable character , min. HP, days to stay and costs
    ## for a dating location
    
    dateLocationData = [
        [ ## shopping mall
            [], ## impact on dateable characters ## done in each dchar file
            80, ## minimum HP to go
            1, ## days to stay
            100 ## money costs
        ],
        [ ## beach
            [], ## impact on dchars
            100, ## minimum HP to go
            2, ## days to stay
            200 ## money costs
        ],
        [ ## secret beach
            [], ## impact on dchars
            150, ## minimum HP to go
            3, ## days to stay
            400 ## money costs
        ],
        [ ## mountain (volcano)
            [], ## impact on dchars
            110, ## minimum HP to go
            2, ## days to stay
            200 ## money costs
        ],
        [ ## forest
            [], ## impact on dchars
            130, ## minimum HP to go
            3, ## days to stay
            300 ## money costs
        ]
    ]
    
    for i in range(0, LEN_DATE_LOC):
        for j in range(0, LEN_CHAR_DCHARS):
            dateLocationData[i][0] += [0.5] 