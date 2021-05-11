from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

import random

import datetime

#import main.py, to get User Entry
import main



reset_snipe_count = 0

def auto_login():


    #define driver as chrome, load webpage
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.ea.com/en-gb/fifa/ultimate-team/web-app/")

    #sleep for 10 seconds to allow button to load, NOT GOOD!!!!!!!!!! fix this 
    #time.sleep(10)

    #find login button, click login button
    #login_button = driver.find_element_by_xpath("//button[1]")
    #login_button.click()

    #sleep for 5 seconds to allow loading
    #time.sleep(5)

    #enter email address
    #email_box = driver.find_element_by_id("email")
    #email_box.send_keys("email@gmail.com")

    #enter password
    #password_box = driver.find_element_by_id("password")
    #password_box.send_keys("password")

    #presss enter
    #password_box.send_keys(Keys.RETURN)

    #sleep for 2 seconds
    #time.sleep(2)

    #send security code
    #send_code_button = driver.find_element_by_id("btnSendCode")
    #send_code_button.click()

#######################################################################################

#generate a random sleep time
def rand_sleep(start, end, increment):
    time.sleep(random.randrange(start,end,increment))

#bronze pack method
def buy_and_sell_bronze_pack():

    print("time = ", datetime.datetime.now())
    
    global transfer_items_int
    #define number of items in transfer list
    try:
        transfer_items = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[9]/div[2]/div/div[1]/span[1]")
        transfer_items_int = int(transfer_items.text)
    except:
        print("transfer_items_int already defined")

    
    print(transfer_items_int)
    if transfer_items_int < 90:

        #Go to store
        store_button = driver.find_element_by_xpath("//button[4]")
        store_button.click()

        rand_sleep(2,5,1)

        #go to bronze pack
        #count number of packs, find if BRONZE is [3] or [4]
        pack_amounts = driver.find_elements_by_class_name("ea-filter-bar-item-view")
        #by default it returns items in the list. this gets the length of list
        xpath_button_value = len(pack_amounts)

        if xpath_button_value == 4:
            BRONZE_button = driver.find_element_by_xpath("//button[4]")
            BRONZE_button.click()
        elif xpath_button_value == 3:
            BRONZE_button = driver.find_element_by_xpath("//button[3]")
            BRONZE_button.click()
        elif xpath_button_value == 5:
            BRONZE_button = driver.find_element_by_xpath("//button[5]")
            BRONZE_button.click()
        

        rand_sleep(2,5,1)

        #click to purchase 400 coin pack
        #WORKS but uses a direct reference. Any update to HTML will break this. cant get it to work any other way tho # FIX THIS SHIT!!!!!!!!!!!!!!!
        purchase_pack = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div[2]/div[3]/button[2]")
        purchase_pack.click()

        rand_sleep(2,5,1)

        #confirm purchase
        #DIRECT REFERENCE AGAIN. PIECE OF SHIT WANK STAIN. FIX IT!!!!!!!!!!!!!!!!
        confirm_purchase = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]")
        confirm_purchase.click()

        #sleep while pack opens
        rand_sleep(7,10,1)

        #get number of players in pack
        number_of_players = driver.find_elements_by_class_name("player-stats-data-component")

        print("number_of_players = ", len(number_of_players))

        #add extra entry to player List
        number_of_players.append("extra item")




        #repeat code for number of players in pack, plus one so it knows to discard
        for i in number_of_players:

            print("start")

            #if card has pace stats, aka is a player
            if driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/section/ul/li[1]/div/div[1]/div[3]/ul/li[1]"):
            
                print("is a player")

                #get "list on transfer market" element
                list_on_transfer_market = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button")
                list_on_transfer_market.click()

                rand_sleep(1,2,1)
                

                #if COPA LIBERTADORES card, sell for 850
                try:
                    driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div[2]/article/div[2]/div[2]/ul[1]/li[1]/h2").click()
                    print("COPA LIBERTADORES CARD!!!!!!!!!!!!!")
                    buy_now_max = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
                    buy_now_max.send_keys(Keys.BACKSPACE)
                    rand_sleep(1,2,1)
                    buy_now_max.send_keys(900)
                    rand_sleep(1,2,1)
                    buy_now_min = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
                    buy_now_min.send_keys(Keys.BACKSPACE)
                    rand_sleep(1,2,1)
                    buy_now_min.send_keys(850)
                    rand_sleep(1,2,1)
                    buy_now_max.send_keys(Keys.RETURN)
                #if regular card, sell for 200
                except:
                    print("regular card, not copa")
                    buy_now_max = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
                    buy_now_max.send_keys(Keys.BACKSPACE)
                    rand_sleep(1,2,1)
                    buy_now_max.send_keys(200)
                    rand_sleep(1,2,1)
                    buy_now_max.send_keys(Keys.RETURN)


                rand_sleep(1,2,1)

                #get "list for transfer" element
                list_for_transfer = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button")
                list_for_transfer.click()


                #add 1 to number of items on transfer list
                #global transfer_items_int
                transfer_items_int +=1

                print("There are now", transfer_items_int, " items on the tranfer list")

                print("end")

                rand_sleep(2,3,1)

            else:
                #quick sell remaining items
                quick_sell_remaining = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[1]/section/div/button")
                quick_sell_remaining.click()

                rand_sleep(1,2,1)

                #confirm quick sell remaining items
                confirm_quick_sell_remaining = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]")
                confirm_quick_sell_remaining.click()

                #if theres a redeemable remaining

                rand_sleep(2,3,1)

                #check if redeem item exists by returning a list of elements with "redeem" button
                redeem_item_exists = driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")
                print(len(redeem_item_exists)," redeemable items")
                #if there are redeem buttons present
                while len(redeem_item_exists) > 0:
                    print("redeemable exists")
                    rand_sleep(1,2,1)
                # find redeem item button
                    redeem_item_button = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")
                # click redeem item
                    redeem_item_button.click()
                    #remove redeemable item from list, so code does not repeat unless theres another redeemable
                    redeem_item_exists.pop()
                    print("len(redeem_item_exists) after redeeming = ", len(redeem_item_exists))
                    rand_sleep(2,3,1)




                print("quick sell remaining items")
                rand_sleep(1,2,1)
                
                print("is not a player")
            
        #if there are less than 90 itmes in the tranfer list
        if transfer_items_int < 90:
            rand_sleep(2,3,1)
            #buy and sell again
            buy_and_sell_bronze_pack()
        else:
            print("ENDED, bc 90+ items on transfer list")
            #go to home first
            home_button = driver.find_element_by_xpath("/html/body/main/section/nav/button[1]")
            home_button.click()
            #check transfer list
            rand_sleep(2,3,1)
            manage_transfer_list()
    else:
        "cannot start until tranfer list is managed"
        manage_transfer_list()

