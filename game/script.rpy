###
# This file contains the definitions of characters, stats and almost any
# other global variable. 
###

## In general, we will have two Variables for a character: 
## The one with data (Python-based) and the one to look at and speak with (Ren'Py-based).
## The first's name will start with a small letter and the last with a big letter.

define Erin      = DynamicCharacter("erin.getShortDisplayName()")
define Pisces    = DynamicCharacter("pisces.getShortDisplayName()")
## non dateable characters
define Prota     = Character(PROTA_NAME)
## when changing the characters, don't forget to change the following 2 lines
define Dcharlist = [Erin, Pisces]
define Charlist = Dcharlist + [Prota]

python early:
    introRunning = False
    creditsRunning = False
    endingRunning = False
    lastMusic = None

init -11 python:
    import math
    import random
    random.seed()
    
    def useItem(): #needed for proper returning from inventory
        renpy.call('useItemLabel')
        return
    
    help = 50
    if persistent.doubleStats:
        help = 100
        persistent.doubleStats = False
    
    STATS = Stats(["Body", "Mind", "Heart"], max = help)
        
    ## Global variables:
    day = 0
    location = 0 ## current location of the player
    isSleeping = False
    dchar = CHAR_NONE ## datable character player is meeting with
    item = ITEM_NONE ## the selected item
    roomOfDchar = CHAR_NONE ## the owner of the  apartment you are visiting
    CIQ = None ## (dateable) Character In Question (for avoiding array calls)
    RIQ = None ## Relation In Question (for avoiding getting calls)
    battle = None ## stores a battle
    date = None ## stores a date
    mouseOverItem = ITEM_NONE ## item of inventory which is hovered over
    
    ## inits needed for proper saving/loading
    prota = None
    erin = None
    pisces = None
    dcharlist = None
    charlist= None
    IA = None
    SIA = None
    
    masterKey = None
    keyToApartment = None
    spareKeyToApartment = None
    spareKeyToErinsApartment = None
    spareKeyToPiscesApartment = None
    
    inventory = None
    shop_krshia = None
    
    Item.initialize(LEN_CHAR, CHAR_PROTA) ## very important!
    
    noIntro = False

label start:
    
    if creditsRunning == True:
        jump credits
    
    python:
        prota = DSC(STATS, "You", (10, 10, 10), money = 100)
        prota.restoreHP()
        prota.restoreBattleHP() 
        erin = DSC(STATS, "Erin", (10, 10, 50), crypt7='erineri',
            crypt6='eriner', crypt5='erine',
            unname="that crazy [Innkeeper]",
            giftReaction = dcharGiftEffect[CHAR_ERIN])
        pisces = DSC(STATS, "Erin", (20, 35, 15), crypt7='piscesp',
            unname="the [Nechromancer]",
            giftReaction = dcharGiftEffect[CHAR_PISCES])
            
        ## create lists
        dcharlist = [erin, pisces]
        charlist = dcharlist + [prota] ## always at the end!!
        
        ## create relationships
        #narrator(str(type(charlist)))
        IA = Interaction(charlist)
        IA.getRel(0,1)
        SIA = SingleInteraction(IA, CHAR_PROTA)
        
    call initializeItemDB from _call_initializeItemDB
        
    python:
        keyToApartment.addCarryingD(1)
        spareKeyToApartment.addStoredD(1)
        spareKeyToErinsApartment.addCarrying(CHAR_ERIN, 1)
        spareKeyToErinsApartment.addCarrying(CHAR_PISCES, 1)
    
    scene bg inn_room
    $ sleepGood()
    jump inn_room

    return
