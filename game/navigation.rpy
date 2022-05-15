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
    scene bg inn
    menu:
        "The Wandering Inn"
        
        "go to room":
            jump inn_room
        
        "meet Erin":
            jump meetErin
            
        "go into garden":
            jump inn_garden
        
        "go outside":
            jump floodplains
        
        "go to Liscor":
            jump liscor_market
    
    jump inn
            
label inn_garden:
    $ location = LOC_INN_GARDEN
    scene bg inn_garden
    menu:
        "Garden of Sanctuary"
        
        "go back to inn":
            jump inn
    
    jump inn_garden
        
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
        
        "go to Market Street":
            jump liscor_market
        
        "leave the city":
            jump floodplains
    
    jump liscor_watch


label floodplains:
    $ location = LOC_FLOODPLAINS
    scene bg floodplains
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
    scene bg bloodfields
    menu:
        "Bloodfields"
        
        "go to floodplains":
            jump floodplains
    
    jump bloodfields