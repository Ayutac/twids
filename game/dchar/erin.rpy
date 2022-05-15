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
    linesTalking[iC][MS_STRANGER] += [
        ("Hey! You there! Have you read the sign? If you're not cool with eating with Goblins, the door is over there.", "angry")]
    linesTalking[iC][MS_STRANGER] += [
        ("Hold on, Lyonette! Can you get this guy's order?", "tired")]
    linesTalking[iC][MS_STRANGER] += [
        "Hi! Just seat yourself wherever you want."]        
 
    linesTalking[iC][MS_NEW_FRIEND] += [
        ("Nice to see you around!", "happy")]
    linesTalking[iC][MS_NEW_FRIEND] += [
        ("Heeeey! You're here again!", "happy")]       
    linesTalking[iC][MS_NEW_FRIEND] += [
        ("Still the same thing as last time?", "happy")]
    linesTalking[iC][MS_NEW_FRIEND] += [
        ("I see you over there. I'm guessing that you're gonna be a regular?", "happy")]        
    linesTalking[iC][MS_NEW_FRIEND] += [
        ("Oh, oh! Oh hey! It's you! Did you like the pizza or the burger? The Blue Fruit juice? Wait, don't tell me! You liked the plays, don't you?", "happy")]        
    linesTalking[iC][MS_NEW_FRIEND] += [
        "By the way, there are rooms upstairs if you need a place to sleep."]       
        
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Hey! Nice day today, isn't it? I kind of want to roll down the hill to be honest.", "happy")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Want me to teach you chess?", "happy")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("The door's out of mana again?", "surprised")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Have some pizza, on the house! Just don't tell Lyonette.", "happy")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        "There's something I want to ask... Wait, damn. It was on the tip of my tongue! Nevermind, I guess it wasn't important."]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("I keep telling you, Goblins are cool. Just talk to them like a normal person and you'll be fine!", "happy")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        ("Have you met Belgrade and Anand? You should meet them! I think you might like them. Maybe. Or maybe you're more of a Pawn kind of person. He's nice too! But lately, he's been spending more time with Lyonette whenever he's here.", "happy")]
    linesTalking[iC][MS_GOOD_FRIEND] += [
        "Hmm... Am I spoiling Mrsha too much? Nah! She's a growing child, she needs to eat a lot. I think."]
        
        
        
        
    linesTalking[iC][MS_CLOSE_FRIEND] += linesTalking[iC][MS_GOOD_FRIEND]
    linesTalking[iC][MS_CLOSE_FRIEND] += [[
        ("Are you busy? Can I take a seat here for a breather?","sad"),
        ("Sometimes, I think to myself "What would've happened if I stayed home?" but then I see this and now I think...","default"),
        ("I built a nice place here, haven't I? A home not just for me...", "happy")]]
    linesTalking[iC][MS_CLOSE_FRIEND] += [[
        ("Have you- Have you ever worried about not being there for people when they need you?", "sad"),
        ("Or if you're not doing enough for them? Yeah... I get that sometimes.", "sad"),
        ("Whenever the Horns go on some dangerous adventure, or when I hear about Belgrade and Anand's job, I feel so worried.", "sad"),
        ("What if they get hurt? Or worse! W-What if... What if they- What if they don't come back?", "sad"),
        ("They're doing these dangerous things while I'm here, just... Just waiting for them. I'Im sorry for the heavy stuff.", "sad")]]
    linesTalking[iC][MS_CLOSE_FRIEND] += [[
        ("I think being strong isn't just about being able to punch stuff really hard or being smart, like Ryoka.", "default"),
        ("It's about being there for people. I think?", "happy"),
        ("Well, I guess what I'm saying is that I want to be there for my friends during their happy or sad moments..", "happy"),
        ("Someone needs to cheer for them, right?", "happy")]]




    
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
