"""
This program is essentially a calculator, but a plain calculator is boring, so
I added dessert because I have a giant sweet tooth :)
"""
__author__ = "Gloria Mayo"
# Gloria Mayo (Yalissa)
# This program is going to ask the user to choose between cookies, cake, or
# pies, and then has them choose one of 3 options provided for each
# It is then going to ask them how many servings of dessert they would like,
# and do the calculations to provide the user with exact quantities
# I am going to start the program by introducing it to the user
from time import sleep


def not_crash_selection(prompt):
    """
This function is to make sure that the program doesn't crash when the user
makes their selections
    :param prompt: asks the user to enter the selection based on the menu
    :return: the selection that the user chose
    """
    test = 0
    input_validation = True
    while input_validation:
        try:
            test = int(input(prompt))
            input_validation = False
        except:
            print("Please enter valid input.")
            # i kept misspelling except and almost ripped my hair out trying
            # to figure out what was wrong -_-
        if test < 1 or test > 3:
            print("Please enter a valid number.")
            input_validation = True
    return test


def not_crash_quan(instructions):
    """
This is to make sure the program doesn't crash when the user enters the
quantity of dessert
    :param instructions: asks the user how much of the dessert they want
    """
    example = 0
    input_Validation = True
    while input_Validation:
        try:
            example = float(input(instructions))
            input_Validation = False
        except:
            print("Please enter a positive number.")
        if example < 1:
            print("Enter a positive number.")
    return example


