###
# Data of Erin, mostly her lines. 
### 

init -4 python:
    
    iC = CHAR_ERIN
            
    
    ##########
    ## casual talking
    ##########
    
    
    linesTalking[iC][MS_STRANGER] += [
        "Sorry, lots of customers here. I'll be with you in a minute!"]
    
    linesTalking[iC][MS_NEW_FRIEND] += [
        ("Nice to see you around!", "happy")]
        
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Hey! Nice day today, isn't it?", "happy")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Would you like to have a learn session together?", "smile")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Do you know the Riemann hypothesis?", "curious")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        "I appreciate classic music."]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        "As my hair indicates, violet is my favourite color."]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        "I like Siberian tigers. They are graceful, strong and exotic. A perfect combination."]
        
    linesTalking[iC][MS_CLOSE_FRIEND] += linesTalking[iC][MS_GOOD_FRIEND]
    linesTalking[iC][MS_CLOSE_FRIEND] += [[
        ("Please tell me when I talk to much.","serious"),
        ("I've read that open communication is the key to a healthy relationship.", "smile")]]
    linesTalking[iC][MS_CLOSE_FRIEND] += [[
        ("Want in on a secret?", "excited"),
        ("I like to eat hamburgers, even though its fast food...", "embarrassed"),
        ("...", "smile")]]
    
    linesTalking[iC][MS_BOYFRIEND] += [[
        ("I'll spare you the embarrassment of asking, so consider the follwing information a favour.", "serious"),
        ("I'm still a fair maiden...", "embarrassed")]]
    linesTalking[iC][MS_BOYFRIEND] += [
        ("I don't know what I should tell my parents...", "nervous")]
    linesTalking[iC][MS_BOYFRIEND] += [
        ("Want to go camping sometime? Just you and me, alone together in the forest", "flirty")]
    
    linesTalking[iC][MS_LOVER] += linesTalking[iC][MS_BOYFRIEND]
    linesTalking[iC][MS_LOVER] += [
        ("I would really appreciate you coming over tonight...", "flirty")]
        
    ## we don't want this line after they became lovers
    linesTalking[iC][MS_BOYFRIEND] += [
        ("I don't know if I'm ready to do {i}it{/i}", "embarrassed")]
        
    linesTalking[iC][MS_BOYTOY] += [
        ("I really need a book about functional analysis.", "serious")]
    linesTalking[iC][MS_BOYTOY] += [
        ("I don't supposed you could pay someone to write an explanation of Wiles' proof of Fermat's last theorem?", "curious")]
    
    linesTalking[iC][MS_SEX_FRIEND] += [
        ("Fancy fornication?", "embarrassed")]
    linesTalking[iC][MS_SEX_FRIEND] += [[
        ("According to my resources, the amount of our bed time is too damn low!", "serious"),
        ("...", "embarrassed")]]
    
    linesTalking[iC][MS_BFF] += [[
        ("Let me tell you about that amazing proof I read today!", "happy"),
        ("It uses something called the diagonal argument. First, let x be a sequence...", "happy")]]
    linesTalking[iC][MS_BFF] += [[
        ("I just talked to my parents over the phone, and I don't think I do them justice...", "sad"),
        ("Blah blah blah blah...", "cry")]]

    linesTalking[iC][MS_IDIOT] += [
        ("I don't have time for you.", "annoyed")]
    linesTalking[iC][MS_IDIOT] += [
        ("...", "annoyed")]
        
    linesTalking[iC][MS_JERK] += linesTalking[iC][MS_IDIOT]
    linesTalking[iC][MS_JERK] += [
        ("Shouldn't you be studying, considering your grades?", "serious")]
        
    linesTalking[iC][MS_CREEP] += [
        ("...", "angry")]
    linesTalking[iC][MS_CREEP] += [
        ("Stop following me around!", "angry")]
        
    linesTalking[iC][MS_ENEMY] += linesTalking[iC][MS_CREEP] 
    linesTalking[iC][MS_ENEMY] += [
        ("Get out of my way, sleezebag!", "angry")]
        
    linesTalking[iC][MS_ARCH_ENEMY] += [
        ("...", "grim")]
    linesTalking[iC][MS_ARCH_ENEMY] += [
        ("I can see why your parents wouldn't love you.", "serious")]
    linesTalking[iC][MS_ENEMY] += [
        ("Why do you study anyway? You will just fail, you know.", "serious")]
            
        
    ##########
    ## questions
    ##########
        
        
    linesAsking[iC][MS_GOOD_FRIEND] += [[ 
        "What kind of music do you think I like?", [
            ("Death Metal", AL_VERY_WRONG),
            ("Techno", AL_WRONG),  
            ("Classic", AL_RIGHT),
            ("Swing", AL_ALMOST_RIGHT)
        ]]]
    linesAsking[iC][MS_GOOD_FRIEND] += [[ 
        "Surely you memorized my favourite color?", [
            ("Violet", AL_RIGHT), 
            ("Orange", AL_VERY_WRONG),
            ("Black", AL_WRONG), 
            ("Blue", AL_ALMOST_RIGHT)
        ]]]
    linesAsking[iC][MS_GOOD_FRIEND] += [[
        "This animal is really fascinating...", [
            ("Grizzly bear", AL_ALMOST_RIGHT),
            ("Oak spider", AL_VERY_WRONG),  
            ("White horse", AL_WRONG),
            ("Siberian tiger", AL_RIGHT) 
        ]]]
        
    linesAsking[iC][MS_CLOSE_FRIEND] += linesAsking[iC][MS_GOOD_FRIEND]
    
    linesAsking[iC][MS_CLOSE_FRIEND] += [[
        "I secretly crave...?", [ 
            ("Love", AL_WRONG), 
            ("The respect of your parents", AL_ALMOST_RIGHT),
            ("The sweet release of death", AL_VERY_WRONG),
            ("Hamburgers", AL_RIGHT)
        ]]]
        
        
    ##########
    ## other things
    ##########
        
        
    linesAnswerReaction[iC][AL_VERY_WRONG] = [
        ("Wha-?!", "shock"),
        ("I mean: No, that is wrong.", "smile"),
        ("...","angry")]
    linesAnswerReaction[iC][AL_WRONG] = [("No, that is wrong.", "smile"), ("...","sad")]
    linesAnswerReaction[iC][AL_ALMOST_RIGHT] = ("Well, if I were to change the definitions a bit, it could be right...", "curious")
    linesAnswerReaction[iC][AL_RIGHT] = ("That is correct.", "happy")
    
    linesNoQuestions[iC] = ("I don't have time for more questioning.", "annoyed")
    
    ## these are lines spoken when the leveling happens through a question
    linesNextMilestoneReady[iC][MS_STRANGER] = [
        ("Since I'm mature, I'll forgive your past offences.", "annoyed")]
    linesNextMilestoneReady[iC][MS_NEW_FRIEND] = [
        ("Well, if you insist, I might be able to find time to chat once in a while.", "annoyed")]
    linesNextMilestoneReady[iC][MS_GOOD_FRIEND] = [
        ("I... see potential for our friendship.", "smile")]
    linesNextMilestoneReady[iC][MS_CLOSE_FRIEND] = [
        ("You seem to be someone I can trust.", "smile")]
    linesNextMilestoneReady[iC][MS_BOYFRIEND] = [
        ("I feel like... like I would rather spend time with you than to study...", "embarrassed")]
    linesNextMilestoneReady[iC][MS_LOVER] = [
        ("I-I-I think I'm ready... For the next step...", "embarrassed")]
    linesNextMilestoneReady[iC][MS_BOYTOY] = [
        ("A stipend doesn't pay everything and there are quite a few books I would like to own.", "smile")]
    linesNextMilestoneReady[iC][MS_SEX_FRIEND] = [
        ("I have read about very... physical relationships that don't involve a... emotional component...", "nervous")]
    linesNextMilestoneReady[iC][MS_BFF] = [
        ("Can you even begin to image what I must feel like?", "angry")]
        
    ## these are the answers
    linesNextMilestoneAccomplished[iC][MS_STRANGER] = [
        "Be on your best behaviour from now on."]
    linesNextMilestoneAccomplished[iC][MS_NEW_FRIEND] = [
        "My name is Juan Lee. Remember it."]
    linesNextMilestoneAccomplished[iC][MS_GOOD_FRIEND] = [[
        ("Here is my number...", "nervous"), 
        ("But don't call during my lectures or study time!", "annoyed")]]
    linesNextMilestoneAccomplished[iC][MS_CLOSE_FRIEND] = [
        "I was born on the 24th day of October."]
    linesNextMilestoneAccomplished[iC][MS_BOYFRIEND] = [
        ("Yesiwouldliketogooutwithyou!", "embarrassed")]
    linesNextMilestoneAccomplished[iC][MS_LOVER] = [
        ("Please... be gentle...", "embarrassed")]
    linesNextMilestoneAccomplished[iC][MS_BOYTOY] = [
        ("Hm... Is your memory good enough to remember them all or should I write a list?", "curious")]
    linesNextMilestoneAccomplished[iC][MS_SEX_FRIEND] = [
        ("To think my first time would be in such an arrangement is so... unorthodox... What would my parents think?", "nervous")]
    linesNextMilestoneAccomplished[iC][MS_BFF] = [
        ("Finally I can tell someone about the pressure I feel!!", "happy")]
        
    linesNotEnoughHP[iC] = ("Your stamina seems depleted, I recommend a night of sleep.", "serious") 
    linesNotEnoughHP2[iC] = ("No time, need to sleep...", "tired") 
    
    linesNoGiftTaken[iC] = ("For your information, I have a stipend and don't need your handouts.", "serious")
    linesNoGiftGiven[iC] = ("Please don't waste my time, there is studying to do.", "serious")
    linesAcceptGifts[iC] = ("I suppose I can accept your gift, whatever it is.", "smile")
    
    linesGifting[iC][GIFT_DERP] = [
        ("On second thought...", "annoyed")]
    linesGifting[iC][GIFT_SMALL] = [
        ("Thank you for your consideration.", "smile")]
    linesGifting[iC][GIFT_MEDIUM] = [[
        ("Oh, you shouldn't have.", "happy"),
        ("I'll take it anyway.", "wink")]]
    linesGifting[iC][GIFT_LARGE] = [[
        ("That is... rather unexpected.", "surprised"),
        ("I'm afraid I don't have anything to match your generousity...", "nervous"),
        ("...", "happy")]]
    linesGifting[iC][GIFT_SUPERB] = [[
        ("...", "shocked"),
        ("...", "surprised"),
        ("...", "happy"),
        ("...", "nervous"),
        ("Sorry, I'm just... speechless...", "embarrassed"),
        ("...", "embarrassed"),
        ("...", "happy")]]
        
    linesBattleAccepted[iC] = ("I will defend myself, you know?", "serious")
    linesBattleDeclined[iC] = "Do I look like I'm ready to rumble?"
    linesBattleWon[iC] = ("Ha! Memorize this, you wuss!", "laugh")
    linesBattleLost[iC] = ("Just stop hitting me, will you?", "cry")
    linesBattleTie[iC] = ("Well. This was an experience.", "serious")
    
    linesNoKissYet[iC] = ("How DARE you?", "angry")
    linesNoKissNow[iC] = ("Maybe later.", "annoyed")
    
    linesDateDeclined[iC] = ("Sorry, but I have to study.", "serious")
    linesDateAccepted[iC] = ("I suppose a change in scenery might help me to loose some tension.", "curious")
    linesDateExhausted[iC] = ("I think you currently lack the energy.", "serious")
    linesDateExpired[iC] = ("The exams are up, so... no.", "serious")
    linesDateEnoughTalk[iC] = "Why don't we enjoy the scenery for a minute?"
    linesDateEnoughQuestions[iC] = ("We've tested your memorization skills enough.", "serious")
    linesDateEnoughGifts[iC] = ("Don't overdo it, okay?", "annoyed")
    linesDateNoPhotoYet[iC] = ("I don't think a photo would be appropriate right now.", "annoyed")
    linesDatePhotoSuccess[iC] = ("Oh, you captured me really good!", "happy")
    linesDateEnoughPhotos[iC] = ("Too many photos will make each single one less great, I think.", "curious")
    linesDateNoFirstKiss[iC] = linesNoKissYet[iC]
    linesDateNoKiss[iC] = linesNoKissNow[iC]
    
    ## please note that they just appear in the room, so
    ## specifying girl and position is necessary
    linesRoomNoEntry[iC] = (iC, "What... Have you moved ANYTHING?!", "angry", [right])
    linesRoomBadSleep[iC] = [("It appears you stumbled into the wrong room.", "serious"), ("Get out. NOW!", "angry")]
        
        
    ##########
    ## gifting values
    ## (all are initialized with GIFT_DERP)
    ##########
        
    
    #dcharGiftEffect[iC][ITEM_POKEBALL] = GIFT_SMALL
        
        
    ##########
    ## date location values
    ## (all are initialized with 0.5 and should stay between 0.0 and 1.0)
    ##########
