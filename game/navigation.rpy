###
# This file is for the overall navigation.
# For now, it is text based, but we can change this later
###
            
label worldReturn:
    if location == LOC_INN:
        jump inn
    if location == LOC_INN_GARDEN:
        jump inn_garden
    if location == LOC_INN_ROOM:
        jump inn_room
    if location == LOC_LISCOR_MARKET:
        jump liscor_market
    if location == LOC_LISCOR_WATCH:
        jump liscor_watch
    if location == LOC_FLOODPLAINS:
        jump floodplains
    if location == LOC_BARKWOOD:
        jump barkwood
    if location == LOC_BLOODFIELDS:
        jump bloodfields
    jump inn

label inn:
    $ location = LOC_INN
    $ playMusic('tenderness.mp3')
    scene bg inn
    menu:
        "The Wandering Inn"
        
        "go to room":
            jump inn_room

        "help out inn kitchen (30 AP)":
            $ resultVal = prota.work(30, (.04, .04, .12))
            if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                "You don't have enough energy left."
            else:
                $ resultVal = moneyStringShort(resultVal)
                $ playSound("coin_drop.mp3")
                "You earned [resultVal]!"
            jump inn

        "go into garden":
            jump inn_garden
            
        "go into weights room":
            jump inn_weights

        "go into theatre area":
            jump inn_theatre
        
        "go outside":
            jump floodplains
        
        "go to Liscor":
            jump liscor_market
    
    jump inn

label inn_theatre:
    $ location = LOC_INN_THEATRE
    $ playMusic('tenderness.mp3')
    scene bg inn_theatre
    menu:
        "The Grand Theatre"

        "meet Erin":
            jump meetErin

        "play chess (25 AP)":
            $ resultVal = prota.train(25, (0, 3+random.randint(-1,1), 0))
            if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                "You don't have enough energy left."
            else:
                $ resultVal = resultVal[1]
                "Your mind stat got raised by [resultVal]!"
            jump inn

        "practice with players (30 AP)":
            $ resultVal = prota.train(30, (0, 0, 4+random.randint(-1,1)))
            if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                "You don't have enough energy left."
            else:
                $ resultVal = resultVal[2]
                "Your heart stat got raised by [resultVal]!"
            jump inn

        "go into garden":
            jump inn_garden

        "go to entrance area":
            jump inn

    jump inn_theatre
            
label inn_garden:
    $ location = LOC_INN_GARDEN
    scene bg inn_garden
    menu:
        "Garden of Sanctuary"
        
        "go back to inn":
            jump inn

        "go into theatre area":
            jump inn_theatre
    
    jump inn_garden
            
label inn_weights:
    $ location = LOC_INN_WEIGHTS
    scene bg inn_weights
    menu:
        "Weights room"
        
        "train (50 AP)":
            $ resultVal = prota.train(50, (6+random.randint(-1,1), 0, 0))
            if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                "You don't have enough energy left."
            else:
                $ resultVal = resultVal[0]
                "Your body stat got raised by [resultVal]!"
            jump inn_weights
        
        "go back to inn":
            jump inn
    
    jump inn_weights
        
label inn_room:
    $ location = LOC_INN_ROOM
    #$ playMusic('pewter_city.ogg')
    scene bg inn_room
    menu:
        "Your room"
        
        "get out here":
            jump inn
        
        "sleep":
            $ sleepGood()
            jump inn_room
    
    jump inn_room


label liscor_market:
    $ location = LOC_LISCOR_MARKET
    $ playMusic('onceagain.mp3')
    scene bg liscor_market
    menu:
        "Market Street of Liscor"
        
        "go to Krshia's shop":
            jump shop_krshia
        
        "go to Watch barracks":
            jump liscor_watch
        
        "go to the Wandering Inn":
            jump inn
        
        "leave the city":
            jump floodplains
    
    jump liscor_market

label shop_krshia:
    scene bg shop_krshia
    menu:
        "Krshia's Shop"
            
        "help out Krshia (25 AP)":
            $ resultVal = prota.work(25, (.0333, .0333, .1))
            if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                "You don't have enough energy left."
            else:
                $ resultVal = moneyStringShort(resultVal)
                $ playSound("coin_drop.mp3")
                "You earned [resultVal]!"
            jump shop_krshia
        
        #"buy":
        #    python:
        #        resultVal = buyFromShop(shop_krshia)
        #        if resultVal == None:
        #            renpy.jump('shop_krshia')
                    
        "leave":
            jump liscor_market
    
    jump shop_krshia
    
label liscor_watch:
    $ location = LOC_LISCOR_WATCH
    scene bg liscor_watch
    menu:
        "Liscor Watch barracks"
            
        "help out Zevara (35 AP)":
            $ resultVal = prota.work(35, (.15, .05, .05))
            if resultVal == ERR_CHAR1_NOT_ENOUGH_HP:
                "You don't have enough energy left."
            else:
                $ resultVal = moneyStringShort(resultVal)
                $ playSound("coin_drop.mp3")
                "You earned [resultVal]!"
            jump liscor_watch
        
        "go to Market Street":
            jump liscor_market
        
        "leave the city":
            jump floodplains
    
    jump liscor_watch


label floodplains:
    $ location = LOC_FLOODPLAINS
    scene bg floodplains
    $ playMusic('instinct.mp3')
    menu:
        "Floodplains of Liscor"
        
        "go into the Wandering Inn":
            jump inn
        
        "go into Liscor":
            jump liscor_market
        
        "go to Barkwood Forest":
            jump barkwood
        
        "go to Bloodfields":
            jump bloodfields
    
    jump floodplains

label barkwood:
    $ location = LOC_BARKWOOD
    scene bg barkwood
    menu:
        "Barkwood Forest"
        
        "meet Pisces":
            jump meetPisces
        
        "go to floodplains":
            jump floodplains
    
    jump barkwood

label bloodfields:
    $ location = LOC_BLOODFIELDS
    $ playMusic('evolution.mp3')
    scene bg bloodfields
    menu:
        "Bloodfields"
        
        "go to floodplains":
            jump floodplains
    
    jump bloodfields