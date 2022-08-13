"""
- Blackjack Card Game Release v1.0.0
- https://github.com/anpo1778/Blackjack
- Made by @Anpo1778 on 08/11/2022
- v1.0.0 Release date: 08/11/2022

"""

import random
print('*Blackjack*')
print(' ')
answer = input("Begin? (Y/N) ")

# Definition of lists and variables for functionality of the script

comp_sum_list = []
comp_str_list = []
sum_list = []
str_list = []
comp_game = False
user_game = False
comp_first = False
user_first = False
user_tot_num = 0
comp_tot_num = 0
stand_input = False
user_game_test = False
comp_game_test = False
user_input = " "
game_test = []
reset = False

# Function that adds additonal cards to Dealer's hand
def comp_check(comp_sum_list, reset):
    global comp_first, comp_tot_num, comp_game, comp_str_list
    # Resets lists and variables if user plays another game
    if reset: 
        comp_str_list = []
        comp_first = False
        comp_game = False
        comp_tot_num = 0
        reset = False
    
    print(" ")
    comp_new_num = random.randint(1, 10)
    comp_sum_list.append(comp_new_num)
    comp_length = len(comp_sum_list)
    
    if not comp_first: 
        for i in range(comp_length):
            comp_str_list.append(str(comp_sum_list[i]))
    else:
        index = comp_length - 1
        comp_str_list.append(str(comp_sum_list[index]))
    print("Dealer's Cards " + (", ").join(comp_str_list))
    
    if not comp_first: 
        for i in range(comp_length):
            comp_tot_num = comp_tot_num + comp_sum_list[i]
    else:
        index = comp_length - 1
        comp_tot_num = comp_tot_num + comp_sum_list[index]
    print("Total Number: " + str(comp_tot_num))
    comp_first = True
    
    comp_game_test = [comp_game, comp_tot_num]
    
    if comp_tot_num < int(21):
        comp_game = True
        comp_game_test = [comp_game, comp_tot_num]
        return comp_game_test
        comp_tot_num = 0
    elif comp_tot_num == int(21):
        comp_game = True
        comp_game_test = [comp_game, comp_tot_num]
        return comp_game_test
        comp_tot_num = 0
    else:
        comp_game = False
        comp_game_test = [comp_game, comp_tot_num]
        return comp_game_test

# Function that adds additonal cards to Dealer's hand
def user_check(sum_list, reset):
    global user_first, user_tot_num, str_list, user_game, stand_input
    # Resets lists and variables if user plays another game
    if reset: 
        str_list = []
        user_first = False
        user_game = False
        stand_input = False
        user_tot_num = 0
        reset = False
    
    user_game_test = [user_game, user_tot_num]
    user_input = input("Hit or Stand? ")
    
    # Functionality for "Stand" input
    if user_input == "Hit" or user_input == "hit":
        print(" ")
        new_num = random.randint(1, 10)
        sum_list.append(new_num)
        length = len(sum_list)
        
        if not user_first: 
            for i in range(length):
                str_list.append(str(sum_list[i]))
        else:
            index = length - 1
            str_list.append(str(sum_list[index]))
        print("Your Numbers: " + (", ").join(str_list))

        if not user_first: 
            for i in range(length):
                user_tot_num = user_tot_num + sum_list[i]
        else:
            index = length - 1
            user_tot_num = user_tot_num + sum_list[index]
        print("Total Number: " + str(user_tot_num))
        user_first = True
        
        if user_tot_num < int(21):
            user_game = True
            stand_input = False
            user_game_test = [user_game, user_tot_num, stand_input]
            return user_game_test
        elif user_tot_num == int(21):
            user_game = True
            stand_input = False
            user_game_test = [user_game, user_tot_num, stand_input]
            return user_game_test
        else:
            user_game = False
            stand_input = False
            user_game_test = [user_game, user_tot_num, stand_input]
            return user_game_test
            user_tot_num = 0
    
    # Functionality for "Stand" input
    elif user_input == "Stand" or user_input == "stand":
        length = len(sum_list)
        print(" ")
        user_tot_num = 0
        for i in range(length):
            user_tot_num = user_tot_num + sum_list[i]
        print("Final Total Number: " + str(user_tot_num))
        user_game = False
        stand_input = True
        user_game_test = [user_game, user_tot_num, stand_input]
        return user_game_test

# Main loop for script functionality      
while True:
    if answer == "Y" or answer == "y":
        # Display code for user's numbers
        sum_list = []
        user_first = False
        user_game = False
        stand_input = False
        user_tot_num = 0
        print(" ")
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        print("Your Numbers: " + str(num1) + ", " + str(num2))
        num_sum = num1 + num2
        print("Total Number: " + str(num_sum))
        sum_list = [num1, num2]
        
        # Display code for computer's numbers
        print(" ")
        comp_sum_list = []
        comp_first = False
        comp_tot_num = 0
        comp_num1 = random.randint(1, 10)
        comp_num2 = random.randint(1, 10)
        print("Dealer's Cards " + str(comp_num1) + ", " + str(comp_num2))
        comp_num_sum = comp_num1 + comp_num2
        print("Total Number: " + str(comp_num_sum))
        comp_sum_list = [comp_num1, comp_num2]
        
        # Calls user/comp functions and checks for wins/loses
        while True:
            user_test = user_check(sum_list, reset)
            comp_test = comp_check(comp_sum_list, reset)
            
            user_list_var = user_test[0]
            comp_list_var = comp_test[0]
            user_list_val = user_test[1]
            comp_list_val = comp_test[1]
            stand_check = user_test[2]
            
            # Checks to see if user won for "Stand" input
            if stand_check and user_list_val > 21 and comp_list_val < 21 or comp_list_val == 21:
                print("Game Over, You Lost! #194")
                break
            if stand_check and user_list_val > 21 and comp_list_val > 21:
                print("Game Over, You Lost! #197")
                break
            if stand_check and user_list_val < 21 or user_list_val == 21:
                if 21 > user_list_val > comp_list_val:
                    print("Game Over, You Won! #201")
                    break
                if 21 > comp_list_val > user_list_val:
                    print("Game Over, You Lost! #204")
                    break
            
            # Checks for double 21+, and double 21s
            if not user_list_var and not comp_list_var and user_list_val > 21 and comp_list_val > 21:
                print("Game Over, You Lost! #209")
                break
            if user_list_var and user_list_val == 21 and comp_list_val == 21:
                print("Game Over, It's a tie! #212")
                break
            
            # Checks if user/comp numbers are 21
            if user_list_var and user_list_val == 21:
                print("Game Over, You Won! #217")
                break
            if comp_list_var and comp_list_val == 21:
                print("Game Over, You Lost! #220")
                break
            
            # Checks if user/comp numbers are over 21
            if not comp_list_var and comp_list_val > 21:
                print("Game Over, You Won! #225")
                break
            if not user_list_var and user_list_val > 21:
                print("Game Over, You Lost! #228")
                break
            
            # Checks if user/comp numbers are under 21
            if user_list_var and user_list_val < 21:
                continue
            if comp_list_var and comp_list_val < 21:
                continue
        
        print(" ")
        replay = input("Play Again? (Y/N) ")
        reset = True
        if replay == "Y" or replay == "y":
            continue
        if replay == "N" or replay == "n":
            break
        
    if answer == "N" or answer == "n":
        break
        
    else:
        break
