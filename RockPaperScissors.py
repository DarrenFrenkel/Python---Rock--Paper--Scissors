# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print ("Sorry, that number it's not an option")
    # convert number to a name using if/elif/else


    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        "Sorry, that name it's not an option"
    

    # convert name to number using if/elif/else



def rpsls(name): 
    # fill in your code below
    name = name_to_number(name)
    player_number = name
    # convert name to player_number using name_to_number
    comp_number = random.randrange(5)
    # compute random guess for comp_number using random.randrange()
    player = (player_number - comp_number)% 5  
    # compute difference of player_number and comp_number modulo five
    computer_guess = number_to_name(comp_number)
    player_guess = number_to_name(player_number)
   
    if player == 1 or player == 2:
        print ("Player chooses " + player_guess)
        print ("Computer choose " + computer_guess)
        print ("player wins!")
        print ("")
    elif player == 3 or player == 4:
        print ("Player chooses " + player_guess)
        print ("Computer choose " + computer_guess)
        print ("computer wins!")
        print ("")
    else:
       print ("Player chooses " + player_guess)
       print ("Computer choose " + computer_guess)
       print ("Player and Computer tie")
       print ("")
    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test my code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




