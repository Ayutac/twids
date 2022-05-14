###
# For all items and how dchars like them.
# Created on 21.09.2012 by Sebastian Koch
### 

label initializeItemDB:

    python:
        
        ## all items:
        #~ usual ones (giftable):
        # pokeball = Item("Pokéball", price = 50)
        #~ unique ones ((not) ungiftable):
        masterKey = Item("Master Key", limit = 1)
        keyToApartment = Item("Key to Room", limit = 1)
        spareKeyToApartment = Item("Spare Key to Room", limit = 1)
        spareKeyToErinsApartment = Item("Spare Key to Erin's Room", limit = 1)
        spareKeyToPiscesApartment = Item("Spare Key to Pisces' Room", limit = 1)
        
        ## put all of them into the inventory
        inventory = [
            masterKey,
            keyToApartment,
            spareKeyToApartment,
            ## it is IMPORTANT the dchars' keys stay at the end of the list
            ## for the use in hotel (dcharRoom) and handing over the key (dcharNavi)
            ## design decision: group general custom items together for each dchar
            spareKeyToErinsApartment,
            #erinsDiary,
            spareKeyToPiscesApartment]
            
        ## give any shop the indices of its items
        shop_krshia = []
        
    return ## we call this label, so return is needed
            
init -5 python:
            
        def hasAnythingStoredD():
            for i in range(0, len(inventory)):
                if inventory[i].hasStoredD():
                    return True
            return False
            
        def hasAnythingWithD():
            for i in range(0, len(inventory)):
                if inventory[i].hasWithD():
                    return True
            return False
        
        def buyFromShop(shoplist):
            shopChoiceSelection = []
            for i in range(0, len(shoplist)):
                shopChoiceSelection.append((
                    inventory[shoplist[i]].Name + " ($ " +
                    str(inventory[shoplist[i]].Price) + ")", shoplist[i]))
            shopChoiceSelection.append(("leave", -1))
            narrator("What do you want to buy?", interact = False)
            resultVal = menu(shopChoiceSelection)
            if resultVal == -1:
                return None
            resultVal = SIA.buy(inventory[resultVal])
            if resultVal == True:
                narrator("Thank you very much!")
            elif resultVal == False:
                narrator("You can't afford this!")
            elif resultVal == -1:
                narrator("You can't carry this!")
            return resultVal

## here is specified what certain items do.
## kwargs needed for proper use of renpy.call
## when adding return anywhere, do not forget to set item = ITEM_NONE
label useItemLabel(**kwargs): 
    #global item
    python:
        renpy.hide_screen('inventory')
    if dchar != CHAR_NONE or inventory[item].hasWithD() != True:
        if dchar == CHAR_NONE: ## if not we need to remember the item
            $ item = ITEM_NONE
        return
    python:
        narrator("[prota.Name], this isn't the right time for this.")
        Prota("Professor Oak?")
        item = ITEM_NONE
    return
