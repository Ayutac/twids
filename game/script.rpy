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
    partyLoc = 0 ## current party location of the player
    floor = 1 ## current floor of the player
    dchar = CHAR_NONE ## datable character player is meeting with
    item = ITEM_NONE ## the selected item
    roomOfDchar = CHAR_NONE ## the owner of the  apartment you are visiting
    CIQ = None ## (dateable) Character In Question (for avoiding array calls)
    RIQ = None ## Relation In Question (for avoiding getting calls)
    battle = None ## stores a battle
    date = None ## stores a date
    mouseOverItem = ITEM_NONE ## item of inventory which is hovered over

label start:
    
    jump inn

    return