def manage_transfer_list():

    nothing_to_clear = bool
    nothing_to_relist = bool

    #go to transfer list
    transfer_tab = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[9]/div[2]")
    transfer_tab.click()

    

    rand_sleep(1,2,1)

    #clear sold
    try:
        rand_sleep(3,5,1)
        clear_sold = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[1]/header/button")
        clear_sold.click()
    except:
        print("Nothing sold to clear")
        nothing_to_clear = True

    rand_sleep(2,3,1)

    #relist unsold items
    try:
        rand_sleep(3,5,1)
        relist_all = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button")
        relist_all.click()

        rand_sleep(1,2,1)

        #confirm relist
        confirm_relist_all = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[2]")
        confirm_relist_all.click()

        rand_sleep(2,3,1)
    except:
        print("Nothing to relist")
        nothing_to_relist = True

    home_button = driver.find_element_by_xpath("/html/body/main/section/nav/button[1]")
    home_button.click()

    #if theres nothing to clear from transfer list
    #sleep for one minute before checking again
    if nothing_to_clear == True and nothing_to_relist == True:
        rand_sleep(40,80,1)
        "The transfer list is too full for another pack. I'll sleep for a minute, then check again."
    else:
        #else if something was cleared, restart buy_and_sell_bronze_pack()
        rand_sleep(2,3,1)

    transfer_items = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[9]/div[2]/div/div[1]/span[1]")
    transfer_items_int = int(transfer_items.text)

    buy_and_sell_bronze_pack()

def sniper():
    #go to transfers tab
    transfers_tab = driver.find_element_by_xpath("/html/body/main/section/nav/button[3]")
    transfers_tab.click()

    rand_sleep(1,2,1)

    #go to Search transfer market
    search_transfer_market_button = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[2]")
    search_transfer_market_button.click()

    rand_sleep(1,2,1)

    #go to Type player name
    type_player_name = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input")
    type_player_name.send_keys(main.player_variable.get())

    

    rand_sleep(1,2,1)

    #Select typed player
    select_player = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[2]/ul/button")
    select_player.click()


    #buy now max
    buy_now_max = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input")
    buy_now_max.send_keys(Keys.BACKSPACE)
    rand_sleep(1,2,1)
    buy_now_max_amount = main.buy_variable.get()
    buy_now_max.send_keys(buy_now_max_amount)
    rand_sleep(1,2,1)
   
    try_to_snipe()





def try_to_snipe():

    #the amount of times the bot increase the minimum bid, before resetting it
    global reset_snipe_count

    #click search for players
    click_search = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
    click_search.click()

    rand_sleep(1,2,1)

    #buy player if available
    try:
        buy_now = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")
        buy_now.click()

        #confirm purchase
        confirm_purchase = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]")
        confirm_purchase.click()

        rand_sleep(1,2,1)

        #list for sale
        list_for_transfer = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button")
        list_for_transfer.click()

        #start price
        start_price = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input")
        rand_sleep(1,2,1)
        start_price.send_keys(Keys.BACKSPACE) 
        rand_sleep(1,2,1) 
        start_price.send_keys(main.sell_variable.get())

        #transfer price
        transfer_price = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input")
        rand_sleep(1,2,1)
        transfer_price.send_keys(Keys.BACKSPACE) 
        rand_sleep(1,2,1)
        transfer_price.send_keys(main.sell_variable.get())

        #list for transfer
        list_for_transfer = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button")
        list_for_transfer.click()

        rand_sleep(1,2,1)

        sniper()

    #if player isnt available
    except:
        #press Back
        back_button = driver.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
        back_button.click()

        rand_sleep(1,2,1)

        print(reset_snipe_count)

        if reset_snipe_count < 5:
            #increase minimum bid
            increase_minimum_bid = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]")
            increase_minimum_bid.click()

            reset_snipe_count +=1
        else:
            minimum_bid_input = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input")
            minimum_bid_input.click()
            rand_sleep(1,2,1)
            minimum_bid_input.send_keys(Keys.BACKSPACE) 
            rand_sleep(1,2,1) 
            minimum_bid_input.send_keys(0)

            print("in reset else:")

            reset_snipe_count =0

        time.sleep(2)

        try_to_snipe()

        


        


#buy_and_sell_bronze_pack()
#auto_login()
#sniper()




