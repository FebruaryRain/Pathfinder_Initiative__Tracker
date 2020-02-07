

from random import randint

#####
# Instructions and Keywords Displays
#####


def display_instructions():
    Instructions = """
    This is a program to aid in the tracking of initiative in Pathfinder. \n 
    You will be asked for the number of combatants. This is all Players and NPCs, at the start of the combat.
    Combatants who arrive later in the combat are supported.
    You must enter the number of combatants first. 
    You will then be asked for a combatant's initiative score.
    If there is a tie, then you will be asked for a combatant's Dex modifier.
    If there is still a tie, after inputting the Dex modifier, this program will 'flip a coin' and tell you who goes first.
    Who's turn it currently is has to be tracked by the user. The game will merely display the order of combat."""
    print(Instructions)
    return


def display_keywords():
    keywords_instructions = """
    The keyword commands are displayed below
    Keywords are to be typed in lower case only.
    help    display the keyword command screen
    new     create a new combat session
    dis     display the current session's combatants in initiative order
    addcom  add a combatant mid-combat
    rmcom   remove a combatant mid-combat
    quit    quit the current combat session, ready to start a new one
    """
    print(keywords_instructions)
    return


def display_opening_screen():
    display_instructions()
    display_keywords()
    return


#####
# Messages for user input
#####


def await_command():
    return str(input("Please enter a command.\n"))


def confirmation():
    #response = 
    if input("Confirm (y/n):") == "y":
        return False
    else:
        return True


def ask_for_combatant_name():
    return input("Combatant name: ")


def deal_with_possessive_of_names(name):
    if name[-1] == 's':
        return (name + "'") 
    else:
        return (name + "'s")


def ask_for_dex_mods(combatant):
    message = "Enter " + deal_with_possessive_of_names(combatant) + " Dexterity Modifier:"
    return int(input(message))


def ask_for_combatant_initiative(combatant):
    return input(deal_with_possessive_of_names(combatant) + " initiative:")


def how_many_combatants():
    return int(input("How many combatants are there? "))


#####
# New Combat Session
#####


def create_new_combat_session(): # Needs a check to ensure that there are not two of the same combatants in there
    combatant_dict = {}
    num_combatants = how_many_combatants()
    for i in range(0, num_combatants):
        combatant_dict = get_the_list_of_combatants_with_initiatives(combatant_dict, i)
    return combatant_dict


def get_the_list_of_combatants_with_initiatives(combatant_dict, i):
    bask_for_this_combatant = True
    buser_unhappy = True
    while bask_for_this_combatant or buser_unhappy:
        print("Combatant", (i+1))
        combatant_name = ask_for_combatant_name()
        combatant_initiative = ask_for_combatant_initiative(combatant_name)

        if there_are_no_combatants_of_that_name_present(combatant_dict, combatant_name): # True if no duplicates
            bask_for_this_combatant = False # Proceed to the next user
            combatant_dict[combatant_name] = combatant_initiative
            buser_unhappy = confirmation() # False when happy
            if buser_unhappy:
                combatant_dict.popitem()
        else:
            print(" **** Please ensure that you do not enter two combatants with the same name. ****")
            bask_for_this_combatant = True
            buser_unhappy = True
        
    return combatant_dict


#def get_combatant_name_and_intiative():


#####
# List ordering
#####


def bubble_sort_session(combatant_list, initiative_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(initiative_list)-1):
            if initiative_list[i] < initiative_list[i+1]:
                combatant_list, initiative_list = swap_positions(combatant_list, initiative_list, i)
                swapped = True
    return combatant_list, initiative_list


                
def swap_positions(list1, list2, num):
    list1[num], list1[num+1] = list1[num+1], list1[num]
    list2[num], list2[num+1] = list2[num+1], list2[num]
    return list1, list2


def sort_combatants_by_initiative(combat_session):
    combatant_list = []
    initiative_list = []
    for combatant, initiative in combat_session.items():
        combatant_list.append(combatant)
        initiative_list.append(initiative)
        combatant_list, initiative_list = bubble_sort_session(combatant_list, initiative_list)
    print(combatant_list)
    print(initiative_list)
    combatant_list, initiative_list = deal_with_ties(combatant_list, initiative_list)
    print(combatant_list)
    print(initiative_list)
    return combatant_list, initiative_list

def coinflip():
    result = randint(1,2)
    if result == 1:
        return True
    else:
        return False


#####
# Dealing with Ties in Scores
#####


def deal_with_dex_ties(combatant_list, initiative_list, i):
    bresult = coinflip()
    if bresult:
        combatant_list, initiative_list = swap_positions(combatant_list, initiative_list, i)
        return combatant_list, initiative_list
    else:
        return combatant_list, initiative_list


def deal_with_ties(combatant_list, initiative_list):
    for i in range(0, len(initiative_list) - 1):
        if initiative_list[i] == initiative_list[i+1]:
            dex1 = ask_for_dex_mods(combatant_list[i])
            dex2 = ask_for_dex_mods(combatant_list[i+1])
            if (dex2 >= dex1 + 1): 
                combatant_list, initiative_list = swap_positions(combatant_list, initiative_list, i)
            elif (dex1 == dex2):
                combatant_list, initiative_list = deal_with_dex_ties(combatant_list, initiative_list, i)
    bubble_sort_session(combatant_list, initiative_list)
    return combatant_list, initiative_list
                

def ties(combatant_list, initiative_list):
    tied_combatants_names = []
    tied_combatants_initiatives = []
    for i in range(0, len(initiative_list)):
        for j in range(0, len(initiative_list)):
            if (initiative_list[i] == initiative_list[j]) and (i != j):
                tied_combatants_names.append[combatant_list[i]]
                tied_combatants_initiatives[initiative_list[i]]
    
        
    return combatant_list, initiative_list
                
#combatant_list.popitem(combatant_list[i])
#initiative_list.popitem(initiative_list[i])


#####
# Error handling and veracity ensuring
#####

def there_are_no_combatants_of_that_name_present(combatant_dict, combatant_name):
    if combatant_name in combatant_dict:
        return False
    else: 
        return True

def display_unknown_command_message():
    print("I'm sorry, I don't recognise that command. Type 'help' for information on Keywords")
    return True



#####
# Reporting
#####

def report_initiative_order(combatant_list, initiative_list):
    print("Combatant Order")
    for i in range(0, len(combatant_list)):
        line = ""
        line = combatant_list[i]
        spaces = 8-len(str(initiative_list[i]))
        line = line + " " * spaces + initiative_list[i]
        print(line)
    return
         

def act_on_command(command):
    combatant_list = []
    initiative_list = []
    if command == "help":
        display_keywords()
        return True
    elif command == "new":
        combat_session = create_new_combat_session()
        print(combat_session)
        combatant_list, initiative_list = sort_combatants_by_initiative(combat_session)
        report_initiative_order(combatant_list, initiative_list)

        return True
    #elif command == "addcom"
#       return True
    #elif command == "rmcom"
#       return True
    elif command == "quit":
        return False
    else:
        return display_unknown_command_message()



if __name__ == "__main__":
    display_opening_screen()
    bplaying = True
    while bplaying:
        command = await_command()
        bplaying = act_on_command(command)