# I googled how to delay my print statements so that it would be easier to
# read and not just a giant block of text (free code camp was the website)
# take each recipe function as arguments and parameters
def main():
    """
code for the main calculations for my integration project
    """
    # i start the program by introducing it to the user
    print("Hey there!")
    sleep(2)
    print("This program gives you the quantity of ingredients", end=' ')
    print("for however many servings of dessert your heart desires.", end=' ')
    sleep(3)
    print("\nSo lets get started!")
    sleep(2)
    print("Here are your choices:")
    sleep(2)
    # Im now going to ask the user to choose a dessert type
    print("1. Cookies")
    sleep(1)
    print("2. Cakes")
    sleep(1)
    print("3. Pies")
    sleep(1)
    user_dessert_choice = not_crash_selection("Enter the number that "
                                              "corresponds with your choice.")
    # user_dessert_choice = int(input("Enter the number that corresponds with "
    #                                "your choice: "))
    mess = "Great Choice!"
    print(mess)
    sleep(2)
    # Im now going to ask the user to choose a cookie type
    if user_dessert_choice == int(1):
        print("Here are your cookie options:")
        sleep(2)
        print("1. Chocolate Chip")
        sleep(1)
        print("2. Oatmeal Raisin")
        sleep(1)
        print("3. Snickerdoodle")
        sleep(1)
        cookie_selection = not_crash_selection(
            "Enter the number that corresponds with your choice.")
        # cookie_selection = int(input("Enter the number that corresponds with
        # "your choice: "))
        print(mess)
        sleep(2)
        cookie_quantity = not_crash_quan("Enter the number of cookies you "
                                         "would like.")
        # cookie_quantity = int(
        # input("Enter the number of cookies you would like: "))
        # all measurements follow the metric system
        print("Below is the quantity of each ingredient you will need.")
        sleep(2)
        if cookie_selection == int(1):
            # cookie recipe (18 servings)
            cc_cookie_salted_butter = float(113.50)  # grams
            cc_cookie_granulated_sugar = float(100.00)  # grams
            cc_cookie_light_brown_sugar = float(110.00)  # grams
            cc_cookie_vanilla_extract = float(1.00)  # tsp
            cc_cookie_unsweetened_applesauce = float(65.00)  # egg substitute
            cc_cookie_flour = float(180.00)  # grams
            cc_cookie_baking_soda = float(0.50)  # tsp
            cc_cookie_baking_powder = float(0.30)  # tsp
            cc_cookie_salt = float(0.50)  # tsp
            cc_cookie_chocolate_chips = float(175.00)  # grams
            cc_cookie_scaling = cookie_quantity / int(18)
            print("Amount of salted butter: ",
                  format(cc_cookie_salted_butter * cc_cookie_scaling, "0.2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ", format(
                cc_cookie_granulated_sugar * cc_cookie_scaling, "0.2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of light brown sugar: ", format(
                cc_cookie_light_brown_sugar * cc_cookie_scaling, "0.2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of vanilla extract: ",
                  format(cc_cookie_vanilla_extract * cc_cookie_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of unsweetened applesauce: ", format(
                cc_cookie_unsweetened_applesauce * cc_cookie_scaling,
                "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of flour: ",
                  format(cc_cookie_flour * cc_cookie_scaling, "0.2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of baking soda: ",
                  format(cc_cookie_baking_soda * cc_cookie_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of baking powder: ",
                  format(cc_cookie_baking_powder * cc_cookie_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(cc_cookie_salt * cc_cookie_scaling, "0.2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of chocolate chips: ",
                  format(cc_cookie_chocolate_chips * cc_cookie_scaling,
                         "0.2f"), " grams", sep='')
        elif cookie_selection == int(2):
            # oatmeal cookie recipe (18 servings)
            oatmeal_flour = float(125)  # grams
            oatmeal_baking_soda = float(.5)  # tsp
            oatmeal_sea_salt = float(.5)  # tsp
            oatmeal_baking_powder = float(.25)  # tsp
            oatmeal_cinnamon = float(.5)  # tsp
            oatmeal_original_butter = float(114)  # grams
            oatmeal_granulated_sugar = float(100)  # grams
            oatmeal_light_brown_sugar = float(110)  # grams
            oatmeal_unsweetened_applesauce = float(32)  # grams
            oatmeal_vanilla = float(1)  # tsp
            oatmeal_oats = float(135)  # grams
            oatmeal_raisins = float(237)  # grams
            oatmeal_scaling = cookie_quantity / int(18)
            print("Amount of flour: ",
                  format(oatmeal_flour * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of baking soda: ",
                  format(oatmeal_baking_soda * oatmeal_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(oatmeal_sea_salt * oatmeal_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of baking powder: ",
                  format(oatmeal_baking_powder * oatmeal_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of cinnamon: ",
                  format(oatmeal_cinnamon * oatmeal_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of unsalted butter: ",
                  format(oatmeal_original_butter * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ",
                  format(oatmeal_granulated_sugar * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of light brown sugar: ",
                  format(oatmeal_light_brown_sugar * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of unsweetened applesauce: ",
                  format(oatmeal_unsweetened_applesauce * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of vanilla extract: ",
                  format(oatmeal_vanilla * oatmeal_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of oats: ",
                  format(oatmeal_oats * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of raisins: ",
                  format(oatmeal_raisins * oatmeal_scaling,
                         "0.2f"), " grams", sep='')
        else:
            # snickerdoodle recipe (makes 14)
            snickerdoodle_shortening = float(52)  # grams
            snickerdoodle_salted_butter = float(57)  # grams
            snickerdoodle_granulated_sugar = float(150)  # grams
            snickerdoodle_unsweetened_applesauce = float(32)  # grams
            snickerdoodle_vanilla = float(.5)  # tsp
            snickerdoodle_flour = float(167)  # grams
            snickerdoodle_cinnamon = float(.25)  # tsp
            snickerdoodle_tartar = float(1)  # tsp
            snickerdoodle_baking_soda = float(.5)  # tsp
            snickerdoodle_salt = float(.13)  # tsp (1/8 but don't know how to
            # print as fraction at the end)
            sc_topping_sugar = float(2)  # tbs
            sc_topping_cinnamon = float(1.5)  # tsp
            snickerdoodle_scaling = cookie_quantity / int(14)
            print("Amount of shortening: ",
                  format(snickerdoodle_shortening * snickerdoodle_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of salted butter: ",
                  format(snickerdoodle_salted_butter * snickerdoodle_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ",
                  format(snickerdoodle_granulated_sugar *
                         snickerdoodle_scaling, "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of unsweetened applesauce: ",
                  format(snickerdoodle_unsweetened_applesauce *
                         snickerdoodle_scaling, "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of vanilla extract: ",
                  format(snickerdoodle_vanilla * snickerdoodle_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of flour: ",
                  format(snickerdoodle_flour * snickerdoodle_scaling,
                         "0.2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of cinnamon: ",
                  format(snickerdoodle_cinnamon * snickerdoodle_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of tartar: ",
                  format(snickerdoodle_tartar * snickerdoodle_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of baking soda: ",
                  format(snickerdoodle_baking_soda * snickerdoodle_scaling,
                         "0.2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(snickerdoodle_salt * snickerdoodle_scaling,
                         "0.2f"), " tps", sep='')
            sleep(1.5)
            print("Below is the quantity of ingredients needed for the cookie "
                  "garnish.")
            sleep(1.5)
            print("Amount of sugar: ",
                  format(sc_topping_sugar * snickerdoodle_scaling, "0.2f"),
                  " tbs", sep='')
            sleep(1.5)
            print("Amount of cinnamon: ", format(sc_topping_cinnamon *
                                                 snickerdoodle_scaling,
                                                 "0.2f"), " tsp", sep='')
    elif user_dessert_choice == int(2):
        print("Here are your cake options:")
        sleep(1)
        print("1. Vanilla Cake")
        sleep(1)
        print("2. Chocolate Cake")
        sleep(1)
        print("3. Carrot Cake")
        cake_selection = not_crash_selection("Enter the number that "
                                             "corresponds with your choice.")
        # cake_selection = int(input("Enter the number that corresponds with "
        #                            "your choice:"))
        print(mess)
        sleep(1.5)
        cake_quantity = not_crash_quan("Enter the desired number of cake "
                                       "servings.")
        # cake_quantity = int(input("Enter desired number of cake servings: "))
        sleep(1.5)
        print("Below is the quantity of each ingredient you will need.")
        sleep(1.5)
        if cake_selection == int(1):
            vanilla_cake_flour = float(219)  # grams
            vanilla_cake_baking_soda = float(.5)  # tsp
            vanilla_cake_baking_powder = float(.5)  # tsp
            vanilla_cake_sea_salt = float(.5)  # tsp
            vanilla_salted_butter = float(114)  # grams
            vanilla_cake_granulated_sugar = float(250)  # grams
            vanilla_cake_unsweetened_applesauce = float(130)  # grams
            vanilla_cake_sour_cream = float(120)  # grams
            vanilla_cake_whole_milk = float(237)  # ml
            vanilla_cake_canola_oil = float(59)  # ml
            vanilla_cake_vanilla_extract = float(2)  # tsp
            vanilla_scaling = cake_quantity / int(18)  # number of servings
            print("Amount of flour: ",
                  format(vanilla_cake_flour * vanilla_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of baking soda: ",
                  format(vanilla_cake_baking_soda * vanilla_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of baking powder: ",
                  format(vanilla_cake_baking_powder * vanilla_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(vanilla_cake_sea_salt * vanilla_scaling, ".2f"),
                  " tsp",
                  sep='')
            print("Amount of salted butter: ",
                  format(vanilla_salted_butter * vanilla_scaling, ".2f"),
                  " grams",
                  sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ",
                  format(vanilla_cake_granulated_sugar * vanilla_scaling,
                         ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of unsweetened applesauce: ",
                  format(vanilla_cake_unsweetened_applesauce * vanilla_scaling,
                         ".2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of sour cream: ",
                  format(vanilla_cake_sour_cream * vanilla_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of whole milk ",
                  format(vanilla_cake_whole_milk * vanilla_scaling, ".2f"),
                  " ml",
                  sep='')
            sleep(1.5)
            print("Amount of canola oil: ",
                  format(vanilla_cake_canola_oil * vanilla_scaling, ".2f"),
                  " ml",
                  sep='')
            sleep(1.5)
            print("Amount of vanilla extract: ",
                  format(vanilla_cake_vanilla_extract * vanilla_scaling,
                         ".2f"),
                  " tsp", sep='')
        elif cake_selection == int(2):
            chocolate_cake_flour = float(150)  # grams
            chocolate_cake_granulated_sugar = float(225)  # grams
            chocolate_cake_cocoa_powder = float(25)  # grams
            chocolate_cake_baking_soda = float(.5)  # tsp
            chocolate_cake_baking_powder = float(.5)  # tsp
            chocolate_cake_salt = float(.5)  # tsp
            chocolate_cake_espresso_powder = float(.5)  # tsp
            chocolate_cake_oil = float(128)  # ml
            chocolate_cake_unsweetened_applesauce = float(64)  # grams
            chocolate_scaling = cake_quantity / int(16)  # number of servings
            print("Amount of flour: ",
                  format(chocolate_cake_flour * chocolate_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ",
                  format(chocolate_cake_granulated_sugar * chocolate_scaling,
                         ".2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of cocoa powder: ",
                  format(chocolate_cake_cocoa_powder * chocolate_scaling,
                         ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of baking soda: ",
                  format(chocolate_cake_baking_soda * chocolate_scaling,
                         ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of baking powder: ",
                  format(chocolate_cake_baking_powder * chocolate_scaling,
                         ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(chocolate_cake_salt * chocolate_scaling, ".2f"),
                  " tsp",
                  sep='')
            sleep(1.5)
            print("Amount of espresso powder: ",
                  format(chocolate_cake_espresso_powder * chocolate_scaling,
                         ".2f"), "tsp", sep='')
            sleep(1.5)
            print("Amount of oil: ",
                  format(chocolate_cake_oil * chocolate_scaling, ".2f"), " ml",
                  sep='')
            sleep(1.5)
            print("Amount of unsweetened applesauce: ", format(
                chocolate_cake_unsweetened_applesauce * chocolate_scaling,
                ".2f"),
                  " grams", sep='')

        else:
            carrot_cake_flour = float(156)  # grams
            carrot_cake_baking_soda = float(1)  # tsp
            carrot_cake_baking_powder = float(.5)  # tsp
            carrot_cake_salt = float(.5)  # tsp
            carrot_cake_cinnamon = float(1)  # tsp
            carrot_cake_butter = float(114)  # grams
            carrot_cake_sugar = float(150)  # grams
            carrot_cake_brown_sugar = float(55)  # grams
            carrot_cake_applesauce = float(189)  # grams
            carrot_cake_vanilla = float(1)  # tsp
            carrot_cake_carrots = float(128)  # grams
            carrot_cake_scaling = cake_quantity / int(16)  # number of servings
            print("Amount of flour: ", format(carrot_cake_flour *
                                              carrot_cake_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount baking soda: ", format(carrot_cake_baking_soda *
                                                 carrot_cake_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount baking powder: ", format(carrot_cake_baking_powder *
                                                   carrot_cake_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount salt: ",
                  format(carrot_cake_salt * carrot_cake_scaling,
                         ".2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount cinnamon: ", format(carrot_cake_cinnamon *
                                              carrot_cake_scaling, ".2f"),
                  " tsp",
                  sep='')
            sleep(1.5)
            print("Amount unsalted butter: ", format(carrot_cake_butter *
                                                     carrot_cake_scaling,
                                                     ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount granulated sugar: ", format(carrot_cake_sugar *
                                                      carrot_cake_scaling,
                                                      ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount brown sugar: ", format(carrot_cake_brown_sugar *
                                                 carrot_cake_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount unsweetened applesauce: ",
                  format(carrot_cake_applesauce
                         * carrot_cake_scaling,
                         ".2f"), " grams",
                  sep='')
            sleep(1.5)
            print("Amount vanilla extract: ", format(carrot_cake_vanilla *
                                                     carrot_cake_scaling,
                                                     ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount shredded carrots: ", format(carrot_cake_carrots *
                                                      carrot_cake_scaling,
                                                      ".2f"),
                  " grams", sep='')
    else:
        print("Here are your pie options:")
        sleep(1)
        print("1. Key Lime Pie")
        sleep(1)
        print("2. Pumpkin Pie")
        sleep(1)
        print("3. Apple Crumble Pie")
        pie_selection = not_crash_selection("Enter the number that "
                                            "corresponds with your choice.")
        # pie_selection = int(
        #     input("Enter the number that corresponds with your "
        #           "choice: "))
        print(mess)
        sleep(1.5)
        pie_quantity = not_crash_quan("Enter desired number of pie servings.")
        # pie_quantity = int(input("Enter desired number of pie servings: "))
        sleep(1.5)
        print("Below is the quantity needed for the pie crust.")
        sleep(1.5)
        if pie_selection == int(1):
            kL_pie_crust_crackers = float(148)  # grams
            kL_pie_crust_sugar = float(50)  # grams
            kL_pie_crust_cinnamon = float(.5)  # tsp
            kL_pie_crust_butter = float(89)  # grams
            # KL_pie_filling_milk = float(794)  # grams
            # im lactose intolerant, so I don't know why i included milk in the
            # first place (vanilla almond milks slaps tho)
            KL_pie_filling_sour_cream = float(115)  # grams
            KL_pie_filling_unsweetened_apple_sauce = float(128)  # grams
            Kl_pie_filling_lime_juice = float(177)  # ml
            KL_pie_filling_vanilla = float(.25)  # tsp
            KL_pie_scaling = pie_quantity / int(12)  # number of servings
            sleep(1.5)
            print("Amount of crackers: ", format(kL_pie_crust_crackers *
                                                 KL_pie_scaling, ".2f"),
                  " grams",
                  sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ", format(kL_pie_crust_sugar *
                                                         KL_pie_scaling,
                                                         ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of cinnamon: ", format(kL_pie_crust_cinnamon *
                                                 KL_pie_scaling, ".2f"),
                  " tsp",
                  sep='')
            sleep(1.5)
            print("Amount of salted butter: ", format(kL_pie_crust_butter *
                                                      KL_pie_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Below is the quantity needed for the pie filling.")
            sleep(1.5)
            print("Amount of sour cream: ", format(KL_pie_filling_sour_cream *
                                                   KL_pie_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of unsweetened applesauce: ", format(
                KL_pie_filling_unsweetened_apple_sauce * KL_pie_scaling,
                ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of lime juice: ", format(
                Kl_pie_filling_lime_juice * KL_pie_scaling, ".2f"), " ml",
                  sep='')
            sleep(1.5)
            print("Amount of vanilla extract: ",
                  format(KL_pie_filling_vanilla *
                         KL_pie_scaling, ".2f"),
                  " tsp", sep='')

        elif pie_selection == int(2):
            pP_filling_unsweetened_apple_sauce = float(96)  # grams
            pP_filling_pumpkin_puree = float(435)  # grams
            pP_filling_cream = float(237)  # grams
            pP_filling_vanilla = float(1)  # tsp
            pP_filling_light_brown_sugar = float(165)  # grams
            pP_filling_salt = float(.5)  # tsp
            pP_filling_cinnamon = float(2)  # tsp
            pP_filling_spice = float(2)  # tsp
            pP_crust_flour = float(158)  # grams
            pP_crust_salt = float(.5)  # tsp
            pP_crust_sugar = float(1)  # tsb
            pP_crust_butter = float(114)  # grams
            pP_crust_water = float(.59)  # ml
            pP_scaling = pie_quantity / int(10)  # number of servings
            sleep(1.5)
            print("Amount of flour: ",
                  format(pP_crust_flour * pP_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(pP_crust_salt * pP_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ", format(pP_crust_sugar *
                                                         pP_scaling, ".2f"),
                  " tbs",
                  sep='')
            sleep(1.5)
            print("Amount of unsalted butter: ", format(pP_crust_butter *
                                                        pP_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of water: ",
                  format(pP_crust_water * pP_scaling, ".2f"),
                  " ml", sep='')
            sleep(1.5)
            print("Below is the quantity needed for the pie filling.")
            sleep(1.5)
            print("Amount of unsweetened applesauce: ", format(
                pP_filling_unsweetened_apple_sauce * pP_scaling, ".2f"),
                  " grams",
                  sep='')
            sleep(1.5)
            print("Amount of pumpkin puree: ",
                  format(pP_filling_pumpkin_puree *
                         pP_scaling, ".2f"), " grams",
                  sep='')
            sleep(1.5)
            print("Amount of heavy cream: ",
                  format(pP_filling_cream * pP_scaling,
                         ".2f"), " grams", sep='')
            sleep(1.5)
            print("Amount of vanilla extract: ", format(pP_filling_vanilla *
                                                        pP_scaling, ".2f"),
                  " tsp",
                  sep='')
            sleep(1.5)
            print("Amount of light brown sugar: ", format(
                pP_filling_light_brown_sugar * pP_scaling, ".2f"), " grams",
                  sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(pP_filling_salt * pP_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of cinnamon: ",
                  format(pP_filling_cinnamon * pP_scaling,
                         ".2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of pumpkin pie spice: ", format(pP_filling_spice *
                                                          pP_scaling, ".2f"),
                  " tsp", sep='')
        else:
            aC_crust_flour = float(156)  # grams
            aC_crust_salt = float(.5)  # tsp
            aC_crust_sugar = float(1)  # tbs
            aC_crust_butter = float(114)  # grams
            aC_crust_water = float(59)  # ml
            aC_filling_apples = float(9)  # apples
            aC_filling_sugar = float(100)  # grams
            aC_filling_flour = float(3)  # tbs
            aC_filling_cinnamon = float(1.5)  # tsp
            aC_topping_sugar = float(67)  # grams
            aC_topping_flour = float(94)  # grams
            aC_topping_butter = float(89)  # grams
            aC_topping_cinnamon = float(.5)  # tsp
            aC_topping_salt = float(.25)  # tsp
            aC_scaling = pie_quantity / int(10)  # number of servings
            print("Amount of flour: ",
                  format(aC_crust_flour * aC_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(aC_crust_salt * aC_scaling, ".2f"),
                  " tsp", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ", format(aC_crust_sugar *
                                                         aC_scaling, ".2f"),
                  " tbs", sep='')
            sleep(1.5)
            print("Amount of unsalted butter: ", format(aC_crust_butter *
                                                        aC_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of water: ", format(aC_crust_water * aC_scaling,
                                              ".2f"), " grams", sep='')
            sleep(1.5)
            print("Below is the quantity needed for the pie filling. ")
            sleep(1.5)
            print("Amount of apples: ", format(aC_filling_apples * aC_scaling,
                                               ".2f"), " apples", sep='')
            sleep(1.5)
            print("Amount of granulated sugar: ", format(aC_filling_sugar *
                                                         aC_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of flour: ",
                  format(aC_filling_flour * aC_scaling, ".2f"), " tbs",
                  sep='')
            sleep(1.5)
            print("Amount of cinnamon: ",
                  format(aC_filling_cinnamon * aC_scaling,
                         ".2f"), "tsp", sep='')
            sleep(1.5)
            print("Below is the quantity needed for the pie topping.")
            sleep(1.5)
            print("Amount of granulated sugar: ", format(aC_topping_sugar *
                                                         aC_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of flour: ",
                  format(aC_topping_flour * aC_scaling, ".2f"), " grams",
                  sep='')
            sleep(1.5)
            print("Amount of unsalted butter: ", format(aC_topping_butter *
                                                        aC_scaling, ".2f"),
                  " grams", sep='')
            sleep(1.5)
            print("Amount of cinnamon: ",
                  format(aC_topping_cinnamon * aC_scaling,
                         ".2f"), " tsp", sep='')
            sleep(1.5)
            print("Amount of salt: ",
                  format(aC_topping_salt * aC_scaling, ".2f"),
                  " tsp", sep='')
    sleep(1.5)
    print("Happy Baking!")


main()


def whole_num(number):
    """
Code to get a whole number, and hope the program doesn't crash
    :param number: gets input from user
    :return: hopefully whole number from user
    """
    value = None
    input_Validation = True
    while input_Validation:
        try:
            value = int(input(number))
            input_Validation = False
        except:
            print("Please enter valid input.")
    return value


def valid_num(directions):
    """
This code is to obtain valid input for the code that didn't fit into my main
program, and make sure the programs doesn't crash
    :param directions: tells the user that type of input to enter
    :return: the input that the user entered
    """
    val = None
    input_Validation = True
    while input_Validation:
        try:
            val = float(input(directions))
            input_Validation = False
        except:
            print("Please enter valid input.")
    return val


def misc():
    """
this function contains all the code/requirements that did not make sense in my
main program
    """
    # Everything under this comment line is the requirements that I couldn't
    # integrate smoothly into the cookie idea
    # **
    # i used ** to raise a number to another number that was input by the user
    sleep(1.5)
    print("And now time for some miscellaneous, but cool code!")
    sleep(1.5)
    print("Want to know what a number raised to a power is?")
    sleep(2)
    num1 = valid_num("Enter first number.")
    num2 = valid_num("Enter second number.")
    # num1 = float(input("Enter first number: "))
    # num2 = float(input("Enter second number: "))
    print(num1 ** num2)
    # %
    # i used % to show if the number of cookies eaten by the user was even or
    # odd
    print(
        "What about knowing if the amount of cookies you ate was even or odd?")
    sleep(2)
    cookies_eaten = valid_num("Enter the number of cookies you ate:")
    # cookies_eaten = float(input("Enter the number of cookies you ate: "))
    if (cookies_eaten % 2) == 0:
        print("Even")
    else:
        print("Odd")
    # //
    # i used // to demonstrate floor division using numbers input by the user
    print("Lets see the result of floor division.")
    first_number = valid_num("Enter first number.")
    second_number = valid_num("Enter second number.")
    # first_number = float(input("Enter first number: "))
    # second_number = float(input("Enter second number: "))
    answer = (first_number // second_number)
    print(answer, "is the result of floor division")
    # +
    # i used + to add two numbers entered by the user
    print("Lets take a step back and do some simple addition.")
    sleep(2)
    addition_one = valid_num("Enter first number.")
    addition_two = valid_num("Enter second number:")
    # addition_one = float(input("Enter first number: "))
    # addition_two = float(input("Enter second number: "))
    print(addition_one + addition_two)
    # -
    # i used - to subtract two numbers provided by the user
    print("Lets try doing the opposite of addition, subtraction.")
    sleep(2)
    sub_one = valid_num("Enter first number.")
    sub_two = valid_num("Enter second number.")
    # sub_one = float(input("Enter first number: "))
    # sub_two = float(input("Enter second number: "))
    print(sub_one - sub_two)
    # string operators
    # *
    # i used the * to repeat a word 100 times back to back
    print("Want to see anything repeated 100 times continuously?")
    sleep(2)
    print("Lets try it!")
    sleep(2)
    word_of_choice = input("Enter anything: ")
    print(word_of_choice * 100)
    print("Ta-Da!")
    # +
    # i used the + to combine an adjective and a noun that was input by the
    # user
    print("Let try describing different nouns.")
    sleep(2)
    word1 = input("Enter adjective: ")
    word2 = input("Enter noun: ")
    print(word1 + " " + word2)
    sleep(2)
    # using shortcut operators
    # +=
    print("Now were going to see how many desserts we've eaten collectively!")
    sleep(1.5)
    dessert_number = valid_num("Enter the number of desserts you've had.")
    # dessert_number = int(input("Enter the number of desserts you've had: "))
    dessert_number += 3
    print("We've had", dessert_number, "desserts collectively!")
    # -=
    sleep(2)
    print("Let's see how many more desserts you've eaten compared to how many "
          "there are.")
    sleep(1.5)
    dessert_total = valid_num("Enter the number of desserts you've had.")
    # dessert_total = int(input("Enter the number of desserts you've had: "))
    dessert_total -= 9
    print("You've had", dessert_total,
          "more desserts compared to how many there "
          "are.")
    # using relational operators ( == & != ) , if/else statement, and while
    # loop
    sleep(2)
    print(
        "I'm thinking of a number 1 through 10, lets see if you can guess it!")
    sleep(1.5)
    user_guess = 0
    while user_guess != 5:
        user_guess = whole_num("Enter your guess.")
        # user_guess = valid_num("Enter your guess.")
        # user_guess = int(input("Enter your guess: "))
        if user_guess == 5:
            print("You've guessed my number!")
        else:
            print("Try again.")
            sleep(1.5)
    # using < and if-elif
    print("Lets compare two different numbers to see which is higher.")
    sleep(1.5)
    number_one = valid_num("Enter a number.")
    number_two = valid_num("Enter another number.")
    # number_one = int(input("Enter a number: "))
    # number_two = int(input("Enter another number: "))
    if number_one < number_two:
        print(number_two, "is the higher number.")
    elif number_two < number_one:
        print(number_one, "is the higher number.")
    # using range, for, and in
    sleep(1.5)
    print(
        "Now we're going to print out consecutive numbers stopping at a "
        "certain number.")
    sleep(1.5)
    range_number = int(input("Enter a whole number."))

    # range_number = int(input("Enter the ending number: "))
    for range_number in range(range_number + 1):
        print(range_number)
    # using not
    sleep(1.5)
    print("Lets see if you can guess a number higher than I am thinking of.")
    sleep(1.5)
    not_number = valid_num("Enter a number.")
    # not_number = int(input("Enter a number: "))
    if not not_number > 7:
        print("Sorry, you guessed a lower number")
    else:
        print("Congrats, you guessed a higher number!")
    # using and
    sleep(1.5)
    print("Enter a number 1 through 10, or else. :) ")
    sleep(1.5)
    and_number = valid_num("Enter a number.")
    # and_number = int(input("Enter a number: "))
    if 1 <= and_number <= 10:
        print("Great job!")
    else:
        print("Listen to instructions next time. :(")
    # using or
    sleep(1.5)
    print("Time to see if you should make dessert!")
    sleep(1.5)
    dessert_time = str(input("Do you have at least 1 hour to spare?: "))
    if dessert_time == "Yes" or dessert_time == "YES" or dessert_time == "yes":
        print("You have time to make dessert!")
        print(":)")
    else:
        print("You don't have time to make dessert.")
        print(":(")


misc()

# # using functions
# def square_area(number):
#     return number * number
# 
# 
# print("Lets find the area of square together.")
# sleep(1.5)
# number = int(input("Enter a number: "))
# print("The area of the square is", square_area(number), "cm squared.")
# 
# 
# def message():
#     print("Better late than never... ._.")
# 
# 
# def main():
#     sleep(1.5)
#     print("This is my integration project so far!")
#     sleep(1.5)
#     message()
# 
# 
# main()
# sleep(1.5)
# print("You've reached the end of Sprint 2")
# special thanks to google and pycharm because i misspelled so many words
# during sprint 2, and to the SAs who helped me narrow down my ideas and helped
# during class time :)
