#create a game menu with 4 starting options
import sys
from random import randint

def innitialise_grid():
    board_array = []
    counter = 0
    while counter < 3:
        # blank_list[0]
        board_array.append([])
        new_counter = 0
        while new_counter < 3:
            print("counter: " + str(counter))
            board_array[counter].append(randint(0, 1))  # this is how rng function is made in this case between 0-1
            new_counter = new_counter + 1
        counter = counter + 1
    print(board_array)
    return board_array

def quit_fn():
    print ("Exiting")
    # exiting through while condition makes this statement redundant
    sys.exit()
def save_fn():
    print("saved")
def new_fn():
    print("what would you like to play")
    board_array = innitialise_grid()

    for itemlist in board_array:
        print(itemlist[0], itemlist[1], itemlist[2])
def load_fn():
    print ("loading...")
#wrap map in a function so it can be used multiple times by the meny

# menu = {}
# menu["1"] = "New game"
# menu["2"] = "Save game"
# menu["3"] = "Load game"
# menu["4"] = "Quit"
# for menu_option in menu:
#     print(menu_option+ " " + menu[menu_option])

listmenu = []
listmenu.append("1 New game")
listmenu.append("2 Save game")
listmenu.append("3 Load game")
listmenu.append("4 Quit")
for menu_option in listmenu:
    print(menu_option)

# print(menu["1"])
# print(menu["2"])
# print(menu["3"])
# print(menu["4"])
user_input = 0
while user_input != 4:
    print("what would you like to do")
    user_input = int(input("what would you like to do next"))
    if user_input == 1:
        new_fn()
    elif user_input == 2:
        save_fn()
    elif user_input == 3:
        load_fn()
    elif user_input == 4:
        quit_fn()
    else:
        print ("invalid input")


