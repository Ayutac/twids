###
# Constants for the game, especially index variables outsourced from script.rpy
# but no Dialog lines
### 

init -150 python:
    
    ## number of days
    MAX_DAYS = 31
    
    ## error constants and return values
    ERR_CHAR1_NOT_ENOUGH_HP = -1
    ERR_CHAR2_NOT_ENOUGH_HP = -2
    ERR_STAT_NOT_FOUND      = -1
    
    STAT_BELOW_MIN          = -1
    STAT_ABOVE_MAX          =  1
    STAT_WITHIN_RANGE       =  0

    BATTLE_CHAR1_WON =  1
    BATTLE_CHAR2_WON = -1
    BATTLE_TIE       =  0
    
    ## constants for battle HP. Outsourced from character.rpy 
    ## so an explanation can be given in game
    #~ the day when the increase happens
    BATTLE_HP_INCREASE_1 = 5
    BATTLE_HP_INCREASE_2 = 11
    BATTLE_HP_INCREASE_3 = 17
    BATTLE_HP_INCREASE_4 = 23
    BATTLE_HP_INCREASE = (BATTLE_HP_INCREASE_1, BATTLE_HP_INCREASE_2, BATTLE_HP_INCREASE_3, BATTLE_HP_INCREASE_4)
    #~ the base battle HP
    BATTLE_HP_AMOUNT_0 = 1
    BATTLE_HP_AMOUNT_1 = 2
    BATTLE_HP_AMOUNT_2 = 3
    BATTLE_HP_AMOUNT_3 = 4
    BATTLE_HP_AMOUNT_4 = 5
    BATTLE_HP_AMOUNT = (BATTLE_HP_AMOUNT_0, BATTLE_HP_AMOUNT_1, BATTLE_HP_AMOUNT_2, BATTLE_HP_AMOUNT_3, BATTLE_HP_AMOUNT_4)
    

    ## index variables for easier accessing
    STAT_BODY  = 0
    STAT_MIND  = 1
    STAT_HEART = 2
    
    ## MS for Milestone
    MS_ARCH_ENEMY    = -5
    MS_ENEMY         = -4
    MS_CREEP         = -3
    MS_JERK          = -2
    MS_IDIOT         = -1
    MS_STRANGER      =  0
    MS_NEW_FRIEND    =  1
    MS_GOOD_FRIEND   =  2
    MS_CLOSE_FRIEND  =  3
    MS_BOYFRIEND     =  4
    MS_LOVER         =  5
    MS_BOYTOY        =  6
    MS_BFF           =  7
    MS_SEX_FRIEND    =  8
    
    MS_FIRST_NON_BAD      = MS_STRANGER
    MS_LAST_NORMAL_GOOD   = MS_LOVER
    MS_FIRST_SPECIAL_GOOD = MS_BOYTOY
    MS_LAST_SPECIAL_GOOD  = MS_BFF

    LEN_MS = 13
    
    #~ I know it's unusual to save constants like that, but
    #~ since this is likely to be changed, this coding makes things easier.    
    CHAR_OTHER = -2
    CHAR_NONE = -1
    
    CHAR_ERIN      = 0
    CHAR_PISCES    = 1
    CHAR_PROTA     = 2
    
    PROTA_NAME = "You"
    
    LEN_CHAR_DCHARS = CHAR_PROTA
    LEN_CHAR        = CHAR_PROTA+1
    
    ## AL for answer level
    
    AL_VERY_WRONG   = 0
    AL_WRONG        = 1
    AL_ALMOST_RIGHT = 2
    AL_RIGHT        = 3
    
    LEN_AL = 4
    
    GIFT_DERP   = 0
    GIFT_SMALL  = 1
    GIFT_MEDIUM = 2
    GIFT_LARGE  = 3
    GIFT_SUPERB = 4
    
    LEN_GIFT = 5
    
    ## item initialization
    
    ITEMS_FOR_EACH_DCHAR = 1 ## tells how many items are custom for each dchar
    
    ITEM_TAKEN = -2    
    ITEM_NONE  = -1
    
    #~ same as CHAR_
    ITEM_NONE        = -1
    
    #~ keys; AK is short for apartment key ASK is short for apartment spare key
    #~ if you change the ordering here, make sure to change meetDchar accordingly
    ITEM_AK_MASTER     = 1+ITEM_NONE
    ITEM_AK_PROTA      = 1+ITEM_AK_MASTER
    ITEM_ASK_PROTA     = 1+ITEM_AK_PROTA
    ITEM_ASK_ERIN      = 1+ITEM_ASK_PROTA
    ITEM_ASK_PISCES    = 1+ITEM_ASK_ERIN
    
    ## this order has the advantage that one can access individual
    ## dchar items easily, e.g. ITEM_ASK_PROTA+1+dchar= ASK of that dchar
    
    LEN_ITEM = ITEM_ASK_PISCES+1
    
    ## Loc for Location
    LOC_WORLD           =   0
    LOC_INN             = LOC_WORLD
    LOC_INN_GARDEN      =   1
    LOC_INN_WEIGHTS     =   2
    LOC_INN_ROOM        = 100
    LOC_LISCOR_MARKET   = 200
    LOC_LISCOR_WATCH    = 201
    LOC_FLOODPLAINS     = 210
    LOC_BARKWOOD        = 211
    LOC_BLOODFIELDS     = 212
    
    ## floor locations
    LOC_PROTA_FLOOR = 1
    
    ## dating locations
    
    DATE_LOC_INN = 0
    DATE_LOC_LISCOR_MARKET = 1
    
    ## saves which dating location belongs to which locaction
    
    DATE_LOC_LOCATION = [
        LOC_INN,
        LOC_LISCOR_MARKET
    ]
    
    LEN_DATE_LOC = len(DATE_LOC_LOCATION)
    
    ## inventory variables to use the inventory correctly
    INV_TO_USE   = 1
    INV_TO_GIFT  = 2
    INV_TO_STORE = 3
    INV_TO_TAKE  = 4